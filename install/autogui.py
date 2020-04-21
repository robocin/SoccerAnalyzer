import pyautogui as pag
import time

pag.hotkey('ctrl','alt','t')
#pag.typewrite('bash\n')
time.sleep(5)
pag.typewrite('source activate analyzer\n', interval=0.1)
pag.typewrite('./install_2.sh\n')
pag.typewrite('./install_3.sh\n')
