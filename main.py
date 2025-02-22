# Bismillahirrahmanirrahim
from PyQt6 import QtWidgets
from App.pancar import Pancar

def initialize_lists(window):
    """Initialize all lists in the main window"""
    try:
        window.update_gearbox_list()
        window.update_environment_list()
        window.update_vehicle_list()
        window.update_engine_list()
    except Exception as e:
        QtWidgets.QMessageBox.critical(
            window,
            "Başlatma Hatası",
            f"Listeler yüklenirken hata oluştu: {str(e)}"
        )

if __name__ == "__main__":
    import sys
    try:
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Fusion")
        
        ana_pencere = Pancar()
        ana_pencere.show()
        
        initialize_lists(ana_pencere)
        
        sys.exit(app.exec())
    except Exception as e:
        print(f"Uygulama başlatılırken hata oluştu: {str(e)}")
        sys.exit(1)