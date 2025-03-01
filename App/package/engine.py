from math import pi, cos, sin


class Motor:
    def __init__(
        self,
        # motor değerleri
        gearBox,
        oran_diferansiyel,
        tekerlek_yaricap,
        ao_verimi,
        v_ruzgar,  # metre/saniye
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
        self.gearBox = gearBox
        self.oran_diferansiyel = oran_diferansiyel
        self.tekerlek_yaricap = tekerlek_yaricap
        self.ao_verimi = ao_verimi
        self.yuvarlanma_katsiyi = yuvarlanma_katsiyi
        self.arac_kutlesi = arac_kutlesi
        self.yol_egimi = yol_egimi
        self.ro_hava_yogunlugu = ro_hava_yogunlugu
        self.af_arac_izdusum_alanı = af_arac_izdusum_alanı
        self.cd_aerodinamik_direnc_katsayisi = cd_aerodinamik_direnc_katsayisi
        self.v_ruzgar = v_ruzgar
        self.cekim_ivmesi = cekim_ivmesi

    def f_yol_direnci(self):
        yol_direncleri = (self.arac_kutlesi * self.cekim_ivmesi) * (
            self.yuvarlanma_katsiyi * cos(self.yol_egimi) + sin(self.yol_egimi)
        )
        return yol_direncleri

    def f_aerodinamik_direnc(self):
        aerodinamik_direnc = (
            self.ro_hava_yogunlugu
            * self.af_arac_izdusum_alanı
            * self.cd_aerodinamik_direnc_katsayisi
            * pow(self.v_arac + self.v_ruzgar, 2)
        ) / 2
        return aerodinamik_direnc

    def velocity_rpm(self, rpm, gear_box):
        gear_set = gear_box[:]
        overall_list = []
        for i in gear_set:
            velocity_list = []
            for a in rpm:
                velocity = (3.6 * (pi / 30) * a * self.tekerlek_yaricap) / (
                    i * self.oran_diferansiyel
                )
                velocity_list.append(round(velocity, 2))
            overall_list.append(velocity_list)

        return overall_list

    def windy_velocity_rpm(self, rpm, gear_box, ruzgar_hizi):
        gear_set = gear_box[:]
        overall_list = []

        for i in gear_set:
            velocity_list = []
            for a in rpm:
                velocity = (3.6 * (pi / 30) * a * self.tekerlek_yaricap) / (
                    i * self.oran_diferansiyel
                )
                velocity_list.append(round(velocity, 2) - ruzgar_hizi)
            overall_list.append(velocity_list)

        return overall_list

    def torque_rev_per_gear(self, overall_gear_ratio, tork_list):
        overall_list = []
        gear = overall_gear_ratio[:]
        for a in gear:
            sub_list = []
            for b in tork_list:
                sub_list.append(round(b * a, 2))
            overall_list.append(sub_list)
        return overall_list

        # gear_set = self.gearBox.pop()
        # velocity_list = []
        # for i in gear_set:
        #     velocity = (3.6 * (pi / 30) * rpm * self.tekerlek_yaricap) / (
        #         i * self.gearBox[-1]
        #     )
        #     velocity_list.append(velocity)
        # return velocity_list
