from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'Readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TLV493D',

    version='1.0.1',

    description='CircuitPython driver for 3D Magnetic Sensor.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url="https://github.com/Infineon/RaspberryPi_TLV",

  
    license='MIT',

   
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    
    py_modules=['TLV'],
)