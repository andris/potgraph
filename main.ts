let pot1 = 0
forever(function () {
    pot1 = pins.A6.analogRead()
    light.graph(pot1, 1023)
})
