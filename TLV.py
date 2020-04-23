import smbus
import math
from time import sleep



class TLV493D:
    
    """Class of 3D Magnetic Sensor TLV493D.
    """
    
    addr = 0x5e
    
    bx = 0
    by = 0
    bz = 0 
    temp = 0
    data =[]
    bus = smbus.SMBus(1)
    
    
    

    def update_data(self):
        """ Read data from register
        """
        global data 
        self.bus.write_byte_data(self.addr, 0x11,0x01)

        data = self.bus.read_i2c_block_data(self.addr, 0x00, 10)
        
      
    def get_x(self):
        """ Get the value of X coordinate
            
            Returns:
            
            int: X coordinate
        """
        
        self.bx = (data[0] << 4) or ((data[4] >> 4) & 0x0f)
        
        if self.bx > 2047:
            
            self.bx -= 4096
        self.bx *=0.098
            
        return self.bx
    
    
    
    
    def get_y(self):
        """ Get the value of Y coordinate
            
            Returns:
            
            int: Y coordinate
        """
        self.by = data[1] << 4 or data[4] & 0x0f

        
        if self.by > 2047:
            
            self.by -= 4096
        self.by *=0.098
            
        return self.by
    
    
    
    
    def get_z(self):
        """ Get the value of Z coordinate
            
            Returns:
            
            int: Z coordinate
        """
        
        self.bz = data[2] << 4 or data[5] & 0x0f
        
        if self.bz > 2047:
            
            self.bz -= 4096
        self.bz *=0.098
            
        return self.bz
    
    
    
    def get_br(self):
        """ Calculate the radial value
            
            Returns:
            
            double : radial value
        """
        
        br = math.sqrt(self.bx*self.bx+self.by*self.by+self.bz*self.bz)
        
        return br
    
    
    
    
    def get_polar(self):
        """ Calculate the polar value
            
            Returns:
            
            double: polar value
        """
        
        polar = math.cos(math.atan2(self.bz,math.sqrt(self.bx*self.bx+self.by*self.by)))
        
        return polar
    
    
    
    
    def get_azimuth(self):
        """ Calculate the azimuthal value
            
            Returns:
            
            double: azimuthal value
        """
        
        azimuth = math.atan2(self.by,self.bx)
        
        return azimuth
  
