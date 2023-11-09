import socketio
import openai
import os

# Set up Socket.IO server
sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Set up OpenAI API credentials
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Socket.IO event handlers
@sio.event
def connect(sid, environ):
    print('Client connected:', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)

@sio.event
def chat_message(sid, message):
    print('Message received from client:', message)

    # Send message to OpenAI Chat API
    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': message}
        ],
        max_tokens=50,  # Number of tokens to include in each response chunk
        temperature=0.7,  # Controls the randomness of the generated text
        n=5  # Number of response chunks to generate
    )

    # Get the generated replies from OpenAI
    replies = [choice.message.content for choice in response.choices]

    # Send replies to the client
    for i, reply in enumerate(replies):
        sio.emit('chat_message', {'chunk': i, 'message': reply}, room=sid)

# Start the Socket.IO server
if __name__ == '__main__':
    app.run()