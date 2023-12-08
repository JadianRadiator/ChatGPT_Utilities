import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout

class PseudoFileSaver(QWidget):
    def __init__(self):
        super().__init__()

        self.save_file_path = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        save_file_button = QPushButton('Save File', self)
        save_file_button.clicked.connect(self.show_file_dialog)

        layout.addWidget(save_file_button)
        self.setLayout(layout)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.save_file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options)

        if self.save_file_path:
            print(f"File saved to: {self.save_file_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PseudoFileSaver()
    window.show()
    sys.exit(app.exec_())
