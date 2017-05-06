"""
Main idea is now to deal with being given a list

we need to dislpay the info 
move lines up or down

scroll the current line

keep a cursor to show current line

return the the current element in list? no this code only operates from the list

refresh time on changes



"""

import Adafruit_CharLCD as LCD
\x01

def render_list(display_list, Adafruit_CharLCD):
    lcd = Adafruit_CharLCD
    lcd.clear()
    cols = Adafruit_CharLCD._lines
    message = ""
    space = "-"
    pointer = LCD.createChar(1,[31,19,29,30,29,19,31,31])
    divider = "\n"
    for each in display_list[0:cols]:
	print each
        message = message+pointers+each+divider
	print message
    lcd.message(message)
    lcd.set_cursor(0,1)
    lcd.blink(True)

