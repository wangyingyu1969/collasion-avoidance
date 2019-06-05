import RPi.GPIO as GPIO
import time
import thread

speed_in = 7
GPIO.setmode( GPIO.BOARD)
GPIO.setup(speed_in,GPIO.IN)


cycle = 0
t1 = time.time()
def test_speed():
    while True:
        while GPIO.input(speed_in):
            pass
            print("0")
        while not GPIO.input(speed_in):
            pass
            print ("1")
        t2 = time.time()
        cur_speed = cycle / (t2 - t1)
        print ("speed %f cm/s"%cur_speed )
        cycle += 1
	
if __name__=="__main__":


try:
#thread.start_new_thread(test_speed)
    test_speed()
#time.sleep(3)
except KeyboardInterrupt:
    GPIO.cleanup()