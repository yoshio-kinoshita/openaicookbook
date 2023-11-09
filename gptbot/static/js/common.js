document.addEventListener('DOMContentLoaded', function () {
    var myForm = document.getElementById('myForm');
    myForm.addEventListener('submit', function (event) {
        event.preventDefault();
        var msg = document.getElementById('user_input').value;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/chat');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onload = function () {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText).response;
                document.getElementById('response').innerHTML = response;
            } else {
                alert('request failed ' + xhr.statusText);
            }
        };
        xhr.send(JSON.stringify({ user_input: msg }));
    });
});

const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user_input');
const submitBtn = document.getElementById('submit-btn');

submitBtn.addEventListener('click', () => {
    const userMessage = userInput.value;
    displayUserMessage(userMessage);
    sendToBot(userMessage);
    userInput.value = '';
});

function displayUserMessage(message) {
    const userDiv = document.createElement('div');
    userDiv.classList.add('user-message');
    userDiv.textContent = message;
    chatLog.appendChild(userDiv);
}

function displayBotMessage(message) {
    const botDiv = document.createElement('div');
    botDiv.classList.add('bot-message');
    botDiv.innerHTML = message;
    chatLog.appendChild(botDiv);
}

function sendToBot(message) {

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/chat');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText).response;
            displayBotMessage(response);
        } else {
            alert('request failed ' + xhr.statusText);
        }
    };
    xhr.send(JSON.stringify({ user_input: message }));
}