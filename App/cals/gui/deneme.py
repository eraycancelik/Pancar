import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QFormLayout
import shelve

class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super(InfoDialog, self).__init__(parent)
        self.setWindowTitle("Bilgi Girişi")
        
        self.name_label = QLabel("Ad:")
        self.name_line_edit = QLineEdit()

        self.age_label = QLabel("Yaş:")
        self.age_line_edit = QLineEdit()

        self.ok_button = QPushButton("Tamam")
        self.ok_button.clicked.connect(self.accept)

        layout = QFormLayout()
        layout.addRow(self.name_label, self.name_line_edit)
        layout.addRow(self.age_label, self.age_line_edit)
        layout.addRow(self.ok_button)

        self.setLayout(layout)

    def get_info(self):
        name = self.name_line_edit.text()
        age = self.age_line_edit.text()
        return name, age


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Ana Pencere")
        
        self.info_dialog = InfoDialog(self)

        self.show_info_button = QPushButton("Bilgi Göster")
        self.show_info_button.clicked.connect(self.show_info_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.show_info_button)

        self.setLayout(layout)

    def show_info_dialog(self):
        result = self.info_dialog.exec_()
        if result == QDialog.Accepted:
            name, age = self.info_dialog.get_info()
            self.save_to_database(name, age)

    def save_to_database(self, name, age):
        with shelve.open("database.db") as db:
            # Burada shelve veritabanına gerekli bilgileri ekleyebilirsiniz
            # Örneğin:
            # db['name'] = name
            # db['age'] = age
            print(f"Bilgiler başarıyla kaydedildi: Ad: {name}, Yaş: {age}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
