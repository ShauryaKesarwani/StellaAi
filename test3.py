from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtCore import Qt, QTimer

class LoadingCursorExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Cursor Example")
        layout = QVBoxLayout(self)

        self.label = QLabel("Click the button to simulate a loading process.")
        layout.addWidget(self.label)

        self.button = QPushButton("Start Loading")
        self.button.clicked.connect(self.start_loading_process)
        layout.addWidget(self.button)

    def start_loading_process(self):
        # Load the spinning circle PNG as a cursor
        pixmap = QPixmap("./Media/Magic Loading.png")  # Replace with your PNG path
        scaled_pixmap = pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        cursor = QCursor(scaled_pixmap)

        # Set the custom cursor
        QApplication.setOverrideCursor(cursor)

        # Simulate a long-running process
        QTimer.singleShot(3000, self.end_loading_process)  # Simulate 3 seconds of work

    def end_loading_process(self):
        # Restore the default cursor
        QApplication.restoreOverrideCursor()
        self.label.setText("Loading process completed!")

if __name__ == "__main__":
    app = QApplication([])

    widget = LoadingCursorExample()
    widget.show()

    app.exec()
