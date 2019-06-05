import RPi.GPIO as GPIO
import time

distance = 0
ultrasound_trig = 7
ultrasound_echo = 13


def init():
    #	global distance
    global ultrasound_trig
    ultrasound_trig = 7
    global ultrasound_echo
    ultrasound_echo = 13
    #	GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(13, GPIO.IN)
    print("sound init finish")


def checkdist():
    global distance
    global ultrasound_trig
    global ultrasound_echo
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.000015)
    #	print ("begin test")
    try:
        GPIO.output(7, GPIO.LOW)
        # print ("test 1")
        while not GPIO.input(13):
            pass
            #	print ("stage 1")
            t1 = time.time()
        #   print ("t1: %0.2f" % t1)
        while GPIO.input(13):
            pass
        #	print ("stage 2")
        t2 = time.time()
        # print ("t2: %0.2f" % t2)
        distance = (t2 - t1) * 340 / 2
        #	print (distance)
        time.sleep(0.000015)
    except Exception:
        print(e)
        GPIO.cleanup()


if __name__ == "__main__":
    try:
        init()
        #	global distance
        while True:
            print("Distance: %0.2f m" % distance)
            print("Distance22: %0.2f m" % checkdist())
            time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
