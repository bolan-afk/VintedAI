import os
import zipfile
import csv
from datetime import datetime


class ExportPack:

    def __init__(self, output_dir="exports/final_pack"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def export(self, items: list):
        """
        items = [
            {
                "image": path,
                "title": str,
                "description": str,
                "tags": list,
                "price": int
            }
        ]
        """

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pack_dir = os.path.join(self.output_dir, f"pack_{timestamp}")
        os.makedirs(pack_dir, exist_ok=True)

        csv_path = os.path.join(pack_dir, "oferty.csv")

        # CSV EXPORT
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow([
                "title",
                "description",
                "tags",
                "price",
                "image"
            ])

            for item in items:
                writer.writerow([
                    item["title"],
                    item["description"],
                    ",".join(item["tags"]),
                    item["price"],
                    item["image"]
                ])

        # ZIP EXPORT
        zip_path = os.path.join(self.output_dir, f"pack_{timestamp}.zip")

        with zipfile.ZipFile(zip_path, "w") as zipf:
            for root, _, files in os.walk(pack_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, pack_dir)
                    zipf.write(file_path, arcname)

        return zip_path
