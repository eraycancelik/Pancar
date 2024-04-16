# Bismillahirrahmanirrahim
from PyQt6 import QtWidgets

from App.pancar import Pancar
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    ana_pencere = Pancar()
    ana_pencere.show()
    ana_pencere.update_gearbox_list()
    ana_pencere.update_environment_list()
    ana_pencere.update_vehicle_list()
    ana_pencere.update_engine_list()
    sys.exit(app.exec())