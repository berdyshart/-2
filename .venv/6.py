def ft_to_kg(ft):
    return ft/2.205
def dm_to_m(dm):
    return dm*2.54/100
weight_ft = float(input())
height_dm = float(input())
IMT = ft_to_kg(weight_ft)/dm_to_m(height_dm)**2
print(round(IMT, 2))
