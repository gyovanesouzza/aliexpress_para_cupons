import pyautogui
from pyautogui import locateOnScreen as LoS
from time import sleep

try:
    sleep(10)
    while True:

        CUPONS = ['2021ali20', 'AECOMPRA20', 'alipay20', 'alitec20', 'awintop20', 'besmart20', 'chinacupon20',
              'cupomvalido20', 'importchina20', 'sav20', 'superdicas20', "tiagolima20", "SANTOSTEC20", 'joaoali20']

        TOTAL = LoS('total.png', confidence=0.8)
        if TOTAL:
            for cupom in CUPONS:
                print(cupom)
                sleep(1)

                x, y = pyautogui.locateCenterOnScreen('text.png', confidence=0.8)
                pyautogui.click(x, y)
                pyautogui.write(cupom)
                sleep(2)
                z, t = pyautogui.locateCenterOnScreen(
                'utilizar.png', confidence=0.8)
                pyautogui.click(z, t)
                sleep(2)

                if LoS('utilizar.png', confidence=0.8) is None:
                    break

        else:
            break
    z, t = pyautogui.locateCenterOnScreen('fazer.png', confidence=0.8)
    pyautogui.click(z, t)
except :
    print("Tire screeshot dos botões novamente")
