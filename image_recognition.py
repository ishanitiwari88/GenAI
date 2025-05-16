'''The code snippet is loading a pre-trained AI model called Gemini (gemini-2.0-flash-001) on Vertex AI.
The code calls the generate_content method of the loaded Gemini model.
The input to the method is an image URI and a prompt containing a question about the image.
The code uses Gemini's ability to understand images and text together. It uses the text provided in the prompt to describe the contents of the image.'''


from google import genai
from google.genai.types import HttpOptions, Part

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=[
        "What is shown in this image?",
        Part.from_uri(
            file_uri="gs://cloud-samples-data/generative-ai/image/scones.jpg",
            mime_type="image/jpeg",
        ),
    ],
)
print(response.text)
