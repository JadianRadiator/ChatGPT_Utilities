import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout

class PseudoFolderSaver(QWidget):
    def __init__(self):
        super().__init__()

        self.save_folder_path = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        save_folder_button = QPushButton('Save Folder', self)
        save_folder_button.clicked.connect(self.show_folder_dialog)

        layout.addWidget(save_folder_button)
        self.setLayout(layout)

    def show_folder_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.save_folder_path = QFileDialog.getExistingDirectory(self, "Save Folder", "", options=options)

        if self.save_folder_path:
            print(f"Folder saved to: {self.save_folder_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PseudoFolderSaver()
    window.show()
    sys.exit(app.exec_())
