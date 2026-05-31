import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# lets test the client
response = client.models.generate_content(model="gemini-3.5-flash", contents="What is the capital of France?")
print(response.text)