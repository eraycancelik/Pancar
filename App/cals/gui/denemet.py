from PyQt5.QtWidgets import (
    QApplication,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Veritabanından çekilen bilgileri burada ekleyin
        data_from_database = ["Item 1", "Item 2", "Item 3"]

        list_widget = QListWidget(self)

        for item_text in data_from_database:
            item = QListWidgetItem(item_text)
            list_widget.addItem(item)

        layout.addWidget(list_widget)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
