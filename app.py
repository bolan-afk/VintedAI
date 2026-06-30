
---

## 📄 app.py (START GUI)

To jest **pierwszy działający interfejs**.

```python
import sys
from ai.vinted_text import VintedTextGenerator
from ai.catvton_engine import CatVTONEngine
from ai.segmentation import BackgroundRemover
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QComboBox, QHBoxLayout
)
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VintedAI - Generator zdjęć")
        self.setMinimumSize(900, 600)

        self.image_path = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Dodaj zdjęcie produktu")
        layout.addWidget(self.label)

        self.btn_load = QPushButton("Wybierz zdjęcie")
        self.btn_load.clicked.connect(self.load_image)
        layout.addWidget(self.btn_load)

        self.image_preview = QLabel("Podgląd")
        self.image_preview.setFixedHeight(300)
        layout.addWidget(self.image_preview)

        gender_layout = QHBoxLayout()
        self.gender = QComboBox()
        self.gender.addItems(["Kobieta", "Mężczyzna"])
        gender_layout.addWidget(QLabel("Płeć:"))
        gender_layout.addWidget(self.gender)
        layout.addLayout(gender_layout)

        self.btn_generate = QPushButton("GENERUJ (placeholder)")
        self.btn_generate.clicked.connect(self.generate)
        layout.addWidget(self.btn_generate)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Wybierz zdjęcie", "", "Images (*.png *.jpg *.jpeg)"
        )

        if file_path:
            self.image_path = file_path
            pixmap = QPixmap(file_path)
            self.image_preview.setPixmap(pixmap.scaledToWidth(400))

    def generate(self):
    if not self.image_path:
        self.label.setText("Dodaj zdjęcie!")
        return

    from ai.segmentation import BackgroundRemover
    from ai.sam2_segment import SAM2Segmenter
    from ai.catvton_engine import CatVTONEngine
    from ai.sdxl_enhancer import SDXLEnhancer

    import os, time

    self.label.setText("1/4 Usuwanie tła...")

    remover = BackgroundRemover()
    cloth = remover.remove_background(self.image_path)

    os.makedirs("cache", exist_ok=True)

    cloth_path = f"cache/cloth_{int(time.time())}.png"
    cloth.save(cloth_path)

    self.label.setText("2/4 Segmentacja SAM2...")

    sam = SAM2Segmenter()
    mask = sam.get_mask(cloth)

    self.label.setText("3/4 CatVTON generuje modela...")

    vton = CatVTONEngine(device="cuda")
    result = vton.generate(cloth, cloth, mask)

    self.label.setText("4/4 Ulepszanie jakości...")

    enhancer = SDXLEnhancer(device="cuda")
    final = enhancer.enhance(result)

    out_path = f"exports/final_{int(time.time())}.png"
    os.makedirs("exports", exist_ok=True)

    final.save(out_path)

    from PySide6.QtGui import QPixmap

    self.label.setText("Gotowe (HYBRYDA AI)")

    self.image_preview.setPixmap(QPixmap(out_path).scaledToWidth(400))
text_gen = VintedTextGenerator()

title = text_gen.generate_title(
    brand="Unknown",
    item="odzież",
    style="fashion"
)

description = text_gen.generate_description(
    item="odzież",
    gender=self.gender.currentText().lower()
)

tags = text_gen.generate_tags("odzież")
category = text_gen.generate_category("odzież")
price = text_gen.estimate_price("odzież")

print("\n=== VINTED AI ===")
print("Tytuł:", title)
print("Kategoria:", category)
print("Cena:", price)
print("Tagi:", tags)
print("Opis:", description)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
