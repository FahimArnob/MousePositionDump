import time as t
import pyautogui as pyg

def mouse_dump():
    try:
        c = 1
        f = open('mouserecord.txt', 'a')
        x, y = pyg.position()
        while True:
            f.write("%04d. [%d, %d]\n" % (c, x, y))
            print('Dump successful\n')
            t.sleep(.7)
            print('Timing successful\n')
            c += 1
        f.close()
    except:
        print("HELLO FRIEND, MY SILENT FRIEND :(")

mouse_dump()
