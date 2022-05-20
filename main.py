_F='ESCAPE'

_E='crew.png'

_D='start.png'

_C='S'

_B='join.png'

_A=True

__author__='guest0417'

from airtest.core.api import *

from airtest.cli.parser import cli_setup

from airtest.core.win.win import *

from airtest.aircv import *

import numpy as np,_pytesseract,cv2,traceback,os,sys

flag=_A

ST.FIND_TIMEOUT_TMP=2

ST.FIND_TIMEOUT_TMP=2

testdata_dir_config='--tessdata-dir "'+os.getcwd()+'\\Tesseract-OCR\\tessdata"'

class LoopException(Exception):0

def click(key):print('[LOG] clicked: ',key);key_press(key);sleep(0.1);key_release(key)

def init():

	print('[LOG] initialising...');temp=0	while not exists(Template('6.png',threshold=0.9)):

		temp+=1

		if temp>=10:raise LoopException

		click('6');sleep(0.5)

	temp=0

	while not exists(Template('7.png',threshold=0.9)):

		temp+=1

		if temp>=10:raise LoopException

		click('7');sleep(0.5)

	temp=0

	while not exists(Template('8.png',threshold=0.9)):

		temp+=1

		if temp>=10:raise LoopException

		click('8');sleep(0.5)

	init_speed()

def init_speed():A='W';print('[LOG] speed initialised');key_press(A);sleep(1.0);key_release(A);click(_C);click(_C);click(_C)

def check_crash(text):

	B='D';A='A';global flag;print('[LOG] checking crash')

	if'返'in text or'回'in text or'战'in text or'场'in text or'前'in text or'方'in text or'水'in text or'深'in text or'不'in text or'足'in text or'放'in text or'弃'in text or'载'in text or'具'in text or'倒'in text or'计'in text or'时'in text or'1'in text or'2'in text or'3'in text or'4'in text or'5'in text or'6'in text or'7'in text or'8'in text or'9'in text:

		print('crashing');key_press(_C);sleep(15)

		if flag==_A:key_press(A)

		else:key_press(B)

		sleep(15)

		if flag==_A:key_release(A)

		else:key_release(B)

		key_release(_C);init_speed();flag=not flag

	return _A

def check_target():

	print('[LOG] checking target');temp=0

	while not exists(Template('target.png',threshold=0.9)):

		temp+=1

		if temp>=10:raise LoopException

		click('E')

	return _A

def check_weapon():

	A='LALT';print('[LOG] checking weapon');temp=0

	while not exists(Template('AA.png'))and not exists(Template('secondary.png')):

		temp+=1

		if temp>=10:raise LoopException

		key_press(A);key_press('2');sleep(0.1);key_release('2');key_release(A);key_press(A);key_press('3');sleep(0.1);key_release('3');key_release(A);sleep(0.1);break

	return _A

def start():

	G.DEVICE.set_foreground();temp=0

	while not exists(Template(_D,threshold=0.95)):

		temp+=1

		if temp>=10:raise LoopException

		print('[LOG] awaiting to start a new game...');sleep(5)

	touch(Template(_D))

	if exists(Template(_D,threshold=0.95)):touch(Template(_D,threshold=0.95))

def join():

	G.DEVICE.set_foreground()

	while not exists(Template(_B,threshold=0.95)):sleep(5)

	touch(Template(_B))

	if exists(Template(_B,threshold=0.95)):touch(Template(_B,threshold=0.95))

	print('[LOG] respawned')

def battle(depth):

	A='rtb1.png';G.DEVICE.set_foreground()

	while not exists(Template(_E)):sleep(5)

	while exists(Template(_E,threshold=0.8)):

		G.DEVICE.set_foreground()

		if depth==0:click('Z');print('[LOG] in battle');init_speed();check_weapon();check_target()

		depth+=1;width,height=G.DEVICE.get_current_resolution();screen=G.DEVICE.snapshot();local=aircv.crop_image(screen,(width/5*2,height/2,width/5*3,height/3*2));hsv=cv2.cvtColor(local,cv2.COLOR_BGR2HSV);lower=np.array([0,43,46]);higher=np.array([10,255,255]);mask=cv2.inRange(hsv,lower,higher);mask=mask*255;text=_pytesseract.image_to_string(mask,lang='chi_sim');print('[LOG] text acquired:',text);check_crash(text)

		if exists(Template('continue.png')):click(_F)

	print('[LOG] not in battle');G.DEVICE.set_foreground();sleep(5.0)

	if exists(Template('rtb.png',threshold=0.95))or exists(Template(_B,threshold=0.95)):

		temp=0

		while not exists(Template(A,threshold=0.9)):

			temp+=1

			if temp>=10:raise LoopException

			G.DEVICE.set_foreground();click(_F)

		touch(Template(A,threshold=0.9))

		if exists(Template(A,threshold=0.95)):touch(Template(A,threshold=0.95))

		click('LEFT');click('ENTER');quit()

	else:quit()

	print('[LOG] battle quited')

def quit():

	B='close.png';A='confirm.png';temp=0

	while not exists(Template(_D,threshold=0.95)):

		G.DEVICE.set_foreground();temp+=1

		if temp>=20:raise LoopException

		if exists(Template(A,threshold=0.9)):print('[LOG] confirm');touch(Template(A,threshold=0.9))

		elif exists(Template(B,threshold=0.8,rgb=_A)):print('[LOG] close');touch(Template(B,threshold=0.8,rgb=_A))

		elif exists(Template('research.png',threshold=0.9)):print('[LOG] research');touch(Template('research1.png',threshold=0.6))

		else:click(_F);sleep(3.0)

def main():

	G.DEVICE.set_foreground()

	if exists(Template(_B,threshold=0.95)):join();depth=0;battle(depth)

	elif exists(Template(_E)):depth=0;battle(depth)

	else:0

	while _A:quit();start();join();depth=0;battle(depth)

if __name__=='__main__':

	try:

		if not cli_setup():auto_setup(__file__,logdir=os.getcwd()+'/log',devices=['Windows:///?title_re=War Thunder*'])

		G.DEVICE.set_foreground();print('[LOG] script started')

		while _A:

			try:main()

			except (AttributeError,TargetNotFoundError,LoopException):pass

	except Exception as e:print('[Exception] ',e);traceback.print_exc()

	os.system('pause')
