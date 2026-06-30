class VintedTextGenerator:

    def __init__(self):
        pass

    def generate_title(self, brand="unknown", item="clothing", style="streetwear"):
        return f"{brand} {item} {style} | stan idealny | Vinted"

    def generate_description(self, item="ubranie", gender="damskie"):
        return f"""
✨ OPIS PRODUKTU

Sprzedam {gender} {item} w bardzo dobrym stanie.

✔ stan: bardzo dobry
✔ bez plam i uszkodzeń
✔ styl: casual / streetwear
✔ idealne na co dzień

📦 szybka wysyłka
📸 realne zdjęcia produktu

#vinted #moda #streetwear
        """.strip()

    def generate_tags(self, item="clothing"):
        return [
            "vinted",
            "moda",
            "streetwear",
            item,
            "ubrania",
            "fashion",
            "outfit",
            "styl"
        ]

    def generate_category(self, item="bluza"):
        if "bluza" in item.lower():
            return "Bluzy"
        if "spodnie" in item.lower():
            return "Spodnie"
        if "koszulka" in item.lower():
            return "Koszulki"
        return "Inne"

    def estimate_price(self, item="unknown"):
        base = 80

        if "zara" in item.lower():
            base = 60
        if "nike" in item.lower():
            base = 120

        return base
