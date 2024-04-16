import matplotlib.pyplot as plt
import numpy as np
from ..package.calculations import powerInHp
import gc
def rpm_v_graph(liste, rpm):
    a = 1
    for i in liste:
        plt.plot(i, rpm, label=(f"{a}. vites"))
        plt.legend()
        a += 1
    plt.xlabel("Araç Hızı")
    plt.ylabel("Motor devir hızı")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("rpm vs vehicle speed")
    plt.savefig("rpm_v_graph.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("rpm_v_graph.png")
    # return a
    

def torque_rpm_graph(rpm,torque):
    plt.plot(rpm,torque, color="red")
    plt.xlabel("Motor devir hızı (d/d)")
    plt.ylabel("Tork (Nm)")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("Tork - Motor Devri grafiği")
    plt.savefig("torque_rpm_graph.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("torque_rpm_graph.png")
    # return a

def _customize_axes(torque, ax1, ax2):
    ax1.set_ylim(min(torque), max(torque) + 50)
    ax1_y_ticks = np.arange(0, max(torque), 50)
    ax1.set_yticks(ax1_y_ticks)
    ax1.tick_params(
        axis="y", labelcolor="blue", which="both", left=True, right=False
    )
    ax2.set_ylim(min(torque), max(torque) + 50)
    ax2_y_ticks = np.arange(0, max(torque), 50)
    ax2.set_yticks(ax2_y_ticks)
    ax2.tick_params(
        axis="y", labelcolor="red", which="both", left=False, right=True
    )
    gc.collect()  # Belleği temizle
    
def plot_torque_rpm_hp_graph(rpm,torque):
    rpm_interpolated = np.linspace(
        min(rpm),
        max(rpm),
        len(powerInHp(tork=torque, devir=rpm)),
    )
    fig, ax1 = plt.subplots()
    ax1.plot(rpm, torque, color="blue")
    ax1.set_xlabel("rpm (d/d)")
    ax1.set_ylabel("tork (Nm)", color="blue")
    ax1.set_title("self.graph_title")
    ax2 = ax1.twinx()
    ax2.plot(
        rpm_interpolated, powerInHp(torque, rpm), color="red"
    )
    ax2.set_ylabel("güç (hp)", color="red")
    _customize_axes(torque,ax1, ax2)
    ax1.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    ax2.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.savefig("plot_torque_rpm_hp_graph.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("plot_torque_rpm_hp_graph.png")
    # return a

def torque_rev_per_gear_graph(geared_torque, rpm):
    a = 1
    for i in geared_torque:
        plt.plot(rpm, i, label=(f"{a}. vites"))
        plt.legend()
        a += 1
    plt.xlabel("Motor devir hızı")
    plt.ylabel("Tork")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("viteslerdeki tork vs rpm")
    plt.savefig("torque_rev_per_gear_graph.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("torque_rev_per_gear_graph.png")
    # return a

def geared_tork_vs_road_speed_graph(geared_torque, list):
    c = 1
    for a, b in zip(list, geared_torque):
        plt.plot(a, b, label=(f"{c}. vites"))
        plt.legend()
        c += 1
    plt.xlabel("Araç Hızı (km/h)")
    plt.ylabel("Tekerlek Torku (Nm)")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("Tekerlek Torku vs Yol Hızı")
    plt.savefig("./geared_tork_vs_road_speed_graph.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("./geared_tork_vs_road_speed_graph.png")
    # return a

def only_tractive_effort_vs_vehicle_speed(tractive_f_list, hiz_list):
    c = 1
    for a, b in zip(tractive_f_list, hiz_list):
        plt.plot(b, a, label=(f"{c}. vites"))
        plt.legend()
        c += 1
    plt.xlabel("Araç Hızı (km/h)")
    plt.ylabel("Çekiş gücü (N)")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("Çekiş Gücü vs Yol Hızı")
    plt.savefig("only_tractive_effort_vs_vehicle_speed.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    
    # a=plt.savefig("only_tractive_effort_vs_vehicle_speed.png")
    # return a
    
def final_tractive_force_vs_vehicle_speed(self, f_list, hiz_list):
    c = 1
    for a, b in zip(f_list, hiz_list):
        plt.plot(b, a, label=(f"{c}. vites"))
        plt.legend()
        c += 1
    plt.xlabel("Araç Hızı (km/h)")
    plt.ylabel("Final Çekiş gücü (N)")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("Final Çekiş Gücü vs Yol Hızı")
    plt.savefig("final_tractive_force_vs_vehicle_speed.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("final_tractive_force_vs_vehicle_speed.png")
    # return a

def cs_final_tractive_force_vs_vehicle_speed(f_list, hiz_list):
    c = 1
    for a, b in zip(f_list, hiz_list):
        plt.plot(b, a, label=(f"{c}. vites"))
        plt.legend()
        c += 1
    plt.xlabel("Araç Hızı (km/h)")
    plt.ylabel("Final Çekiş gücü (N)")
    plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
    plt.suptitle("Final Çekiş Gücü vs Yol Hızı")
    plt.savefig("cs_final_tractive_force_vs_vehicle_speed.png")
    plt.clf()  # Mevcut figürü temizle
    gc.collect()  # Belleği temizle
    # a=plt.savefig("cs_final_tractive_force_vs_vehicle_speed.png")
    # return a