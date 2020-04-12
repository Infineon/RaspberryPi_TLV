
# TLV493D-A1B6-3DMagnetic-Sensor

<img src="https://github.com/Infineon/Assets/blob/master/Pictures/3D%20Magnetic%20Sensor%202Go.jpg" width=250> <img src="https://github.com/Infineon/Assets/blob/master/Pictures/TLV493D-Sense-Shield2Go_Top_plain.jpg_2045671804.jpg?raw=true" width=300> 

## Summary
The 3D magnetic sensor TLV493D-A1B6 offers accurate three-dimensional sensing with extremely low power consumption in a small 6-pin package. With its magnetic field detection in x, y, and z-direction the sensor reliably measures three-dimensional, linear and rotation movements. Applications include joysticks, control elements (white goods, multifunction knops), or electric meters (anti tampering) and any other application that requires accurate angular measurements or low power consumptions.

Key features are 3D magnetic sensing with a very low power consumption during operations. The sensor has a digital output via 2-wire based standard I2C interface up to 1 MBit/sec and 12 bit data resolution for each measurement direction (Bx, By and Bz linear field measurement up to +-130mT).

## Key Features and Benefits
* Integrated temperature sensing
* Low current consumption of 0.007 µA in power down mode and 10 µA in ultra low power mode
* 2.7 to 3.5 V operating supply voltage
* Digital output via 2-wire standard I2C interface
* Bx, By and Bz linear field measurement up to ±130 mT
* 12-bit data resolution for each measurement direction
* Resolution 98 µT/LSB
* Operating temperature range from -40 °C to 125 °C

Dependencies
============

This driver depends on:

* python version 3 and above
* [SMBus](https://github.com/kplindegaard/smbus2)

Please ensure all dependencies are resolved before proceeding further.

Steps for installation
----------------------

Supported hardware --> Raspberry pi Zero/3/3B+/4B

* Update apt

```

sudo apt update

```


* Enable i2c (Interfacing options menu and then I2C enable). For detailed steps see this [article](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/).

```

sudo raspi-config

```


* Install pip3

```

sudo apt install python3-pip

```


* Install smbus

```

pip3 install smbus
sudo apt-get install -y python-smbus i2c-tools

```

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver from [PyPI](https://pypi.org/)

For current user:
```

pip3 install TLV493D

```

To install system-wide (this may be required in some cases):
```

sudo pip3 install TLV493D

```

Connection diagram:
-------------------
<img src="https://github.com/Infineon/Assets/blob/master/Pictures/RPi_Connection_TLV.PNG" width=550 >  

| Raspberry Pi | TLV |
| :---: |:---:|
| 3.3V | 3V3 |
| GND | GND |
| BCM 2 (pin3) | SDA |
| BCM 3 (pin 5) | SCL |





* Clone the Github repository or download the .zip, unzip it, go to examples folder and run the sample code.



## Printables
The TLx493D 3D magnetic sensor family has additional tools which can be directly mounted on top of the evaluation boards. The 3D print data of the [joystick](https://www.infineon.com/cms/en/product/promopages/sensors-2go/#Add-ons-3D-Magnetic-2GO), the [rotate knob](https://www.infineon.com/cms/en/product/promopages/sensors-2go/#Add-ons-3D-Magnetic-2GO) and the [linear slider](https://www.infineon.com/cms/en/product/promopages/sensors-2go/#Add-ons-3D-Magnetic-2GO) can be found in the folder `printables`.

<img src="https://www.infineon.com/export/sites/default/media/products/Sensors/joystick.jpg_708092179.jpg" width=250>

## Board Information, Datasheet and Additional Information

The datasheet for the TLV493D-A1B6 can be found here [TLV493D-A1B6 Datasheet](https://www.infineon.com/dgdl/Infineon-TLV493D-A1B6-DS-v01_00-EN.pdf?fileId=5546d462525dbac40152a6b85c760e80) while respective application notes are located here [Application Notes](https://www.infineon.com/dgdl/Infineon-TLV493D-A1B6_3DMagnetic-UM-v01_03-EN.pdf?fileId=5546d46261d5e6820161e75721903ddd).

Please check the [wiki](https://github.com/Infineon/TLV493D-A1B6-3DMagnetic-Sensor/wiki) with more information for the TLV493D-A1B6 3DSense Shield2Go as well.
