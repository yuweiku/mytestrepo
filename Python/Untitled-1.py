
#%%
import openai

# Replace 'your-new-api-key' with your actual new API key
prompt = """
A young Taiwanese girl walking on an old Japanese street looking for local gifts. The street is lined with traditional Japanese wooden buildings, lanterns, and shop signs. The girl is wearing casual clothes, and she has a curious and happy expression. The shops have various local items displayed, such as handmade crafts, souvenirs, and traditional sweets. The scene is set during a sunny day with a clear blue sky, creating a warm and inviting atmosphere.
"""

# Generate an image using the updated OpenAI API
response = openai.Image.create_variation(
    prompt=prompt,
    n=1,
    size="1024x1024"
)

# Get the generated image URL
image_url = response['data'][0]['url']
print("Generated Image URL:", image_url)
#%%