from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QStackedWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
import os


class Widget(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window
        self.setWindowTitle("QLabel Image Demo")

        # Initialize image list, current index, and file paths set
        self.selected_file_paths = []

        # Create a QStackedWidget to manage images
        self.stacked_widget = QStackedWidget()

        # Create a QLabel to display the image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stacked_widget.addWidget(self.image_label)

        # Create a QPushButton to open the file dialog
        self.select_button = QPushButton("Select Images")
        self.select_button.clicked.connect(self.select_images)

        # Create a QPushButton to go to the previous image
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.show_previous_image)
        self.prev_button.setEnabled(False)  # Initially disabled

        # Create a QPushButton to go to the next image
        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.show_next_image)
        self.next_button.setEnabled(False)  # Initially disabled

        # Create a QPushButton to open the file dialog
        self.remove_button = QPushButton("Remove Image")
        self.remove_button.clicked.connect(self.remove_image)
        self.remove_button.setEnabled(False)

        # Create a QLabel to show information
        self.image_info_label = QLabel()
        self.image_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.select_button)
        button_layout.addWidget(self.next_button)
        button_layout.addWidget(self.remove_button)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        main_layout.addWidget(self.image_info_label)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def select_images(self):
        # Open a file dialog to select multiple images
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Images", "", "Images (*.png)")
        if file_paths:
            for file_path in file_paths:
                # Check if the file path is already selected
                if file_path in self.selected_file_paths:
                    self.main_window.show_status_message(
                        f"Image '{os.path.basename(file_path)}' already selected.", 5000)
                    continue  # Skip if already selected

                # Load the selected image
                pixmap = QPixmap(file_path)

                # Create a QLabel to display the image
                image_label = QLabel()
                image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                # Get the primary screen
                screen = QGuiApplication.primaryScreen()
                screen_geometry = screen.availableGeometry()

                screen_width = screen_geometry.width()
                screen_height = screen_geometry.height()
                image_width = int(screen_width * 0.5)
                image_height = int(screen_height * 0.5)

                # Resize the image to 50% of the screen resolution
                resized_pixmap = pixmap.scaled(image_width, image_height, Qt.AspectRatioMode.KeepAspectRatio)

                # Set the resized pixmap to the QLabel
                image_label.setPixmap(resized_pixmap)

                # Add the QLabel to the stacked widget
                self.stacked_widget.addWidget(image_label)
                self.selected_file_paths.append(file_path)  # Add file path to the set

            # Set the current index to the last added image
            self.stacked_widget.setCurrentIndex(self.stacked_widget.count() - 1)
            self.prev_button.setEnabled(self.stacked_widget.currentIndex() > 1)
            self.next_button.setEnabled(self.stacked_widget.currentIndex() < self.stacked_widget.count() - 1)
            self.remove_button.setEnabled(True)
            self.image_info_label.setText(
                f"Image : {os.path.basename(self.selected_file_paths[self.stacked_widget.currentIndex()-1])}," +
                f" ({self.stacked_widget.currentIndex()}/{self.stacked_widget.count()-1})")

    def remove_image(self):
        self.selected_file_paths.pop(self.stacked_widget.currentIndex()-1)
        self.stacked_widget.removeWidget(self.stacked_widget.currentWidget())
        if self.stacked_widget.currentIndex() == 1:
            self.prev_button.setEnabled(False)
        if self.stacked_widget.currentIndex() == self.stacked_widget.count() - 1:
            self.next_button.setEnabled(False)
        if self.stacked_widget.count() == 1:
            self.remove_button.setEnabled(False)

    def show_previous_image(self):
        if self.stacked_widget.currentIndex() > 0:
            self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex()-1)
            self.prev_button.setEnabled(self.stacked_widget.currentIndex() > 1)
            self.next_button.setEnabled(self.stacked_widget.currentIndex() < self.stacked_widget.count() - 1)

    def show_next_image(self):
        if self.stacked_widget.currentIndex() < self.stacked_widget.count():
            self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex()+1)
            self.prev_button.setEnabled(self.stacked_widget.currentIndex() > 1)
            self.next_button.setEnabled(self.stacked_widget.currentIndex() < self.stacked_widget.count() - 1)
