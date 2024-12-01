from PySide6.QtWidgets import QWidget, QHBoxLayout, QTabWidget
from graphic.img_refactor_page import Widget as ImageRefactorWidget


class Widget(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.setWindowTitle("QTabWidgetDemo Demo")

        tab_widget = QTabWidget(self)

        # Image refactor
        widget_img = ImageRefactorWidget(main_window)  # Pass the MainWindow instance

        # Outputs
        widget_output = QWidget()

        # Error
        widget_error = QWidget()

        # Add tabs to widget
        tab_widget.addTab(widget_img, "Image refactor")
        tab_widget.addTab(widget_output, "Output")
        tab_widget.addTab(widget_error, "Error")

        layout = QHBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)
