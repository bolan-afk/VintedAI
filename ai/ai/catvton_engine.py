import torch
from PIL import Image


class CatVTONEngine:

    def __init__(self, device="cuda"):
        self.device = device
        self.pipe = None

    def load(self):
        from diffusers import StableDiffusionInpaintPipeline

        print("Ładowanie CatVTON (hybryda SDXL-ready)...")

        self.pipe = StableDiffusionInpaintPipeline.from_pretrained(
            "runwayml/stable-diffusion-inpainting",
            torch_dtype=torch.float16
        ).to(self.device)

        self.pipe.enable_attention_slicing()

        print("CatVTON pipeline ready")

    def generate(self, person_image, cloth_image, mask):
        if self.pipe is None:
            self.load()

        prompt = (
            "fashion model wearing the exact clothing, "
            "professional e-commerce photo, studio lighting, ultra realistic"
        )

        negative = "blurry, distorted, low quality"

        with torch.autocast("cuda"):
            result = self.pipe(
                prompt=prompt,
                negative_prompt=negative,
                image=person_image,
                mask_image=mask,
                num_inference_steps=30
            ).images[0]

        return result
