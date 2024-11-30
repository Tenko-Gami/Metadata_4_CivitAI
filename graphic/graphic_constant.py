from PySide6.QtGui import QGuiApplication

# Get the primary screen
screen = QGuiApplication.primaryScreen()
screen_geometry = screen.availableGeometry()

SCREEN_WIDTH = screen_geometry.width()
SCREEN_HEIGHT = screen_geometry.height()

# Optional: Print the screen dimensions for debugging
print(f"Screen Width: {SCREEN_WIDTH}, Screen Height: {SCREEN_HEIGHT}")