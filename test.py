from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
import sys

class Popup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(0, 0, 450, 60)

        self.result = None
        
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Type your query...")
        self.input_box.setGeometry(10, 10, 430, 50)
        self.input_box.returnPressed.connect(self.on_enter)
        
        mouse_position = QCursor.pos()  # Get global mouse position
        self.move(mouse_position.x(), mouse_position.y())
        print(self.x)
        
        self.input_box.setFocus()
        
    def keyPressEvent(self, event):
        # Close and cancel on pressing Escape
        if event.key() == Qt.Key.Key_Escape:
            self.result = None
            self.close()
    
    def on_enter(self):
        # Save the input text and close the window
        self.result = self.input_box.text()
        self.close()

my_sheet = """
    QMainWindow {
        background-color: transparent;
    }
    QLineEdit {
        background-color: rgba(255, 240, 126, 0.275);
        border: 1px solid rgba(99, 93, 48, 0.275);
        border-radius: 10px;
        padding: 5px;
        color: rgba(244, 255, 126, 0.796);;
        font-weight: bold;
        font-size: 16pt;
    }
    QLineEdit:focus {
        border: 1px solid rgba(99, 93, 48, 0.275);
    }
"""


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(my_sheet)
    window = Popup()
    window.show()
    
    # Wait for the user to close the popup
    app.exec()
    
    # Return the result of the input
    return window.result

if __name__ == "__main__":
    result = main()
    if result is not None:
        print(f"You typed: {result}")
    else:
        print("Input was canceled.")