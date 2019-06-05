# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time



'''使用2块L298N驱动控制4个直流电机
前轮驱动：18-ENDA, 22-ENDB, 11-左前前, 12-左前后, 16-右前前, 29-右前后'''
# 初始化设置引脚输出
def init():
    #        GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)



# 所有引脚置低电平，用于复位、停止运行的功能
def reset():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(29, GPIO.LOW)



# 左前轮向前转
def front_left_back():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)


def front_right_forward():
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(29, GPIO.LOW)

def front_left_forward():
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)


def front_right_back():
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(29, GPIO.HIGH)

def forward():
    reset()
    front_left_forward()
    front_right_forward()


def yuandi():
    reset()
    front_right_back()
    front_left_forward()


def back():
    reset()
    front_left_back()
    front_right_back()



def front_left_turn():
    reset()
    front_right_forward()


def front_right_turn():
    reset()
    front_left_forward()
    rear_left_forward()

def stop():
    reset()


if __name__ == "__main__":
    init()
    try:
        while True:
            reset()
            forward()
            #	reset()
            #	front_left_forward()
            time.sleep(5)
    except:
        GPIO.cleanup()
    while(1):
            reset()
            #front_left_forward()
            #front_right_forward()
            forward()
            time.sleep(30)
            back()
            time.sleep(30)
            # front_left_turn()
            # time.sleep(1)
            # front_right_turn()
            # time.sleep(1)
            stop()
            GPIO.cleanup()
