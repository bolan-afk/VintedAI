import torch
from PIL import Image


class LocalTryOnEngine:

    def __init__(self, device="cuda"):
        self.device = device

        # tutaj później załadujemy CatVTON
        self.model = None

    def load_model(self):
        """
        Ładowanie modelu CatVTON
        (w kolejnym kroku dodamy realny checkpoint)
        """
        print("Ładowanie modelu try-on...")

        # placeholder - struktura pod realny model
        self.model = "catvton_loaded"

        print("Model gotowy!")

    def generate(self, person_image: Image.Image, clothing_image: Image.Image):
        """
        Generuje modela w ubraniu
        """

        if self.model is None:
            self.load_model()

        # ⚠️ placeholder inference (tu później CatVTON forward pass)
        result = self._fake_inference(person_image, clothing_image)

        return result

    def _fake_inference(self, person, cloth):
        """
        Tymczasowy wynik testowy
        """

        # na tym etapie tylko symulujemy pipeline
        # później zastąpimy realnym modelem diffusion

        return person.copy()
