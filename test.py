from PyQt6 import QtWidgets, QtCore
from App.package.ui import report_progress

def update_progress(ui):
    for i in range(10):
        ui.progressBar.setValue(i)
        QtCore.QThread.msleep(1000)  # 1000 milisaniye (1 saniye) bekle

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    raporProgressWindow = QtWidgets.QDialog()
    ui = report_progress.Ui_Dialog()
    ui.setupUi(raporProgressWindow)
    raporProgressWindow.setModal(True)
    ui.progressBar.setMaximum(10)
    ui.progressBar.setMinimum(0)
    ui.progressBar.setValue(0)
    raporProgressWindow.show()

    # update_progress fonksiyonu QTimer kullanılmadan çağrılıyor
    update_progress(ui)

    sys.exit(app.exec())
