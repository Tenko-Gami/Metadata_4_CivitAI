from PySide6.QtWidgets import QWidget, QHBoxLayout, QTabWidget
from graphic.img_refactor_page import ImageRefactorWidget
from graphic.output_page import OutputWidget


class TabWidget(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        tab_widget = QTabWidget(self)

        # Outputs
        self.widget_output = OutputWidget()

        # Image refactor
        self.widget_img = ImageRefactorWidget(main_window, self.widget_output)  # Pass the MainWindow instance

        # Error
        widget_error = QWidget()

        # Add tabs to widget
        tab_widget.addTab(self.widget_img, "Image refactor")
        tab_widget.addTab(self.widget_output, "Output")
        tab_widget.addTab(widget_error, "Error")

        layout = QHBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)
