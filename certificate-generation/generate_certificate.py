import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

def load_api_key():
    """
    Load OpenAI API key from environment variables.
    """
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")

def initialize_openai_client(api_key):
    """
    Initialize OpenAI client with the provided API key.
    """
    return OpenAI(api_key=api_key)

def generate_image(prompt, client):
    """
    Generate an image using OpenAI's DALL-E model.
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        response_format="b64_json",
    )
    return response

def save_image(image_data, filename):
    """
    Save the generated image to a file.
    """
    image_bytes = base64.b64decode(image_data)
    with open(filename, 'wb') as file:
        file.write(image_bytes)

def main():
    """
    Main function to run the script.
    """
    # Use placeholders in the prompt for dynamic values
    prompt = '''
    Generate a certificate with light yellow background and black texts. Do not add a logo but leave space for it.
    Only around the edges you can make a plain dark color for beauty. Otherwise it should be a completely
    plain certificate. In the middel do leave space for Name, Date and Signature. And also leave space for
    the name of the organization at the top middle and right below it should be where you leave space for the logo.
    I want you to write Certificate of Accomplishment in the middle as well right above the name. 
    '''

    api_key = load_api_key()
    openai_client = initialize_openai_client(api_key)

    response = generate_image(prompt, openai_client)
    image_path = "generated_certificate.jpg"
    save_image(response.data[0].b64_json, image_path)

    print(f"Certificate generated successfully. Image saved as {image_path}.")

if __name__ == "__main__":
    main()
