import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout

class PseudoFileOpener(QWidget):
    def __init__(self):
        super().__init__()

        self.selected_file_path = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        open_file_button = QPushButton('Open File', self)
        open_file_button.clicked.connect(self.show_file_dialog)

        layout.addWidget(open_file_button)
        self.setLayout(layout)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.selected_file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)", options=options)

        if self.selected_file_path:
            print(f"Selected File: {self.selected_file_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PseudoFileOpener()
    window.show()
    sys.exit(app.exec_())
