from math import pi

def deg_to_gms(deg, formats = 'string'):
    degrees = int(deg)

    minutes = int((deg-degrees) * 60)
    secounds = (((deg-degrees) * 60) - minutes) * 60
    secounds = round(secounds)
    return(degrees, minutes, secounds)


def gms_to_deg(degrees, minutes, secounds):
    deg = round(degrees + minutes / 60 + secounds / 3600, 3)
    return deg
def deg_to_rad(deg):
    rad = deg + pi / 180
    return rad
def rad_to_deg(rad):
    deg = rad * 180 / pi
    return deg

if __name__ == "__main__":
    print(deg_to_gms(3.97))
    print(gms_to_deg(25, 50, 424))