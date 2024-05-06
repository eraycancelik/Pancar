import sys
import time
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QProgressBar

class WorkerThread(QThread):
    progress_update = pyqtSignal(int)

    def run(self):
        for i in range(101):
            time.sleep(0.1)  # Simülasyon amaçlı bekleme
            self.progress_update.emit(i)
            print(i)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread and QProgressBar Example")
        self.setGeometry(100, 100, 400, 200)

        # Ana widget oluştur
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Ana layout oluştur
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # İlerleme çubuğu oluştur
        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        # Başlat düğmesi oluştur
        self.start_button = QPushButton("Başlat")
        self.start_button.clicked.connect(self.start_worker_thread)
        layout.addWidget(self.start_button)

    def start_worker_thread(self):
        # İş parçacığını oluştur ve başlat
        self.worker_thread = WorkerThread()
        self.worker_thread.progress_update.connect(self.update_progress_bar)
        self.worker_thread.start()
        

    def update_progress_bar(self, value):
        # İlerleme çubuğunu güncelle
        self.progress_bar.setValue(value)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
