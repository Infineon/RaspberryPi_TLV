import TLV

from time import sleep

tlv493d = TLV.TLV493D()

while True:
    tlv493d.update_data()
    tlv493d.get_x()
    tlv493d.get_y()
    tlv493d.get_z()
    br = tlv493d.get_br()
    polar = tlv493d.get_polar()
    azimuth = tlv493d.get_azimuth()

    print("br: ", br, "polar: ", polar, "azimuth: ",azimuth)