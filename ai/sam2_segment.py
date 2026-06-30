from PIL import Image
import numpy as np


class SAM2Segmenter:

    def __init__(self):
        self.model = None

    def load(self):
        """
        Tu będzie SAM2 (Segment Anything v2)
        """
        print("Ładowanie SAM2...")
        self.model = "sam2_loaded"
        print("SAM2 gotowy")

    def get_mask(self, image: Image.Image):
        """
        Zwraca maskę ubrania
        (na tym etapie placeholder + heurystyka)
        """

        if self.model is None:
            self.load()

        # pseudo-mask (w realu SAM2 generuje segmentację)
        mask = Image.new("L", image.size, 255)

        return mask
