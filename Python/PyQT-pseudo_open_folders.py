import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout

class PseudoFolderOpener(QWidget):
    def __init__(self):
        super().__init__()

        self.selected_folder_path = ""

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        open_folder_button = QPushButton('Open Folder', self)
        open_folder_button.clicked.connect(self.show_folder_dialog)

        layout.addWidget(open_folder_button)
        self.setLayout(layout)

    def show_folder_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.selected_folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", "", options=options)

        if self.selected_folder_path:
            print(f"Selected Folder: {self.selected_folder_path}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PseudoFolderOpener()
    window.show()
    sys.exit(app.exec_())
