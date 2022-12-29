kelvin_list = [200,334,455,586,598,987,635,600,484,300]

for K in kelvin_list:
    F = ((K - (273.15)) * 9 / 5 + 32)
    C = (K - 273.15)
    print(f"""{K} K = {F} degree Faranheit = {C} degree celsius""" )