import torch
from PIL import Image


class SDXLEnhancer:

    def __init__(self, device="cuda"):
        self.device = device
        self.pipe = None

    def load(self):
        from diffusers import StableDiffusionUpscalePipeline

        print("Ładowanie SDXL enhancer...")

        self.pipe = StableDiffusionUpscalePipeline.from_pretrained(
            "stabilityai/stable-diffusion-x4-upscaler",
            torch_dtype=torch.float16
        ).to(self.device)

        print("Enhancer ready")

    def enhance(self, image: Image.Image):
        if self.pipe is None:
            self.load()

        prompt = "ultra realistic fashion product photo, sharp details"

        with torch.autocast("cuda"):
            result = self.pipe(
                prompt=prompt,
                image=image
            ).images[0]

        return result
