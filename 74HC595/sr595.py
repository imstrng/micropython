"""
Serial In Parallel Out Shift Register

            74HC575

dataPin   : DS    14 
clockPin  : SH_CP 11
latchPin  : ST_CP 12
enablePin : MR    10
"""

class SR:
    def __init__(self, dataPin, clockPin, latchPin, enablePin = None):
        self.dataPin = dataPin
        self.clockPin = clockPin
        self.latchPin = latchPin
        self.enablePin = enablePin
        print('Initialized')

    def data(self,value):
        self.dataPin(value)

    def clock(self):
        self.clockPin(1)
        self.clockPin(0)

    def latch(self):
        self.latchPin(1)
        self.latchPin(0)

    def enable(self):
        if self.enablePin != None:
            self.enablePin(0)
        else:
            print('enablePin not definded')

    def disable(self):
        if self.enablePin != None:
            self.enablePin(1)
        else:
            print('enablePin not definded')

    def append(self,value):
        self.data(value)
        self.clock()
        self.latch()