def on_button_pressed_a():
    global currentDirection, currentDirectionY
    if currentDirection == NorthX and currentDirectionY == NorthY:
        currentDirection = EastX
        currentDirectionY = EastY
        basic.show_string("E")
    elif currentDirection == EastX and currentDirectionY == EastY:
        currentDirection = SouthX
        currentDirectionY = SouthY
        basic.show_string("S")
    elif currentDirection == SouthX and currentDirectionY == SouthY:
        currentDirection = WestX
        currentDirectionY = WestY
        basic.show_string("W")
    elif currentDirection == WestX and currentDirectionY == WestY:
        currentDirection = NorthX
        currentDirectionY = NorthY
        basic.show_string("N")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global currentDirection, currentDirectionY
    if currentDirection == NorthX and currentDirectionY == NorthY:
        currentDirection = WestX
        currentDirectionY = WestY
        basic.show_string("W")
    elif currentDirection == WestX and currentDirectionY == WestY:
        currentDirection = SouthX
        currentDirectionY = SouthY
        basic.show_string("S")
    elif currentDirection == SouthX and currentDirectionY == SouthY:
        currentDirection = EastX
        currentDirectionY = EastY
        basic.show_string("E")
    elif currentDirection == EastX and currentDirectionY == EastY:
        currentDirection = NorthX
        currentDirectionY = NorthY
        basic.show_string("N")
input.on_button_pressed(Button.B, on_button_pressed_b)

heading = 0
currentDirectionY = 0
currentDirection = 0
EastY = 0
EastX = 0
WestY = 0
WestX = 0
SouthY = 0
SouthX = 0
NorthY = 0
NorthX = 0
NorthX = 280
NorthY = 360
SouthX = 135
SouthY = 225
WestX = 255
WestY = 315
EastX = 45
EastY = 135
currentDirection = NorthX
currentDirectionY = NorthY
while True:
    heading = input.compass_heading()
    if heading >= currentDirection and heading <= currentDirectionY:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
        music.play(music.string_playable("C5 C5 C5 - - - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
