import pyautogui
from pyautogui import locateOnScreen as LoS
from time import sleep
from datetime import datetime


sleep(3)
while True:

    CUPONS = ['2021ali20', 'AECOMPRA20','alipay20', 'alitec20', 'awintop20', 'chinacupon20',
              'cupomvalido20', 'importchina20', 'superdicas20', "tiagolima20", "SANTOSTEC20", 'joaoali20']

    TOTAL = LoS('total.png', confidence=0.8)
    if TOTAL:
        for cupom in CUPONS:
            print(cupom)
            texto = LoS('text.png', confidence=0.8)
            if texto is None :
                z, t = pyautogui.locateCenterOnScreen('fazer.png', confidence=0.8)
                print(datetime.now() + " Foi aplicado o Cupom: " + cupom)   
                pyautogui.click(z, t)
                break

           
            x, y = pyautogui.locateCenterOnScreen('text.png', confidence=0.8)
            pyautogui.click(x, y)
            sleep(1)
            pyautogui.write(cupom)
            sleep(1.5)

            z, t = pyautogui.locateCenterOnScreen(
            'utilizar.png', confidence=0.8)
            pyautogui.click(z, t)

            sleep(2)
           
    else:
        break 