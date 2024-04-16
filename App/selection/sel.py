# importing libraries
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 500, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()



	# method for components
	def UiComponents(self):

		# creating a QListWidget
		list_widget = QListWidget(self)

		# setting geometry to it
		list_widget.setGeometry(50, 70, 150, 60)

		# list widget items
		item1 = QListWidgetItem("A")
		item2 = QListWidgetItem("B")
		item3 = QListWidgetItem("C")

		# adding items to the list widget
		list_widget.addItem(item1)
		list_widget.addItem(item2)
		list_widget.addItem(item3)

		# setting selection mode property
		list_widget.setSelectionMode(mode=QItemSelection)
		# creating a label
		label = QLabel("GeeksforGeeks", self)

		# setting geometry to the label
		label.setGeometry(230, 80, 280, 80)

		# making label multi line
		label.setWordWrap(True)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
