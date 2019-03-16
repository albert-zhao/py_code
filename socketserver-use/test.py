import traceback
import time


while True:
	try:
		a = 8//0
	except:
		traceback.print_exc()
	print('here')
	time.sleep(1)
