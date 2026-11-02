class SmartDevice:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        print(f'{self.name}: LED turned on with warm brightness.')

    def turn_off(self):
        print(f'{self.name}: LED turned off.')

class Fan(SmartDevice):
    def turn_on(self):
        print(f'{self.name}: Ceiling fan spinning at speed 4.')

    def turn_off(self):
        print(f'{self.name}: Ceiling fan stopped.')

class AC(SmartDevice):
    def turn_on(self):
        print(f'{self.name}: AC cooling set to 24°C.')

    def turn_off(self):
        print(f'{self.name}: AC powered off.')

class TV(SmartDevice):
    def turn_on(self):
        print(f'{self.name}: Smart TV display turned on to HDMI 1.')

    def turn_off(self):
        print(f'{self.name}: Smart TV entered standby mode.')

devices = [Light('Living Room Light'), Fan('Master Bedroom Fan'), AC('Guest Room AC'), TV('Hall TV')]
for d in devices:
    d.turn_on()
    d.turn_off()
