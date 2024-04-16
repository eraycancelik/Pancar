from .engine import Motor
from .graphs import EngineDataGraph
from .calculations import overall_resist_forces, cs_overall_resist_forces, tractive_f, final_force, overall_gear_ratio


class OutGraps:
    def __init__(
        self,
        arac_ismi,
        sanziman_ismi,
        motor_ismi,
        cevre_ismi,
        # motor değerleri
        gearBox,
        oran_diferansiyel,
        tekerlek_yaricap,
        ao_verimi,
        v_ruzgar,  # metre/saniye
        motor_tork,
        motor_hiz,
        # yol dirençleri değerleri
        yuvarlanma_katsiyi,
        arac_kutlesi=1200,
        yol_egimi=0,
        # aerodinamik değerler
        ro_hava_yogunlugu=1.225,  # kg/metreküp
        af_arac_izdusum_alanı=1.85,  # metrekare
        cd_aerodinamik_direnc_katsayisi=0.5,
        cekim_ivmesi=9.81,
        
    ): 
        self.arac_ismi=arac_ismi
        self.sanziman_ismi=sanziman_ismi
        self.motor_ismi=motor_ismi
        self.cevre_ismi=cevre_ismi
        self.gearBox = gearBox
        self.oran_diferansiyel = oran_diferansiyel
        self.tekerlek_yaricap = tekerlek_yaricap
        self.ao_verimi = ao_verimi
        self.motor_tork=motor_tork
        self.motor_hiz=motor_hiz
        self.yuvarlanma_katsiyi = yuvarlanma_katsiyi
        self.arac_kutlesi = arac_kutlesi
        self.yol_egimi = yol_egimi
        self.ro_hava_yogunlugu = ro_hava_yogunlugu
        self.af_arac_izdusum_alanı = af_arac_izdusum_alanı
        self.cd_aerodinamik_direnc_katsayisi = cd_aerodinamik_direnc_katsayisi
        self.v_ruzgar = v_ruzgar
        self.cekim_ivmesi = cekim_ivmesi
        
        
        self.arac = Motor(
            gearBox=self.gearBox,
            oran_diferansiyel=self.oran_diferansiyel,
            tekerlek_yaricap=self.tekerlek_yaricap,
            ao_verimi=self.ao_verimi,
            arac_kutlesi=self.arac_kutlesi,
            yuvarlanma_katsiyi=self.yuvarlanma_katsiyi,
            ro_hava_yogunlugu=self.ro_hava_yogunlugu,
            v_ruzgar=self.v_ruzgar,
            af_arac_izdusum_alanı=self.af_arac_izdusum_alanı,
            cd_aerodinamik_direnc_katsayisi=self.cd_aerodinamik_direnc_katsayisi,
            yol_egimi=self.yol_egimi,
            )
        
    def tork_times_gear_list(self):
        tork_times_gear_list=self.arac.torque_rev_per_gear(
            tork_list=self.motor_tork,overall_gear_ratio=self.gearBox
        )
        return tork_times_gear_list
        
    def arac_v_list(self):
        arac_v_list=self.arac.velocity_rpm(rpm=self.motor_hiz,gear_box=self.gearBox)
        return arac_v_list
    
    
    def windy_v_list(self):
        windy_v_list=self.arac.windy_velocity_rpm(
            rpm=self.motor_hiz,gear_box=self.gearBox,ruzgar_hizi=self.v_ruzgar
        )
        return windy_v_list
    
    
    def resist_forces(self):
        resist_forces=overall_resist_forces(
            arac_kutlesi=self.arac.arac_kutlesi,
            cekim_ivmesi=self.arac.cekim_ivmesi,
            yuvarlanma_katsiyi=self.arac.yuvarlanma_katsiyi,
            yol_egimi=self.arac.yol_egimi,
            p_yogunluk=self.arac.ro_hava_yogunlugu,
            cw_aero=self.arac.cd_aerodinamik_direnc_katsayisi,
            Af_izdusum=self.arac.af_arac_izdusum_alanı,
            hiz_list=self.windy_v_list,
        )
        return resist_forces

    def cs_resist_forces(self):
        cs_resist_forces=cs_overall_resist_forces(
            arac_kutlesi=self.arac.arac_kutlesi,
            cekim_ivmesi=self.arac.cekim_ivmesi,
            yuvarlanma_katsiyi=self.arac.yuvarlanma_katsiyi,
            yol_egimi=self.arac.yol_egimi,
            p_yogunluk=self.arac.ro_hava_yogunlugu,
            cw_aero=self.arac.cd_aerodinamik_direnc_katsayisi,
            Af_izdusum=self.arac.af_arac_izdusum_alanı,
            hiz_list=self.arac_v_list(),
            ruzgar_hizi=self.arac.v_ruzgar,
        )
        print("///////////////////////////////////////////////////////////////////////")
        return cs_resist_forces
    
    def rpm_v_graph(self):
        graph_instance = EngineDataGraph(
            torque_main=self.motor_tork, rpm_main=self.motor_hiz,graph_title="rb 26 motoru"
        )
        graph_instance.rpm_v_graph( 
            liste=self.arac_v_list(),
            rpm=self.motor_hiz,
        )
           
    def torque_rpm_graph(self):
        graph_instance = EngineDataGraph(
            torque_main=self.motor_tork, rpm_main=self.motor_hiz,graph_title="rb 26 motoru"
        )
        graph_instance.torque_rpm_graph()
        
    def torque_rpm_power_graph(self):
        graph_instance = EngineDataGraph(
            torque_main=self.motor_tork, rpm_main=self.motor_hiz,graph_title="rb 26 motoru"
        )
        graph_instance.plot_torque_rpm_hp_graph()
        
        
    def only_tractive_effort_vs_vehicle_speed(self):
        graph_instance = EngineDataGraph(
            torque_main=self.motor_tork, rpm_main=self.motor_hiz,graph_title="rb 26 motoru"
        )
        
        graph_instance.only_tractive_effort_vs_vehicle_speed(
            tractive_f_list=tractive_f(
                tork_list=self.tork_times_gear_list(), ################################################################sorunlu
                r_w=self.arac.tekerlek_yaricap,
                t_efficiency=self.arac.ao_verimi,
            ),
            hiz_list=self.arac_v_list(),
        )
        
    
        #  --------------------------------------------------------Kontrol Edilecek----------------------------------------------------------
    def cs_final_tractive_force_vs_vehicle_speed(self):
        graph_instance = EngineDataGraph(
            torque_main=self.motor_tork, rpm_main=self.motor_hiz,graph_title="rb 26 motoru"
        )
        graph_instance.cs_final_tractive_force_vs_vehicle_speed(
            f_list=final_force(
                resist_f=self.cs_resist_forces(),
                tractive_f=tractive_f(
                    tork_list=self.tork_times_gear_list(),
                    r_w=self.arac.tekerlek_yaricap,
                    t_efficiency=self.arac.ao_verimi,
                ),
            ),
            hiz_list=self.arac_v_list(),
        )
        return graph_instance