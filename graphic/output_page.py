import os
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (QWidget, QVBoxLayout)
from PySide6.QtWebEngineWidgets import QWebEngineView

CURRENT_DIRECTORY = Path(__file__).resolve().parent


class OutputWidget(QWidget):
    def __init__(self):
        super().__init__()

        filename = os.fspath(CURRENT_DIRECTORY / "./output.html")
        self.url = QUrl.fromLocalFile(filename)

        self.webV = QWebEngineView()
        self.webV.load(self.url)

        layout = QVBoxLayout(self)
        layout.addWidget(self.webV)

    def refresh(self):
        self.webV.load(self.url)
