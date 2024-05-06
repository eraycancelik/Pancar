import os, webbrowser
import asyncio
import time

from PyQt6 import QtWidgets, QtCore
import matplotlib.pyplot as plt
from fpdf import FPDF


from .package.ui import mainWindow, engine, env, vehicle, gearbox, rapor, report_progress
from .package.speed_torque import Speed_Torque
from .database import Engine_db, Environment_db,Gearbox_db,Vehicle_db
from .utils import is_numeric,is_valid
from .package.pancar_class import OutGraps
from .report.report import rpm_v_graph, torque_rpm_graph, plot_torque_rpm_hp_graph, cs_final_tractive_force_vs_vehicle_speed, only_tractive_effort_vs_vehicle_speed
from .package.calculations import overall_resist_forces, cs_overall_resist_forces, tractive_f, final_force


class Pancar(QtWidgets.QMainWindow):
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

        selected_engine=self.engine_tork_speed_list.currentItem().text()
        selected_gearbox=self.gearbox_list.currentItem().text()
        selected_environment=self.environment_list.currentItem().text()
        selected_vehicle=self.vehicle_list.currentItem().text()
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
            self.get_current_status().rpm_v_graph()
            print("******************************************---------------------------------")
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

    def onTorque_enginev(self):
        try:
            self.get_current_status().torque_rpm_graph()
            
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
        
        
        
    def progress_ui(self):
        self.raporProgressWindow = QtWidgets.QDialog()
        self.ui = report_progress.Ui_Dialog()
        self.ui.setupUi(self.raporProgressWindow)
        self.raporProgressWindow.setModal(True)
        self.raporProgressWindow.show()
    

    def func_rpm_v_graph(self):
        rpm_v_graph(liste=self.get_current_status().arac_v_list(),rpm=self.get_current_status().motor_hiz)
    
    def func_torque_rpm_graph(self):
        torque_rpm_graph(rpm=self.get_current_status().motor_hiz,torque=self.get_current_status().motor_tork)
    
    def func_plot_torque_rpm_hp_graph(self):
        plot_torque_rpm_hp_graph(rpm=self.get_current_status().motor_hiz,torque=self.get_current_status().motor_tork)
    
    def func_cs_final_tractive_force_vs_vehicle_speed(self):
        cs_final_tractive_force_vs_vehicle_speed(f_list=final_force(resist_f=self.get_current_status().cs_resist_forces(),tractive_f=tractive_f(tork_list=self.get_current_status().tork_times_gear_list(),r_w=self.get_current_status().tekerlek_yaricap,t_efficiency=self.get_current_status().ao_verimi)),hiz_list=self.get_current_status().arac_v_list())
    
    def func_only_tractive_effort_vs_vehicle_speed(self):
        only_tractive_effort_vs_vehicle_speed(tractive_f_list=tractive_f(tork_list=self.get_current_status().tork_times_gear_list(),r_w=self.get_current_status().tekerlek_yaricap,t_efficiency=self.get_current_status().ao_verimi,),hiz_list=self.get_current_status().arac_v_list())
            
    
    def message(self):
        msg=QtWidgets.QMessageBox.information(
            self,
            "Başarılı",
            "Performans Raporunuz Başarıyla Oluşturulmuştur.",
            QtWidgets.QMessageBox.StandardButton.Ok
        )
        if msg==QtWidgets.QMessageBox.StandardButton.Ok:
            return
        
    def pdf_report(self,isim):
        try:
            WIDTH = 210
            HEIGHT = 297
            pdf = FPDF() # A4 (210 by 297 mm)
            pdf.add_page()
            print(os.getcwd())
            pdf.image("./App/icons/panco_yildizli.png", 0, 0, WIDTH)
            pdf.set_font('Arial', '', 24)

            pdf.image("./App/report/rpm_v_graph.png", x=8, y=140, w=95)
            print("buraya kadar sorunsuz geldik")
            pdf.image("./App/report/only_tractive_effort_vs_vehicle_speed.png",x=55, y=60, w=95)
            print("buraya kadar sorunsuz geldik")
            pdf.image("./App/report/torque_rpm_graph.png", x=8, y=215, w=95)
            print("buraya kadar sorunsuz geldik")
            pdf.image("./App/report/plot_torque_rpm_hp_graph.png", x=105, y=140, w=95)
            print("buraya kadar sorunsuz geldik")
            pdf.image("./App/report/cs_final_tractive_force_vs_vehicle_speed.png", x=107, y=215, w=95)
            print("buraya kadar sorunsuz geldik")
            pdf.output(f"{isim}.pdf")

        except:
            print("ne oldu ki")
            msg=QtWidgets.QMessageBox.warning(
                self,
                "Başarısız",
                "Performans raporunuz oluşturulurken bir hata oluştu.",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            if msg==QtWidgets.QMessageBox.StandardButton.Ok:
                return
        else:
            pass

    def create_analytics_report(self):
        self.raporProgressWindow = QtWidgets.QDialog()
        self.ui = report_progress.Ui_Dialog()
        self.ui.setupUi(self.raporProgressWindow)
        self.raporProgressWindow.setModal(True)

        isim=self.report_location("Performans Raporu")
        self.progress_ui()
        self.raporProgressWindow.show()
        self.func_rpm_v_graph()
        self.func_torque_rpm_graph()
        self.func_plot_torque_rpm_hp_graph()
        self.func_cs_final_tractive_force_vs_vehicle_speed()
        self.func_only_tractive_effort_vs_vehicle_speed()
        self.pdf_report(isim)
        self.raporProgressWindow.close()
        self.message()
    def report_location(self, file_name):
        fname, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            "Save File",
            file_name,
            "Files (.pdf)"
        )   
        if fname and fname != "":
            return fname
        else:
            print("File selection canceled")
            return None


    
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
        current_item = self.engine_tork_speed_list.currentItem()
        query=Engine_db()
        if current_item is not None:
            query.delete_engine(engine=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_engine_list()

    def delete_gearbox(self):
        current_item = self.gearbox_list.currentItem()
        query=Gearbox_db()
        if current_item is not None:
            query.delete_gearbox(gearbox=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_gearbox_list()
        
    def delete_environment(self):
        current_item = self.environment_list.currentItem()
        query=Environment_db()
        if current_item is not None:
            query.delete_environment(environment=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_environment_list()
        
    def delete_vehicle(self):
        current_item = self.vehicle_list.currentItem()
        query=Vehicle_db()
        if current_item is not None:
            query.delete_vehicle(vehicle=current_item.text())
            print(f"{current_item.text()} is deleted")
        else:
            print("Herhangi bir öğe seçilmedi.")
        self.update_vehicle_list()

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
            self.raporWindow.close()
            self.create_analytics_report()
            print("deneme tıklandı")

        except :
            print("something went wrong !!!")
        
        
    def file(self):
        file_filter="Excel File (*.xlsx *.xls);"
        response=QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption="Motor hız-tork tablosu",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter="Excel File (*.xlsx *.xls)"
        )
        path=str(response[0])
        self.ui.label_3.setText(path)
        self.path=path
        if self.path!="":
            self.pushButton.setEnabled(True)
    
    def onEngineClicked(self):
        dosya_yolu=self.path
        engine=Speed_Torque(file=dosya_yolu)
        speed=engine.out()[0]
        torque=engine.out()[1]
        speed_string=' '.join(str(e) for e in speed)
        torque_string=' '.join(str(e) for e in torque)
        motor_ismi=self.ui.motor_isim.text()
        if not motor_ismi or not speed_string or not torque_string:
            QtWidgets.QMessageBox.warning(
                self,
                "Hata",
                "Tüm alanları doldurunuz!",
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            
        else:
            engine_instance=Engine_db(
                engine_name=motor_ismi,
                speed=speed_string,
                torque=torque_string
            )
            engine_instance.create_engine()
            self.engineWindow.close()
            self.update_engine_list()
            print(speed_string,torque_string,motor_ismi)
            
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