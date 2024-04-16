import math


def powerInHp(tork, devir):
    hp = [(a * b) / 7127 for a, b in zip(tork, devir)]

    return hp


def powerInKw(tork, devir):
    kw = [
        round(((a * b) * ((2 * math.pi) / 60) * (1 / 1000)), 2)
        for a, b in zip(tork, devir)
    ]
    return kw


def overall_gear_ratio(gearBox, differential_gear_ratio):
    gear_list = [1]
    for i in gearBox:
        gear_list.append(gear_list[-1] * i)
    gear_list.pop(0)
    response = [a * differential_gear_ratio for a in gear_list]
    # response.append(round(differential_gear_ratio * i, 2))
    return response


def road_resist_forces(arac_kutlesi, cekim_ivmesi, yuvarlanma_katsiyi, yol_egimi):
    F_road = (arac_kutlesi * cekim_ivmesi) * (
        yuvarlanma_katsiyi * math.cos(yol_egimi) + math.sin(yol_egimi)
    )
    return F_road


def ae_forces(p_yogunluk, cw_aero, Af_izdusum, arac_hizi):
    F_aero = (p_yogunluk * cw_aero * Af_izdusum * arac_hizi) / 2
    return F_aero


def tractive_f(tork_list, r_w, t_efficiency):
    overall_Ft = []
    for _ in tork_list:
        subTork_list = []
        for a in _:
            subTork_list.append(((a) / r_w) * t_efficiency)
        overall_Ft.append(subTork_list)
    return overall_Ft


def overall_resist_forces(
    arac_kutlesi,
    cekim_ivmesi,
    yuvarlanma_katsiyi,
    yol_egimi,
    p_yogunluk,
    cw_aero,
    Af_izdusum,
    hiz_list,
):
    overall_F_r = []
    for _ in hiz_list:
        sublist = []
        for i in _:
            resistors = (arac_kutlesi * cekim_ivmesi) * (
                yuvarlanma_katsiyi * math.cos(math.radians(yol_egimi))
                + math.sin(math.radians(yol_egimi))
            ) + (p_yogunluk * cw_aero * Af_izdusum * (i)) / 2
            sublist.append(resistors)
        overall_F_r.append(sublist)
    return overall_F_r


def cs_overall_resist_forces(
    arac_kutlesi,
    cekim_ivmesi,
    yuvarlanma_katsiyi,
    yol_egimi,
    p_yogunluk,
    cw_aero,
    Af_izdusum,
    hiz_list,
    ruzgar_hizi,
):
    overall_F_r = []
    for _ in hiz_list:
        sublist = []
        for i in _:
            resistors = (arac_kutlesi * cekim_ivmesi) * (
                yuvarlanma_katsiyi * math.cos(math.radians(yol_egimi))
                + math.sin(math.radians(yol_egimi))
            ) + ((p_yogunluk * cw_aero * Af_izdusum * (i + ruzgar_hizi)) / 2)
            sublist.append(resistors)
        overall_F_r.append(sublist)
    return overall_F_r


def final_force(tractive_f, resist_f):
    liste = []
    for f, d in zip(tractive_f, resist_f):
        sublist = []
        for a, b in zip(f, d):
            f_net = a - b
            sublist.append(f_net)
        liste.append(sublist)
    return liste
