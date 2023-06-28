import numpy as np

d_original = 15.1  # Diameter av mønsteret på lampen [mm]
n = 1.520  # Brytningsindex til linsene
S1_obj = 1260  # Avstand Lampe - Linse [mm]
S1_img = 240  # Avstand Linse - Bilde [mm]
S2_obj = 300  # Avstand Lampe - Linse [mm]
S2_img = 600  # Avstand Linse - Bilde [mm]
sph_met_rad = 12  # Radius av sfærometeret[mm]
d = 0.36  # Målte verdien med sfærometeret [mm]


def focal_len(s_obj, s_img):  # Beregener fokallengde
    return 1/((1/s_obj) + (1/s_img))


def magnification(s_obj, s_img):  # Beregner forstørrelse
    return s_img/s_obj


def lens_rad(D, d):  # Beregner krumningsradius
    return ((D**2) + (d**2))/(2*d)


def linsemaker(n, R1, R2):  # Linsemakerformelen
    return 1/((n-1)*((1/R1)-(1/R2)))


f1 = focal_len(S1_obj, S1_img)  # Fokallengde for punkt 3
M1 = magnification(S1_obj, S1_img)  # Forstørrelse for 150 cm avstand
M2 = magnification(S1_img, S1_obj)  # Forstørrelse for 150 cm avstand
M3 = magnification(S2_obj, S2_img)  # Forstørrelse for 90 cm avstand
M4 = magnification(S2_img, S2_obj)  # Forstørrelse for 90 cm avstand
rad_lens = lens_rad(sph_met_rad, d)  # Krumningsradius for 200 mm linsen  [mm]
f1_linsemaker = linsemaker(n, rad_lens, -rad_lens)  # Fokallengde for 200 mm linsen  [mm]

print(M1)
print(M2)
print(rad_lens)
print(f1_linsemaker)
