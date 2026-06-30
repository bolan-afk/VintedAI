from rembg import remove
from PIL import Image
import numpy as np
import io


class BackgroundRemover:

    def __init__(self):
        pass

    def remove_background(self, image_path: str) -> Image.Image:
        """
        Usuwa tło z obrazu ubrania
        """

        with open(image_path, "rb") as f:
            input_data = f.read()

        output_data = remove(input_data)

        image = Image.open(io.BytesIO(output_data)).convert("RGBA")

        return image

    def save_result(self, image: Image.Image, path: str):
        image.save(path, "PNG")
