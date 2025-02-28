from PyQt6 import QtWidgets, QtGui
from .package.ui import mainWindow, engine, env, vehicle, gearbox, rapor
from .package.speed_torque import Speed_Torque
from .database import Engine_db, Environment_db,Gearbox_db,Vehicle_db
from .utils import is_numeric,is_valid
from .package.pancar_class import OutGraps
from fpdf import FPDF
import matplotlib.pyplot as plt
import os, webbrowser
from .report.report import rpm_v_graph, torque_rpm_graph, plot_torque_rpm_hp_graph, cs_final_tractive_force_vs_vehicle_speed, only_tractive_effort_vs_vehicle_speed
from .package.calculations import overall_resist_forces, cs_overall_resist_forces, tractive_f, final_force
from multiprocessing import Process
from PyQt6.QtWidgets import QProgressDialog
from PyQt6.QtCore import Qt, QTimer
from datetime import datetime

class Pancar(QtWidgets.QMainWindow):
    DEFAULT_DIR = "/home/qt_user/Documents"
    PDF_WIDTH = 210
    PDF_HEIGHT = 297
    def __init__(self,path=""):
        super().__init__()
        self.path=path
        self.ui = mainWindow.Ui_VehicleDynamicsApp()
        self.ui.setupUi(self)
        self.URL="www.pancartech.com"
        self.engine_tork_speed_list=self.ui.engine_torque_speed_list
        self.gearbox_list=self.ui.gearbox_list
        self.vehicle_list=self.ui.vehicle_list
        self.environment_list=self.ui.environment_list

        # İkonu bir kez yükle
        self.window_icon = QtGui.QIcon("./Pancar.ico")
        
        # MenuBar stilini ayarla
        menubar_style = """
            QMenuBar {
                min-height: 10px;
                background-color: rgb(28,28,28);
            }
            QMenuBar::item {
                padding: 8px 12px;
                margin: 2px;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: rgb(45,45,45);
                border-radius: 4px;
            }
            QMenu {
                background-color: rgb(28,28,28);
                color: white;
                padding: 5px;
            }
            QMenu::item {
                padding: 6px 25px 6px 20px;
                border-radius: 3px;
            }
            QMenu::item:selected {
                background-color: rgb(45,45,45);
            }
        """
        self.ui.menubar.setStyleSheet(menubar_style)
        
    ################################################################### SIGNALS ###################################################################
        self.ui.vehicle_entry.triggered.connect(self.openVehicle)
        self.ui.actionProgram_Kaynaklar.triggered.connect(self.openWebSite)
        self.ui.actionDosyaya_Aktar.triggered.connect(self.openRapor)
        self.ui.environment_entry.triggered.connect(self.openEnv)
        self.ui.gearbox_entry.triggered.connect(self.openGearbox)
        self.ui.engine_entry.triggered.connect(self.openEngine)
        self.ui.gearbox_list_delete_button.clicked.connect(self.delete_gearbox)
        self.ui.env_list_delete_button.clicked.connect(self.delete_environment)
        self.ui.vehicle_list_delete_button.clicked.connect(self.delete_vehicle)
        self.ui.ets_list_delete_button.clicked.connect(self.delete_engine)
                    ############# grafikler ##############
        self.ui.enginev_vehiclev.clicked.connect(self.onEnginev_vehiclev)
        self.ui.torque_enginev.clicked.connect(self.onTorque_enginev)
        self.ui.torque_enginev_power.clicked.connect(self.onTorque_enginev_power)
        self.ui.tractiveF_vehiclev.clicked.connect(self.onTractiveF_vehiclev)
        self.ui.tractiveFnet_vehiclev.clicked.connect(self.onTractiveFnet_vehiclev)
    
    ###############################################################################################################################################
    
    def get_current_status(self):
        try:
            selected_engine = self.engine_tork_speed_list.currentItem().text()
            selected_gearbox = self.gearbox_list.currentItem().text()
            selected_environment = self.environment_list.currentItem().text()
            selected_vehicle = self.vehicle_list.currentItem().text()
        except AttributeError:
            raise ValueError("Lütfen tüm listelerde seçim yapınız")
        
        engine_instance=Engine_db()
        environment_instance=Environment_db()
        vehicle_instance=Vehicle_db()
        gearbox_instance=Gearbox_db()

        arac_ismi=vehicle_instance.get_specific_vehicle(selected_vehicle).vehicle_name
        sanziman_ismi=gearbox_instance.get_specific_gearbox(selected_gearbox).gearbox_name
        motor_ismi=engine_instance.get_specific_engine(selected_engine).engine_name
        cevre_ismi=environment_instance.get_specific_environment(selected_environment).environment_name
        
        gearBox_str=(gearbox_instance.get_specific_gearbox(selected_gearbox).gear_ratio_list).split()
        motor_hiz_str=(engine_instance.get_specific_engine(selected_engine).speed).split()
        motor_tork_str=(engine_instance.get_specific_engine(selected_engine).torque).split()
        
        gearBox=[float(x) for x in gearBox_str]
        oran_diferansiyel=float(gearbox_instance.get_specific_gearbox(selected_gearbox).differential_gear_ratio)
        tekerlek_yaricap=float(vehicle_instance.get_specific_vehicle(selected_vehicle).r_dynamic_rolling)
        ao_verimi=float(gearbox_instance.get_specific_gearbox(selected_gearbox).powertrain_efficiency)
        motor_hiz=[float(x) for x in motor_hiz_str]
        motor_tork=[float(x) for x in motor_tork_str]
        yuvarlanma_katsiyi=float(vehicle_instance.get_specific_vehicle(selected_vehicle).rolling_resistance)
        arac_kutlesi=float(vehicle_instance.get_specific_vehicle(selected_vehicle).vehicle_mass)
        yol_egimi=float(environment_instance.get_specific_environment(selected_environment).slope_angel_road)
        ro_hava_yogunlugu=float(environment_instance.get_specific_environment(selected_environment).air_density)
        af_arac_izdusum_alanı=float(vehicle_instance.get_specific_vehicle(selected_vehicle).af_projection_area)
        cd_aerodinamik_direnc_katsayisi=float(vehicle_instance.get_specific_vehicle(selected_vehicle).c_aero)
        v_ruzgar=float(environment_instance.get_specific_environment(selected_environment).wind_speed)
        cekim_ivmesi=float(environment_instance.get_specific_environment(selected_environment).gravitational_force)
        instance=OutGraps(
            arac_ismi=arac_ismi,
            sanziman_ismi=sanziman_ismi,
            motor_ismi=motor_ismi,
            cevre_ismi=cevre_ismi,
            
            gearBox = gearBox,
            oran_diferansiyel = oran_diferansiyel,
            tekerlek_yaricap = tekerlek_yaricap,
            ao_verimi = ao_verimi,
            motor_tork=motor_tork, #
            motor_hiz=motor_hiz, #
            yuvarlanma_katsiyi = yuvarlanma_katsiyi,
            arac_kutlesi = arac_kutlesi,
            yol_egimi = yol_egimi,
            ro_hava_yogunlugu = ro_hava_yogunlugu,
            af_arac_izdusum_alanı = af_arac_izdusum_alanı,
            cd_aerodinamik_direnc_katsayisi = cd_aerodinamik_direnc_katsayisi,
            v_ruzgar = v_ruzgar,
            cekim_ivmesi = cekim_ivmesi
        )
        # print("###################################################################################################")
        # print(instance.motor_tork)
        # print(len(instance.tork_times_gear_list()))
        # print(instance.tork_times_gear_list()[0])
        return instance
    



    #################################################################### SLOTS ####################################################################
    def onEnginev_vehiclev(self):
        try:
            # Grafiği oluştur
            plt.figure()
            self.get_current_status().rpm_v_graph()
            
            # Grafik penceresini Qt widget'ına dönüştür
            fig_manager = plt.get_current_fig_manager()
            fig_manager.window.setWindowFlags(
                Qt.WindowType.WindowStaysOnTopHint |  # Her zaman üstte
                Qt.WindowType.Window                   # Normal pencere özellikleri
            )
            fig_manager.window.setWindowModality(Qt.WindowModality.ApplicationModal)  # Ana pencereyi kilitle
            plt.show()
            
        except Exception as e:
            print("Hata", e)
            msg = QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Bütün tablolardan seçim yapmadan grafik oluşturamazsınız!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def onTorque_enginev(self):
        try:
            plt.figure()
            self.get_current_status().torque_rpm_graph()
            
            fig_manager = plt.get_current_fig_manager()
            fig_manager.window.setWindowFlags(
                Qt.WindowType.WindowStaysOnTopHint |
                Qt.WindowType.Window
            )
            fig_manager.window.setWindowModality(Qt.WindowModality.ApplicationModal)
            plt.show()
            
        except Exception as e:
            print("Hata", e)
            msg = QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Bütün tablolardan seçim yapmadan grafik oluşturamazsınız!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def onTorque_enginev_power(self):
        try:
            self.get_current_status().torque_rpm_power_graph()
        except Exception as e:
            print("Hata",e)
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Bütün tablolardan seçim yapmadan grafik oluşturamazsınız!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
    
    def onTractiveF_vehiclev(self):
        try:
            self.get_current_status().only_tractive_effort_vs_vehicle_speed()
        except Exception as e:
            print("Hata",e)
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Bütün tablolardan seçim yapmadan grafik oluşturamazsınız!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
    
    def onTractiveFnet_vehiclev(self):
        try:
            self.get_current_status().cs_final_tractive_force_vs_vehicle_speed()
        except Exception as e:
            print("Hata",e)
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Bütün tablolardan seçim yapmadan grafik oluşturamazsınız!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
        
        
        
        
    
    def create_analytics_report(self):
        try:
            isim = self.report_location("Rapor")
            if not isim:  # Kullanıcı iptal ettiyse
                return
                
            # Progress dialog oluştur
            self.progress = QProgressDialog("Rapor hazırlanıyor...", "İptal", 0, 100, self)
            self.progress.setWindowModality(Qt.WindowModality.WindowModal)
            self.progress.setWindowTitle("Lütfen Bekleyin")
            self.progress.setAutoClose(True)
            self.progress.setCancelButton(None)  # İptal butonunu kaldır
            self.progress.setMinimumDuration(0)  # Hemen göster
            self.progress.show()
            
            def update_progress(value):
                self.progress.setValue(value)
                QtWidgets.QApplication.processEvents()  # UI'ı güncelle
            
            update_progress(10)
            
            # PDF oluşturma
            pdf = FPDF()
            pdf.add_font('DejaVuBold', '', './App/fonts/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf', uni=True)
            pdf.add_font('DejaVu', '', './App/fonts/dejavu-fonts-ttf-2.37/ttf/DejaVuSansCondensed.ttf', uni=True)
            # İlk sayfa - bilgi alanı, tablo ve başlık
            pdf.add_page()
            pdf.image("./App/icons/rapor_sayfa1.png", 0, 0, self.PDF_WIDTH)
            
            # Tarih
            pdf.set_font('DejaVu', '', 12)
            pdf.set_xy(150, 18)
            current_date = datetime.now().strftime("%d.%m.%Y")
            pdf.cell(30, 10, current_date, 0, 0, 'R')

            # Ana başlık
            pdf.set_font('DejaVu', '', 14)
            pdf.set_y(45)  # 30'dan 65'e çıkarıldı (35mm aşağı)
            pdf.cell(0, 10, 'Araç Bilgileri ve Belirlenen Ortamdaki Performans Değerleri', 0, 1, 'C')
            
            # Bilgi alanı
            pdf.set_font('DejaVuBold', '', 11)
            pdf.set_y(pdf.get_y() + 5)  # Başlıktan sonra 5mm boşluk
            
            # Seçilen değerleri al
            selected_vehicle = self.get_current_status().arac_ismi
            selected_engine = self.get_current_status().motor_ismi
            selected_gearbox = self.get_current_status().sanziman_ismi
            selected_environment = self.get_current_status().cevre_ismi
            
            # Bilgileri yerleştir
            info_x = 60
            info_spacing = 8
            
            for label, value in [
                ('Araç:', selected_vehicle),
                ('Motor:', selected_engine),
                ('Şanzıman:', selected_gearbox),
                ('Ortam:', selected_environment)
            ]:
                pdf.set_x(info_x)
                pdf.set_font('DejaVuBold', '', 11)  # Etiketler için kalın font
                pdf.cell(40, info_spacing, label, 0, 0)
                pdf.set_font('DejaVu', '', 11)      # Değerler için normal font
                pdf.cell(100, info_spacing, value, 0, 1)

            update_progress(20)
            
            # Tablo başlığı
            pdf.set_font('DejaVu', '', 13)
            pdf.set_y(pdf.get_y() + 20)  # Bilgi alanından sonra 20mm boşluk
            pdf.cell(0, 10, 'Aracın Belirlenen Ortamdaki En Yüksek Hızları Ve Çekiş Gücü Değerleri', 0, 1, 'C')
            pdf.set_y(pdf.get_y() + 5)  # Tablo başlığından sonra 5mm boşluk

            # Tablo başlıkları ve verileri
            pdf.set_font('DejaVuBold', '', 9)
            col_width = 40
            row_height = 9
            left_margin = (self.PDF_WIDTH - (col_width * 4)) / 2
            pdf.set_left_margin(left_margin)
            
            # Tablo başlıkları
            headers = ['Vites', 'Max. Hız (km/h)', 'Çekiş Kuvveti (N)', 'Net Çekiş Kuvveti (N)']
            for header in headers:
                pdf.cell(col_width, row_height, header, 1, 0, 'C')
            pdf.ln()
            
            # Tablo verileri
            pdf.set_font('Arial', '', 10)
            hiz_list = self.get_current_status().arac_v_list()
            tractive_forces = tractive_f(
                tork_list=self.get_current_status().tork_times_gear_list(),
                r_w=self.get_current_status().tekerlek_yaricap,
                t_efficiency=self.get_current_status().ao_verimi)
            net_forces = final_force(
                resist_f=self.get_current_status().cs_resist_forces(),
                tractive_f=tractive_forces)
            
            # Her vites için maksimum değerleri bul ve tabloya ekle
            for gear_num in range(len(hiz_list)):
                max_speed = max(hiz_list[gear_num])
                max_force_idx = tractive_forces[gear_num].index(max(tractive_forces[gear_num]))
                max_force = tractive_forces[gear_num][max_force_idx]
                net_force = net_forces[gear_num][max_force_idx]
                
                pdf.cell(col_width, row_height, f'{gear_num + 1}. Vites', 1, 0, 'C')
                pdf.cell(col_width, row_height, f'{max_speed:.2f}', 1, 0, 'C')
                pdf.cell(col_width, row_height, f'{max_force:.2f}', 1, 0, 'C')
                pdf.cell(col_width, row_height, f'{net_force:.2f}', 1, 1, 'C')
            update_progress(30)
            # İkinci sayfa - diğer grafikler
            pdf.add_page()
            pdf.image("./App/icons/rapor_sayfa2.png", 0, 0, self.PDF_WIDTH)
            pdf.set_font('DejaVu', '', 12)
            pdf.set_xy(150, 18)
            pdf.cell(30, 10, current_date, 0, 0, 'R')
            update_progress(45)

            # Önce tüm grafikleri oluştur
            cs_final_tractive_force_vs_vehicle_speed(
                f_list=final_force(
                    resist_f=self.get_current_status().cs_resist_forces(),
                    tractive_f=tractive_f(
                        tork_list=self.get_current_status().tork_times_gear_list(),
                        r_w=self.get_current_status().tekerlek_yaricap,
                        t_efficiency=self.get_current_status().ao_verimi)),
                hiz_list=self.get_current_status().arac_v_list())
            
            rpm_v_graph(liste=self.get_current_status().arac_v_list(),
                       rpm=self.get_current_status().motor_hiz)
            
            torque_rpm_graph(rpm=self.get_current_status().motor_hiz,
                           torque=self.get_current_status().motor_tork)
            
            plot_torque_rpm_hp_graph(rpm=self.get_current_status().motor_hiz,
                                   torque=self.get_current_status().motor_tork)
            
            only_tractive_effort_vs_vehicle_speed(
                tractive_f_list=tractive_f(
                    tork_list=self.get_current_status().tork_times_gear_list(),
                    r_w=self.get_current_status().tekerlek_yaricap,
                    t_efficiency=self.get_current_status().ao_verimi),
                hiz_list=self.get_current_status().arac_v_list())
            
            update_progress(55)
            
            # Grafikleri düzenle
            graph_width = 85  # Grafik genişliği biraz küçültüldü
            graph_height = 85  # Grafik yüksekliği biraz küçültüldü
            
            # Üstteki grafik için merkezi konumlandırma
            x_center = (self.PDF_WIDTH - graph_width) / 2
            y_top = 35  # Üst grafik biraz yukarı alındı
            
            # Alt grafiklerin yerleşimi için
            x_margin = (self.PDF_WIDTH - (2 * graph_width)) / 3  # Yatay kenar boşluğu
            y_start = y_top + graph_height  # Üst grafikle alt grafikler arası mesafe azaltıldı
             # Alt grafik sıraları arası boşluk eklendi

            # Üstteki merkezi grafik
            pdf.image("./App/report/plot_torque_rpm_hp_graph.png", 
                     x=x_center, 
                     y=y_top, 
                     w=graph_width)
            update_progress(60)

            # Alt sıra ilk iki grafik
            pdf.image("./App/report/rpm_v_graph.png", 
                     x=x_margin, 
                     y=y_start, 
                     w=graph_width)
            update_progress(70)
            
            pdf.image("./App/report/torque_rpm_graph.png", 
                     x=x_margin*2 + graph_width, 
                     y=y_start, 
                     w=graph_width)
            update_progress(80)

            # En alt sıra iki grafik
            pdf.image("./App/report/cs_final_tractive_force_vs_vehicle_speed.png", 
                     x=x_margin, 
                     y=y_start + graph_height, 
                     w=graph_width)
            update_progress(85)
            
            pdf.image("./App/report/only_tractive_effort_vs_vehicle_speed.png", 
                     x=x_margin*2 + graph_width, 
                     y=y_start + graph_height, 
                     w=graph_width)
            update_progress(90)
            
            # PDF'i kaydet
            pdf.output(f"{isim}.pdf")
            update_progress(100)
            
            # Başarı mesajı göster
            self.show_success_message("Başarılı", "Rapor başarıyla oluşturuldu!")
            
            # Geçici dosyaları temizle
            self.cleanup_temp_files()
            
        except Exception as e:
            self.show_error_message("Hata", f"Rapor oluşturulurken bir hata oluştu: {str(e)}")
            return

    def report_location(self, file_name):
        default_dir = self.DEFAULT_DIR
        default_filename = os.path.join(default_dir, file_name)
        fname, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save File",
            default_filename,
            "Files (.pdf)"
        )
        if fname:
            print(fname)
        return fname

    def show_error_message(self, title, message):
        """Genel hata mesajı gösterme fonksiyonu"""
        msg = QtWidgets.QMessageBox.warning(
            self,
            title,
            message,
            QtWidgets.QMessageBox.StandardButton.Ok
        )
        return msg

    def show_success_message(self, title, message):
        """Genel başarı mesajı gösterme fonksiyonu"""
        msg = QtWidgets.QMessageBox.information(
            self,
            title,
            message,
            QtWidgets.QMessageBox.StandardButton.Ok
        )
        return msg

    ##### LISTE ISLEMLERI #####
    def update_gearbox_list(self):
        gearbox_db = Gearbox_db()
        query_result = gearbox_db.get_gearboxes()
        self.gearbox_list.clear()
        if query_result:
            for gearbox in query_result:
                item_text = gearbox.gearbox_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.gearbox_list.addItem(list_item)
        else:
            self.gearbox_list.addItem("Şanzıman kaydı bulunamadı.")
            
    def update_environment_list(self):
        environments_db=Environment_db()
        query_result = environments_db.get_environments()
        self.environment_list.clear()
        if query_result:
            for item in query_result:
                item_text = item.environment_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.environment_list.addItem(list_item)
        else:
            self.environment_list.addItem("Ortam kaydı bulunamadı.")

    def update_vehicle_list(self):
        vehicle_db=Vehicle_db()
        query_result = vehicle_db.get_vehicles()
        self.vehicle_list.clear()
        if query_result:
            for item in query_result:
                item_text = item.vehicle_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.vehicle_list.addItem(list_item)
        else:
            self.vehicle_list.addItem("Ortam kaydı bulunamadı.")
    
    def update_engine_list(self):
        engine_db=Engine_db()
        query_result = engine_db.get_engines()
        self.engine_tork_speed_list.clear()
        if query_result:
            for item in query_result:
                item_text = item.engine_name
                list_item = QtWidgets.QListWidgetItem(item_text)
                self.engine_tork_speed_list.addItem(list_item)
        else:
            self.engine_tork_speed_list.addItem("Ortam kaydı bulunamadı.")
            
    def delete_engine(self):
        try:
            selected_engine = self.engine_tork_speed_list.currentItem().text()
            
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Silme Onayı")
            msg.setText(f'{selected_engine} motorunu silmek istediğinizden emin misiniz?')
            msg.setWindowIcon(self.window_icon)
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)  # Soru işareti ikonu ekle
            
            sil_button = msg.addButton('Sil', QtWidgets.QMessageBox.ButtonRole.YesRole)
            iptal_button = msg.addButton('İptal', QtWidgets.QMessageBox.ButtonRole.NoRole)
            msg.setDefaultButton(iptal_button)
            
            msg.exec()
            
            if msg.clickedButton() == sil_button:
                engine_instance = Engine_db()
                engine_instance.delete_engine(selected_engine)
                self.update_engine_list()
                
                QtWidgets.QMessageBox.information(
                    self,
                    "Başarılı",
                    f"{selected_engine} motoru başarıyla silinmiştir",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
        except:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Lütfen silmek istediğiniz motoru seçiniz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def delete_gearbox(self):
        try:
            selected_gearbox = self.gearbox_list.currentItem().text()
            
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Silme Onayı")
            msg.setText(f'{selected_gearbox} şanzımanını silmek istediğinizden emin misiniz?')
            msg.setWindowIcon(self.window_icon)
            msg.setIcon(QtWidgets.QMessageBox.Icon.Question)  # Soru işareti ikonu ekle
            
            sil_button = msg.addButton('Sil', QtWidgets.QMessageBox.ButtonRole.YesRole)
            iptal_button = msg.addButton('İptal', QtWidgets.QMessageBox.ButtonRole.NoRole)
            msg.setDefaultButton(iptal_button)
            
            msg.exec()
            
            if msg.clickedButton() == sil_button:
                gearbox_instance = Gearbox_db()
                gearbox_instance.delete_gearbox(selected_gearbox)
                self.update_gearbox_list()
                
                QtWidgets.QMessageBox.information(
                    self,
                    "Başarılı",
                    f"{selected_gearbox} şanzımanı başarıyla silinmiştir",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
        except:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Lütfen silmek istediğiniz şanzımanı seçiniz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def delete_environment(self):
        try:
            selected_environment = self.environment_list.currentItem().text()
            
            reply = QtWidgets.QMessageBox.question(
                self,
                'Silme Onayı',
                f'{selected_environment} ortamını silmek istediğinizden emin misiniz?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )
            
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                environment_instance = Environment_db()
                environment_instance.delete_environment(selected_environment)
                self.update_environment_list()
                
                QtWidgets.QMessageBox.information(
                    self,
                    "Başarılı",
                    f"{selected_environment} ortamı başarıyla silinmiştir",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
        except:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Lütfen silmek istediğiniz ortamı seçiniz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def delete_vehicle(self):
        try:
            selected_vehicle = self.vehicle_list.currentItem().text()
            
            reply = QtWidgets.QMessageBox.question(
                self,
                'Silme Onayı',
                f'{selected_vehicle} aracını silmek istediğinizden emin misiniz?',
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )
            
            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                vehicle_instance = Vehicle_db()
                vehicle_instance.delete_vehicle(selected_vehicle)
                self.update_vehicle_list()
                
                QtWidgets.QMessageBox.information(
                    self,
                    "Başarılı",
                    f"{selected_vehicle} aracı başarıyla silinmiştir",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
        except:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Lütfen silmek istediğiniz aracı seçiniz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def openEngine(self):
        self.engineWindow=QtWidgets.QDialog()
        self.ui=engine.Ui_Dialog()
        self.ui.setupUi(self.engineWindow)
        self.engineWindow.setModal(True)
        self.engineWindow.show()
        print("engine done")
        self.pushButton = self.engineWindow.findChild(QtWidgets.QPushButton, "kaydet")
        self.secPushButton = self.engineWindow.findChild(QtWidgets.QPushButton, "sec")
        self.secPushButton.clicked.connect(self.file)
        if self.path=="":
            self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.onEngineClicked)
        print("engine clicked")
    
        
    def openGearbox(self):
        self.gearboxWindow=QtWidgets.QDialog()
        self.ui=gearbox.Ui_Sanziman()
        self.ui.setupUi(self.gearboxWindow)
        self.gearboxWindow.setModal(True)
        self.gearboxWindow.show()
        print("gearbox done")
        self.pushButton = self.gearboxWindow.findChild(QtWidgets.QPushButton, "sanziman_kaydet")
        self.pushButton.clicked.connect(self.onGearClicked)


    def openVehicle(self):
        self.vehicleWindow=QtWidgets.QDialog()
        self.ui=vehicle.Ui_Dialog()
        self.ui.setupUi(self.vehicleWindow)
        self.vehicleWindow.setModal(True)
        self.vehicleWindow.show()
        print("vehicle done")
        self.pushButton = self.vehicleWindow.findChild(QtWidgets.QPushButton, "arac_kaydet")
        self.pushButton.clicked.connect(self.onVehicleClicked)


    def openEnv(self):
        self.envWindow=QtWidgets.QDialog()
        self.ui=env.Ui_Cevre()
        self.ui.setupUi(self.envWindow)
        self.envWindow.setModal(True)
        self.envWindow.show()
        print("environment done")
        self.pushButton = self.envWindow.findChild(QtWidgets.QPushButton, "ortam_kaydet")
        self.pushButton.clicked.connect(self.onEnvClicked)
    
    def openRapor(self):

        self.raporWindow=QtWidgets.QDialog()
        self.ui=rapor.Ui_Rapor()
        self.ui.setupUi(self.raporWindow)
        self.raporWindow.setModal(True)
        
        self.raporWindow.show()
        self.button=self.ui.rapor_olustur
        self.button.clicked.connect(self.onRaporClicked)
        
        

        try:
            motor_ismi=self.get_current_status().motor_ismi
            self.ui.motor.setText(motor_ismi)
            
            arac=self.get_current_status().arac_ismi
            self.ui.arac.setText(arac)
            
            sanziman_ismi=self.get_current_status().sanziman_ismi
            self.ui.sanziman.setText(sanziman_ismi)
            
            cevre_ismi=self.get_current_status().cevre_ismi    
            self.ui.cevre.setText(cevre_ismi)
            
            
        except :
            self.ui.motor.setText("-")
            self.ui.arac.setText("-")
            self.ui.sanziman.setText("-")
            self.ui.cevre.setText("-")
            #self.ui.kullanici.setText("-")
            #self.ui.arac_ismi.setText("-")
            
            
    def openWebSite(self):
            webbrowser.open(url=self.URL)
            
    def onRaporClicked(self):
        try:
            self.create_analytics_report()
            # Rapor başarıyla oluşturulduktan sonra rapor penceresini kapat
            self.raporWindow.close()
            print("Rapor başarıyla oluşturuldu")
            
        except Exception as e:
            print(f"Hata oluştu: {str(e)}")
        
        
    def file(self):
        file_filter = "CSV File (*.csv)"  # Düzeltilmiş filtre
        response = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Motor hız-tork tablosu",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter=file_filter  # initialFilter da CSV olarak değiştirildi
        )
        path = str(response[0])
        self.ui.label_3.setText(path)
        self.path = path
        
        # Dosya seçildiyse verileri oku
        if self.path:
            try:
                engine = Speed_Torque(file=self.path)
                self.speed_list = engine.out()[0]  # Hız listesi
                self.torque_list = engine.out()[1]  # Tork listesi
                self.pushButton.setEnabled(True)
            except Exception as e:
                print(f"Dosya okuma hatası: {str(e)}")
                self.pushButton.setEnabled(False)

    def onEngineClicked(self):
        try:
            motor_ismi = self.ui.motor_isim.text()
            
            if not hasattr(self, 'speed_list') or not hasattr(self, 'torque_list'):
                QtWidgets.QMessageBox.warning(
                    self,
                    "Hata",
                    "Lütfen önce motor verilerini yükleyin!",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
                return
            
            speed_string = ' '.join(str(e) for e in self.speed_list)
            torque_string = ' '.join(str(e) for e in self.torque_list)
            
            if not motor_ismi or not speed_string or not torque_string:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Hata",
                    "Tüm alanları doldurunuz!",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
            else:
                engine_instance = Engine_db(
                    engine_name=motor_ismi,
                    speed=speed_string,
                    torque=torque_string
                )
                engine_instance.create_engine()
                self.engineWindow.close()
                self.update_engine_list()
                
                # Başarı mesajı göster
                msg = QtWidgets.QMessageBox.information(
                    self,
                    "Başarılı",
                    f"{motor_ismi} motoru başarıyla kaydedilmiştir",
                    QtWidgets.QMessageBox.StandardButton.Ok
                )
        except Exception as e:
            print(f"Motor ekleme hatası: {str(e)}")
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Motor eklenirken bir hata oluştu!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )

    def onGearClicked(self):
        sanziman_ismi = self.ui.sanziman_ismi.text()
        vites_oranlari = self.ui.vites_oranlari.text()
        dif_oran = self.ui.dif_oran.text()
        ao_verimi = self.ui.ao_verimi.text()

        if not sanziman_ismi or not vites_oranlari or not dif_oran or not ao_verimi:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        elif is_valid(vites_oranlari) and is_numeric(dif_oran) and is_numeric(ao_verimi):
            gearbox_instance = Gearbox_db(
                gearbox_name=sanziman_ismi,
                gear_ratio_list=vites_oranlari,
                differential_gear_ratio=dif_oran,
                powertrain_efficiency=ao_verimi,
            )
            gearbox_instance.create_gearbox()
            self.gearboxWindow.close()
            self.update_gearbox_list()
            print("Şanzıman kaydedildi")  
            msg=QtWidgets.QMessageBox.information(
                self,
                "Başarılı",
                f"{sanziman_ismi} başarıyla kaydedilmiştir   ",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
            print("araç kaydettim")
        
        else:
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "İlgili alanları yalnızca sayısal değerlerle doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
                                  

    def onVehicleClicked(self):
        arac_ismi=self.ui.arac_ismi.text()
        arac_kutlesi=self.ui.arac_kutlesi.text()
        cf_aero=self.ui.cf_aero.text()
        izdusum_alan=self.ui.izdusum_alan.text()
        yuvarlanma_direnc=self.ui.yuvarlanma_direnc.text()
        teker_efektif_r=self.ui.teker_efektif_r.text()
        if  not arac_kutlesi or not cf_aero or not izdusum_alan or not yuvarlanma_direnc or not teker_efektif_r:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        elif is_numeric(arac_kutlesi) and is_numeric(cf_aero) and is_numeric(izdusum_alan) and is_numeric(yuvarlanma_direnc) and is_numeric(teker_efektif_r):
            vehicle_instance = Vehicle_db(
            vehicle_name=arac_ismi,
            vehicle_mass=arac_kutlesi,
            c_aero=cf_aero,
            af_projection_area=izdusum_alan,
            rolling_resistance=yuvarlanma_direnc,
            r_dynamic_rolling=teker_efektif_r,
        )
            vehicle_instance.create_vehicle()
            self.vehicleWindow.close()
            self.update_vehicle_list()
            msg=QtWidgets.QMessageBox.information(
                self,
                "Başarılı",
                f"{arac_ismi} aracı başarıyla kaydedilmiştir   ",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
            print("araç kaydettim")
        
        else:
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "İlgili alanları yalnızca sayısal değerlerle doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return

    def onEnvClicked(self):
        cevre_isim=self.ui.cevre_isim.text()
        ruzgar_hizi=self.ui.ruzgar_hizi.text()
        yol_egimi=self.ui.yol_egimi.text()
        hava_yogunlugu=self.ui.hava_yogunlugu.text()
        yercekimi=self.ui.yercekimi.text()
        if  not cevre_isim or not ruzgar_hizi or not yol_egimi or not hava_yogunlugu or not yercekimi:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
        elif is_numeric(ruzgar_hizi) and is_numeric(yol_egimi) and is_numeric(hava_yogunlugu) and is_numeric(yercekimi) :
            environment_instance = Environment_db(
            environment_name=cevre_isim,
            wind_speed=ruzgar_hizi,
            slope_angel_road=yol_egimi,
            air_density=hava_yogunlugu,
            gravitational_force=yercekimi,
        )
            environment_instance.create_environment()
            self.envWindow.close()
            self.update_environment_list()
            msg=QtWidgets.QMessageBox.information(
                self,
                "Başarılı",
                f"{cevre_isim} ortamı başarıyla kaydedilmiştir   ",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
            print("araç kaydettim")
        
        else:
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "İlgili alanları yalnızca sayısal değerlerle doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return

    def cleanup_temp_files(self):
        """Geçici grafik dosyalarını temizle"""
        temp_files = [
            "only_tractive_effort_vs_vehicle_speed.png",
            "cs_final_tractive_force_vs_vehicle_speed.png",
            "plot_torque_rpm_hp_graph.png",
            "rpm_v_graph.png",
            "torque_rpm_graph.png"
        ]
        
        for file in temp_files:
            try:
                if os.path.exists(f"./App/report/{file}"):
                    os.remove(f"./App/report/{file}")
            except Exception as e:
                print(f"Dosya silinirken hata: {str(e)}")

    def validate_numeric_inputs(self, **inputs):
        """Sayısal girişleri doğrula"""
        for name, value in inputs.items():
            if not value:
                raise ValueError(f"{name} alanı boş bırakılamaz")
            if not is_numeric(value):
                raise ValueError(f"{name} alanı sayısal olmalıdır")
        return True

    def validate_and_create_instance(self, instance_type, **kwargs):
        """Ortak validasyon ve instance oluşturma işlemleri"""
        if not all(kwargs.values()):
            self.show_error_message("Hata", "Tüm alanları doldurunuz!")
            return False
        # ... validasyon ve instance oluşturma
