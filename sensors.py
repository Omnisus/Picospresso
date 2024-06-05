from machine import Pin, Timer, I2C, ADC

class pressure:
    def __init__(self, adcpin=1):
        #Calibration data
        self.pressureRange = 200
        self.voltageLowerLimit = 0.344
        self.voltageUpperLimit = 3.094
    
        self.adc = ADC(1)

    def read():
        self.volts = self.adc.read_u16() * 3.3 / 65535 
        self.psi = (self.volts - self.voltageLowerLimit)/(self.voltageUpperLimit-self.voltageLowerLimit)*self.pressureRange
        self.bar = self.psi / 14.5038

    def get_bar():
        self.read()
        return(self.bar)


class flow:
    def __init__(self, pinin=3):
        #Calibration data
        self.revolutions_per_liter = 1925
        
        self.spin_volume = 1000 / self.revolutions_per_liter # ml per revolution

        self.pin_IN = Pin(pinin,Pin.IN,pull=Pin.PULL_DOWN)
        self.pin_IN.irq(trigger=self.pin_IN.IRQ_RISING,handler=self.update)
        self.last_time = 0
        self.count = 0
        self.last_count = 0
        self.flow = 0

    def update(self,pin):
        self.count += 1

    def compute(self):
        current_time = time.ticks_ms()
        
        if self.last_time != 0:
            delta_time = time.ticks_diff(current_time, self.last_time)
            delta_count = self.count - self.last_count
            self.flow = self.spin_volume * delta_count / (delta_time / 1000) # ml / sec
        
        self.last_time = self.current_time
        self.last_count = self.count

class weight:
    pass
    
class temperature:
    pass