import requests
import base64
from PIL import Image
import io


class VirtualTryOn:

    def __init__(self):
        # przykładowe API (można podmienić później na CatVTON lokalnie)
        self.api_url = "https://api.example-vton.com/generate"
        self.api_key = "demo-key"

    def encode_image(self, image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    def generate_model(self, clothing_path, gender="kobieta", body_type="normalna"):
        """
        Generuje modela w ubraniu
        """

        payload = {
            "api_key": self.api_key,
            "clothing_image": self.encode_image(clothing_path),
            "gender": gender,
            "body_type": body_type,
            "style": "studio fashion photo"
        }

        # ⚠️ placeholder request (API w kolejnym kroku możemy podmienić)
        response = requests.post(self.api_url, json=payload)

        if response.status_code != 200:
            raise Exception("Błąd generowania AI")

        image_bytes = base64.b64decode(response.json()["image"])

        return Image.open(io.BytesIO(image_bytes))
