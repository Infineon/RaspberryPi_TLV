import TLV

from time import sleep

tlv493d = TLV.TLV493D()

while True:
    tlv493d.update_data()
    x = tlv493d.get_x()
    y = tlv493d.get_y()
    z = tlv493d.get_z()

    print("x: ", x, "y: ", y, "z: ",z)
