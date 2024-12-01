from PySide6.QtWidgets import QApplication, QMainWindow
from graphic.principal import TabWidget
import sys
from PySide6.QtGui import QGuiApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Get the primary screen
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Calculate 50% of the screen width and height
        window_width = int(screen_geometry.width() * 0.5)
        window_height = int(screen_geometry.height() * 0.5)

        # Set the window size
        self.resize(window_width, window_height)

        # Set the window title
        self.setWindowTitle("ComfyUi to civitAI metadata")

        # Create the central widget
        self.principal_widget = TabWidget(self)  # Pass the MainWindow instance
        self.setCentralWidget(self.principal_widget)

        # Create a status bar
        self.status_bar = self.statusBar()

    def show_status_message(self, message, duration=5000):
        self.status_bar.showMessage(message, duration)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
