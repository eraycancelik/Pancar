from PySide6.QtWidgets import QMessageBox, QWidget, QPushButton, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons program")

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_critical)
        buttons_layout.addWidget(button_question)
        buttons_layout.addWidget(button_information)
        buttons_layout.addWidget(button_warning)
        buttons_layout.addWidget(button_about)

        self.setLayout(buttons_layout)

    def button_clicked_critical(self):
        ret = QMessageBox.critical(
            self,
            "Message Title",
            "Critical Message!",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")

    def button_clicked_information(self):
        ret = QMessageBox.information(
            self,
            "Message Title",
            "Informative Message",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")

    def button_clicked_warning(self):
        ret = QMessageBox.warning(
            self,
            "Message Title",
            "Warning Message!",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")

    def button_clicked_about(self):
        ret = QMessageBox.about(self, "Message Title", "About Message")
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")

    def button_clicked_question(self):
        ret = QMessageBox.question(
            self,
            "Message Title",
            "Question Message",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
