from PIL import Image
import numpy as np
import cv2


def load_image(path: str):
    return Image.open(path).convert("RGB")


def pil_to_cv2(img: Image.Image):
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)


def cv2_to_pil(img):
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def resize_image(img: Image.Image, size=1024):
    return img.resize((size, size))
