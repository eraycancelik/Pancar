from engine import Motor
from utils import kmh_to_ms
import shelve
from graphs import EngineDataGraph
from calculations import (
    overall_resist_forces,
    cs_overall_resist_forces,
    tractive_f,
    final_force,
)
import pprint
arac_tork_name = "2jz_tork"
arac_rpm_name = "2jz_rpm"


disli_kutusu = [3.23, 2.52, 1.66, 1.22, 1, 3.45]

dif_orani = 3.45
yaricap = 0.299  # metre
verim = 0.85
yuvarlanma_katsiyi = 0.015
w_arac = 1500
# aerodinamik direnç katsayıları
hava_yogunlugu = 1
ruzgar_hizi = 20  # km/saat
izdusum = 4
ae_katsayi = 0.19
yol_egimi = 0
arac = Motor(
    gearBox=disli_kutusu,
    oran_diferansiyel=dif_orani,
    tekerlek_yaricap=yaricap,
    ao_verimi=verim,
    arac_kutlesi=w_arac,
    yuvarlanma_katsiyi=yuvarlanma_katsiyi,
    ro_hava_yogunlugu=hava_yogunlugu,
    v_ruzgar=kmh_to_ms(ruzgar_hizi),
    af_arac_izdusum_alanı=izdusum,
    cd_aerodinamik_direnc_katsayisi=ae_katsayi,
    yol_egimi=yol_egimi,
)

engine_db = shelve.open("engines.db")
    # doc = Document()
    # doc.save("grafikler.docx")


    
tork_times_gear_list = arac.torque_rev_per_gear(
    tork_list=engine_db[arac_tork_name], overall_gear_ratio=arac.gearBox
)
# print(engine_db[arac_tork_name])

arac_v_list = arac.velocity_rpm(rpm=engine_db[arac_rpm_name], gear_box=arac.gearBox)
windy_v_list = arac.windy_velocity_rpm(
    rpm=engine_db[arac_rpm_name], gear_box=arac.gearBox, ruzgar_hizi=arac.v_ruzgar
)
resist_forces = overall_resist_forces(
    arac_kutlesi=arac.arac_kutlesi,
    cekim_ivmesi=arac.cekim_ivmesi,
    yuvarlanma_katsiyi=arac.yuvarlanma_katsiyi,
    yol_egimi=arac.yol_egimi,
    p_yogunluk=arac.ro_hava_yogunlugu,
    cw_aero=arac.cd_aerodinamik_direnc_katsayisi,
    Af_izdusum=arac.af_arac_izdusum_alanı,
    hiz_list=windy_v_list,
)
cs_resist_forces = cs_overall_resist_forces(
    arac_kutlesi=arac.arac_kutlesi,
    cekim_ivmesi=arac.cekim_ivmesi,
    yuvarlanma_katsiyi=arac.yuvarlanma_katsiyi,
    yol_egimi=arac.yol_egimi,
    p_yogunluk=arac.ro_hava_yogunlugu,
    cw_aero=arac.cd_aerodinamik_direnc_katsayisi,
    Af_izdusum=arac.af_arac_izdusum_alanı,
    hiz_list=arac_v_list,
    ruzgar_hizi=arac.v_ruzgar,
)
    # tork_times_gear_list = arac.torque_rev_per_gear(
    #     tork_list=engine_db["rb_26_tork"],
    #     overall_gear_ratio=overall_gear_ratio(
    #         gearBox=arac.gearBox, differential_gear_ratio=arac.oran_diferansiyel
    #     ),
    # )

    # arac_v_list = arac.velocity_rpm(
    #     rpm=engine_db["rb_26_rpm"],
    #     gear_box=overall_gear_ratio(
    #         gearBox=arac.gearBox, differential_gear_ratio=arac.oran_diferansiyel
    #     ),
    # )
    # pprint(len(arac_v_list[0]))

    # pprint(tork_times_gear_list)
    # pprint(len(tork_times_gear_list[0]))

arac_graph = EngineDataGraph(
        engine_db, arac_tork_name, arac_rpm_name, "rb 26 motoru"
    )
def torque_rpm_graph():
    arac_graph.torque_rpm_graph()  # araç tork vs rpm grafiği
    
def torque_rpm_power_graph():
    arac_graph.plot_torque_rpm_hp_graph()  # araç tork vs rpm,güç grafiği,
    
def rpm_v_graph():
    arac_graph.rpm_v_graph(  # viteslere göre motor hızı vs araç hızı grafiği
        list=arac_v_list,
        rpm=engine_db[arac_rpm_name],
    )
    # # ########################################################################################
def only_tractive_effort_vs_vehicle_speed():
    arac_graph.only_tractive_effort_vs_vehicle_speed(
        tractive_f_list=tractive_f(
            tork_list=tork_times_gear_list,
            r_w=arac.tekerlek_yaricap,
            t_efficiency=arac.ao_verimi,
        ),
        hiz_list=arac_v_list,
    )

    # arac_graph.final_tractive_force_vs_vehicle_speed(
    #     f_list=final_force(
    #         resist_f=resist_forces,
    #         tractive_f=tractive_f(
    #             tork_list=tork_times_gear_list,
    #             r_w=arac.tekerlek_yaricap,
    #             t_efficiency=arac.ao_verimi,
    #         ),
    #     ),
    #     hiz_list=windy_v_list,
    # )
    # #####################################################################################

    #  --------------------------------------------------------Kontrol Edilecek----------------------------------------------------------
def cs_final_tractive_force_vs_vehicle_speed():
    arac_graph.cs_final_tractive_force_vs_vehicle_speed(
        f_list=final_force(
            resist_f=cs_resist_forces,
            tractive_f=tractive_f(
                tork_list=tork_times_gear_list,
                r_w=arac.tekerlek_yaricap,
                t_efficiency=arac.ao_verimi,
            ),
        ),
        hiz_list=arac_v_list,
    )
    # arac_graph.torque_rev_per_gear_graph(
    #     geared_torque=tork_times_gear_list, rpm=engine_db[arac_rpm_name]
    # )
    # arac_graph.geared_tork_vs_road_speed_graph(
    #     geared_torque=tork_times_gear_list, list=arac_v_list
    # )
only_tractive_effort_vs_vehicle_speed()
engine_db.close()