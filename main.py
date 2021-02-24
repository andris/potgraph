pot1 = 0

def on_forever():
    global pot1
    pot1 = pins.A1.analog_read()
    light.graph(pot1, 1023)
forever(on_forever)
