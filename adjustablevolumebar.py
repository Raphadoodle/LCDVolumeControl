from gpiozero import *
import math

def roundup(x): #Will be used in a future update
    return math.ceil(x / 10.0) * 10
import rpi_lcd as lcd
import alsaaudio
control=alsaaudio.Mixer()
control.setvolume(0)#Reset volume to 1
up=Button(17)
dwn=Button(27)
vol=0

screen=lcd.LCD()


screen.text(f"Volume: {vol}", 1)
MAX_SCREEN_DIGITS=16
count=0
remaining=MAX_SCREEN_DIGITS-count
screen.text(count*"#"+remaining*".", 2)

MAX_VOL=80


while True:
    try:
        if up.is_pressed:
            if count>=MAX_SCREEN_DIGITS and vol>=MAX_VOL:
                count=MAX_SCREEN_DIGITS
                vol=MAX_VOL
                remaining=MAX_SCREEN_DIGITS-count
                screen.text(count*"#"+remaining*".", 2)
            elif not(count>=MAX_SCREEN_DIGITS and vol>=MAX_VOL):
                count+=1
                vol+=5
                screen.text(f"Volume: {vol}", 1)
                control.setvolume(vol)
                remaining=MAX_SCREEN_DIGITS-count
                screen.text(count*"#"+remaining*".", 2)
        if dwn.is_pressed:
                if count<=0 and vol<=0:
                    count=0
                    vol=0
                    remaining=MAX_SCREEN_DIGITS-count
                    screen.text(count*"#"+remaining*".", 2)
                elif not(count<=0 and vol<=0):
                    count-=1
                    vol-=5
                    screen.text(f"Volume: {vol}", 1)
                    control.setvolume(vol)
                    remaining=MAX_SCREEN_DIGITS-count
                    screen.text(count*"#"+remaining*".", 2)
    except KeyboardInterrupt:
        screen.clear()
        print("\n\nStopped")
        import sys
        sys.exit()



