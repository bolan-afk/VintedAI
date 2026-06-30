import os
import time

from ai.segmentation import BackgroundRemover
from ai.catvton_engine import CatVTONEngine
from ai.sam2_segment import SAM2Segmenter
from ai.sdxl_enhancer import SDXLEnhancer
from ai.vinted_text import VintedTextGenerator


class BatchProcessor:

    def __init__(self, device="cuda"):
        self.device = device

        self.remover = BackgroundRemover()
        self.vton = CatVTONEngine(device=device)
        self.sam = SAM2Segmenter()
        self.enhancer = SDXLEnhancer(device=device)
        self.text = VintedTextGenerator()

        self.output_dir = "exports/batch"
        os.makedirs(self.output_dir, exist_ok=True)

    def process_single(self, image_path: str, index: int):
        print(f"[{index}] Przetwarzanie: {image_path}")

        # 1. remove bg
        cloth = self.remover.remove_background(image_path)

        # 2. mask
        mask = self.sam.get_mask(cloth)

        # 3. try-on
        result = self.vton.generate(cloth, cloth, mask)

        # 4. enhance
        final = self.enhancer.enhance(result)

        # 5. text generation
        title = self.text.generate_title(item="ubranie")
        desc = self.text.generate_description(item="ubranie")
        tags = self.text.generate_tags("ubranie")

        # 6. save
        ts = int(time.time())

        img_path = f"{self.output_dir}/item_{index}_{ts}.png"
        txt_path = f"{self.output_dir}/item_{index}_{ts}.txt"

        final.save(img_path)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("TITLE:\n" + title + "\n\n")
            f.write("DESCRIPTION:\n" + desc + "\n\n")
            f.write("TAGS:\n" + ", ".join(tags))

        return img_path

    def process_batch(self, image_paths: list):
    results = []

    for i, path in enumerate(image_paths):

        cloth = self.remover.remove_background(path)
        mask = self.sam.get_mask(cloth)
        result = self.vton.generate(cloth, cloth, mask)
        final = self.enhancer.enhance(result)

        title = self.text.generate_title(item="ubranie")
        desc = self.text.generate_description(item="ubranie")
        tags = self.text.generate_tags("ubranie")
        price = self.text.estimate_price("ubranie")

        img_path = f"exports/batch/item_{i}.png"
        final.save(img_path)

        results.append({
            "image": img_path,
            "title": title,
            "description": desc,
            "tags": tags,
            "price": price
        })

    return results
