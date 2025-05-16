#The code snippet is loading a pre-trained AI model called Gemini (gemini-2.0-flash-001) on Vertex AI.
#The code calls the send_message method of the loaded Gemini model.
#The code uses Gemini's ability to chat. It uses the text provided in the prompt to chat.

# ---- CHAT RESPONSES WITHOUT STREAM ----

from google import genai
from google.genai.types import HttpOptions, ModelContent, Part, UserContent
import logging
from google.cloud import logging as gcp_logging

# ------  Below cloud logging code is for Qwiklab's internal use, do not edit/remove it. --------
# Initialize GCP logging
gcp_logging_client = gcp_logging.Client()
gcp_logging_client.setup_logging()

client = genai.Client(
  vertexai=True, 
  project= 'fill project_id',
  location = 'REGION',
  http_options=HttpOptions(api_version="v1")
)
chat = client.chats.create(
  model = "gemini-2.0-flash-001",
  history=[
    Usercontent(parts = [Part(text="Hello")]), 
    ModelContent(
      parts=[Part(text="Great to meet you. What would you like to know?")], 
    ),  
  ],
)
response = chat.send_message("What are all the colors in a rainbow?")
print(response.text)
response = chat.send_message("Why does it appear when it rains?")
print(response.text)






