input.onButtonPressed(Button.B, function () {
    basic.showNumber(Score)
    Score = 0
})
let rastGeleBolunen = 0
let Score = 0
let Flag = true
Score = 0
let rastGeleBolen = randint(2, 9)
basic.showNumber(rastGeleBolen)
basic.pause(500)
basic.clearScreen()
basic.pause(200)
basic.forever(function () {
    if (Flag) {
        rastGeleBolunen = randint(10, 99)
        basic.showNumber(rastGeleBolunen)
        basic.showString("?")
        basic.pause(500)
        basic.clearScreen()
        if (rastGeleBolunen % rastGeleBolen == 0 && input.buttonIsPressed(Button.A)) {
            basic.showIcon(IconNames.Yes)
            basic.clearScreen()
            Score += 1
        } else if (rastGeleBolunen % rastGeleBolen == 0 && !(input.buttonIsPressed(Button.A))) {
            basic.showIcon(IconNames.No)
            Flag = false
        } else if (rastGeleBolunen % rastGeleBolen != 0 && input.buttonIsPressed(Button.A)) {
            basic.showIcon(IconNames.No)
            basic.clearScreen()
            Flag = false
        }
    }
})
