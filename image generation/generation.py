import openai

response = openai.Image.create(
  prompt="A painting that mixes Van Gogh's sunflowers and Picasso's Munch's Scream.",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)
