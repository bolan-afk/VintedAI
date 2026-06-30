
---

## 📄 app.py (START GUI)

To jest **pierwszy działający interfejs**.

```python
import sys
from ai.tryon import VirtualTryOn
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
        self.label.setText("Najpierw wybierz zdjęcie!")
        return

        self.label.setText("Generowanie... (następny etap: AI)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
