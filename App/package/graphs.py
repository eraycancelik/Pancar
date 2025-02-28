import matplotlib.pyplot as plt
import numpy as np
from .calculations import powerInHp
import gc
class EngineDataGraph:
    def __init__(self, torque_main, rpm_main, graph_title):
        self.torque_main = torque_main
        self.rpm_main = rpm_main
        self.graph_title = graph_title

    def plot_torque_rpm_hp_graph(self):
        rpm_interpolated = np.linspace(
            min(self.rpm_main),
            max(self.rpm_main),
            len(powerInHp(self.torque_main, self.rpm_main)),
        )

        fig, ax1 = plt.subplots()

        ax1.plot(self.rpm_main, self.torque_main, color="blue")
        ax1.set_xlabel("rpm (d/d)")
        ax1.set_ylabel("tork (Nm)", color="blue")
        ax1.set_title(self.graph_title)

        ax2 = ax1.twinx()
        ax2.plot(
            rpm_interpolated, powerInHp(self.torque_main, self.rpm_main), color="red"
        )
        ax2.set_ylabel("güç (hp)", color="red")

        self._customize_axes(ax1, ax2)

        ax1.grid(which="both", axis="both", linestyle="--", linewidth=0.5)

        ax2.grid(which="both", axis="both", linestyle="--", linewidth=0.5)

        plt.show()
        del ax1,ax2
        gc.collect
        # sys.exit()

    def _customize_axes(self, ax1, ax2):
        ax1.set_ylim(min(self.torque_main), max(self.torque_main) + 50)
        ax1_y_ticks = np.arange(0, max(self.torque_main), 50)
        ax1.set_yticks(ax1_y_ticks)
        ax1.tick_params(
            axis="y", labelcolor="blue", which="both", left=True, right=False
        )

        ax2.set_ylim(min(self.torque_main), max(self.torque_main) + 50)
        ax2_y_ticks = np.arange(0, max(self.torque_main), 50)
        ax2.set_yticks(ax2_y_ticks)
        ax2.tick_params(
            axis="y", labelcolor="red", which="both", left=False, right=True
        )

    def torque_rpm_graph(self):
        plt.plot(self.rpm_main, self.torque_main, color="red")
        plt.xlabel("Motor devir hızı (d/d)")
        plt.ylabel("Tork (Nm)")
        plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
        plt.suptitle("Tork - Motor Devri grafiği")
        plt.show()

    def rpm_v_graph(self, liste, rpm):
        a = 1
        for i in liste:
            plt.plot(i, rpm, label=(f"{a}. vites"))
            plt.legend()
            a += 1
        plt.xlabel("Araç Hızı")
        plt.ylabel("Motor devir hızı")
        plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
        plt.suptitle("Motor Hızı vs Araç Hızı")
        plt.show()
        del a,i
        gc.collect

    def torque_rev_per_gear_graph(self, geared_torque, rpm):
        a = 1
        for i in geared_torque:
            plt.plot(rpm, i, label=(f"{a}. vites"))
            plt.legend()
            a += 1
        plt.xlabel("Motor devir hızı")
        plt.ylabel("Tork")
        plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
        plt.suptitle("viteslerdeki tork vs rpm")
        plt.show()
        del a,i,geared_torque,rpm
        gc.collect

    def geared_tork_vs_road_speed_graph(self, geared_torque, list):
        c = 1
        for a, b in zip(list, geared_torque):
            plt.plot(a, b, label=(f"{c}. vites"))
            plt.legend()
            c += 1
        plt.xlabel("Araç Hızı (km/h)")
        plt.ylabel("Tekerlek Torku (Nm)")
        plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
        plt.suptitle("Tekerlek Torku vs Yol Hızı")
        plt.show()
        del geared_torque,list,a,b,c
        gc.collect

    def only_tractive_effort_vs_vehicle_speed(self, tractive_f_list, hiz_list):
        print("--------------------------------------------------------------------------------0")
        print(tractive_f_list)
        c = 1
        for a, b in zip(tractive_f_list, hiz_list):
            plt.plot(b, a, label=(f"{c}. vites"))
            plt.legend()
            c += 1
        plt.xlabel("Araç Hızı (km/h)")
        plt.ylabel("Çekiş gücü (N)")
        plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
        plt.suptitle("Çekiş Gücü vs Yol Hızı")
        plt.show()
        del a,b,c,tractive_f_list,hiz_list
        gc.collect

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
        plt.show()
        del a,b,c,f_list,hiz_list
        gc.collect

    def cs_final_tractive_force_vs_vehicle_speed(self, f_list, hiz_list):
        c = 1
        for a, b in zip(f_list, hiz_list):
            plt.plot(b, a, label=(f"{c}. vites"))
            plt.legend()
            c += 1
        plt.xlabel("Araç Hızı (km/h)")
        plt.ylabel("Final Çekiş gücü (N)")
        plt.grid(which="both", axis="both", linestyle="--", linewidth=0.5)
        plt.suptitle("Final Çekiş Gücü vs Yol Hızı")
        plt.show()
        del a,b,c,f_list,hiz_list
        gc.collect
        
