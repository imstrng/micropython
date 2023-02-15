from machine import Pin
from time import sleep_us

class kaku:
    def __init__(self,pin=2):
        self.txPin = Pin( pin, Pin.OUT)
        self.pin = pin
        self.msg = ''
        self.pulsetrain = ''

    def tx(self, msg):
        self.msg = msg
        self.pulsetrain = "1" + "0"*9
        for b in range(0,len(self.msg)):
            self.pulsetrain = self.pulsetrain + "100010" if self.msg[b] == '1' else self.pulsetrain + "101000"
        self.pulsetrain = self.pulsetrain + '1' + '0'*40
        pulses = list(map(int, self.pulsetrain))
        for i in range(7):
            for p in pulses:
                self.txPin.value(p)
                sleep_us(102)

    def On(self, address=1337, unit=1):
        self.msg = "{0:026b}".format(address) + '01' + "{0:04b}".format(unit)
        self.tx(self.msg)

    def Off(self, address=1337, unit=1):
        self.msg = "{0:026b}".format(address) + '00' + "{0:04b}".format(unit)
        self.tx(self.msg)

