# The code snippet is loading a pre-trained AI model called ImageGenerationModel (imagen-3.0-generate-002) on Vertex AI.
#The code calls the generate_image method of the loaded Gemini model.
#The input to the method is a text prompt.
#The code uses Gemini's ability to understand the text prompt and use it to build an AI Image.
#Note: By default, a SynthID watermark is added to images, but you can disable it by specifying the optional parameter add_watermark=False.
#You can't use a seed value and watermark at the same time. 


import argparse
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

def generate_image(
  project_id:str, location:str, output_file:str, prompt:str
) -> vertexai.preview.vision_models.ImageGenerationResponse:
  """ Generate an image using a text prompt.
  Args:
    project_id: google cloud project ID, used to initialize Veretx AI
    location: google cloud region, used to initialize Vertex AI
    output_file: local path to the output image file
    prompt: text prompt describing what you want to see """
  vertexai.init(project=project_id, location=location)
  model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")
  images = model.generate_images(
      prompt=prompt, 
      #optional parameters
      number_of_images =1, 
      seed=1, 
      add_watermark=False, 
  )
  images[0].save(location=output_file)
  return images

generate_image(
  project_id = '"fill project-id"'
  location = '"REGION"'
  output_file='image.jpeg',
  prompt='Create an image of a cricket ground in the heart of Los Angeles',
)
