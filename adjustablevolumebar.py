from gpiozero import *
up=Button(17)
dwn=Button(27)

import math

def roundup(x):
    return math.ceil(x / 10.0) * 10
import rpi_lcd as lcd
import alsaaudio
control=alsaaudio.Mixer()
currentvol=roundup(control.getvolume()[0])

if currentvol >= 80:
    currentvol=80
vol=currentvol
count=0
screen=lcd.LCD()
MAX_SCREEN_DIGITS=16
def getRemaining(volume: int):
    global MAX_SCREEN_DIGITS
    getremaining={0:0, 10:2, 20:4, 30:6, 40:8, 50:10, 60:12, 70:14, 80:16}
    return MAX_SCREEN_DIGITS-getremaining[volume]


def getCurrentVolume(volume: int):
    global count
    getremaining={0:0, 10:2, 20:4, 30:6, 40:8, 50:10, 60:12, 70:14, 80:16}
    getvolumes={0:0*"#", 10:2*"#", 20:4*"#", 30:6*"#", 40:8*"#", 50:10*"#", 60:12*"#", 70:14*"#", 80:16*"#"}
    count=getremaining[volume]
    if volume != 0:
        return getvolumes[volume]
    elif volume == 0:
        return getvolumes[volume]

screen.text(f"Volume: {vol}", 1)

remaining=getRemaining(currentvol)
screen.text(getCurrentVolume(currentvol)+remaining*".", 2)

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
        sys.exit() # End of prog
