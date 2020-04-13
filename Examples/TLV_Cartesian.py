import TLV

from time import sleep

tlv493d = TLV.TLV493D()

while True:
    tlv493d.update_data()
    x = tlv493d.get_x()
    y = tlv493d.get_y()
    z = tlv493d.get_z()
    temp = tlv493d.get_temp()

    print("x: ", x, "y: ", y, "z: ",z,"temp: ",temp)
    sleep(0.5)