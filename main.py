def on_button_pressed_b():
    global Score
    basic.show_number(Score)
    Score = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

rastGeleBolunen = 0
Score = 0
Flag = True
Score = 0
rastGeleBolen = randint(2, 9)
basic.show_number(rastGeleBolen)
basic.pause(500)
basic.clear_screen()
basic.pause(200)

def on_forever():
    global rastGeleBolunen, Score, Flag
    if Flag:
        rastGeleBolunen = randint(10, 99)
        basic.show_number(rastGeleBolunen)
        basic.show_string("?")
        basic.pause(500)
        basic.clear_screen()
        if rastGeleBolunen % rastGeleBolen == 0 and input.button_is_pressed(Button.A):
            basic.show_icon(IconNames.YES)
            basic.clear_screen()
            Score += 1
        elif rastGeleBolunen % rastGeleBolen == 0 and not (input.button_is_pressed(Button.A)):
            basic.show_icon(IconNames.NO)
            Flag = False
        elif rastGeleBolunen % rastGeleBolen != 0 and input.button_is_pressed(Button.A):
            basic.show_icon(IconNames.NO)
            basic.clear_screen()
            Flag = False
basic.forever(on_forever)
