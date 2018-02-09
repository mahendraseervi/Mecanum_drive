#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor_fl_a = 8        #fl (front left) 1
Motor_fl_b = 7
Motor_fl_en = 25

Motor_fr_a = 21        #fr (front right) 2
Motor_fr_b = 20
Motor_fr_en = 16

Motor_bl_a = 13     #bl (back left) 3
Motor_bl_b = 19
Motor_bl_en = 26

Motor_br_a = 10       #br (back right) 4
Motor_br_b =9
Motor_br_en = 11


GPIO.setup(Motor_fr_a, GPIO.OUT)     #direction pins
GPIO.setup(Motor_fr_b, GPIO.OUT)
GPIO.setup(Motor_fl_a, GPIO.OUT)
GPIO.setup(Motor_fl_b, GPIO.OUT)
GPIO.setup(Motor_bl_a, GPIO.OUT)
GPIO.setup(Motor_bl_b, GPIO.OUT)
GPIO.setup(Motor_br_a, GPIO.OUT)
GPIO.setup(Motor_br_b, GPIO.OUT)

GPIO.setup(Motor_fl_en, GPIO.OUT)     # enable pins
GPIO.setup(Motor_fr_en, GPIO.OUT)
GPIO.setup(Motor_br_en, GPIO.OUT)
GPIO.setup(Motor_bl_en, GPIO.OUT)

p1 = GPIO.PWM(Motor_fl_en,100)
p2 = GPIO.PWM(Motor_fr_en,100)
p3 = GPIO.PWM(Motor_bl_en,100)
p4 = GPIO.PWM(Motor_br_en,100)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

a = 5

def callback(data):
    direction = data.data
    print(direction)

    if(direction == "8"):
        move_front()
        # print("front")

    elif(direction == "2"):
        move_back()

    elif(direction == "4"):
       move_left()

    elif(direction == "6"):
        move_right()

    elif(direction == "7"):
        move_front_left()

    elif(direction == "9"):
        move_front_right()

    elif(direction == "1"):
        move_back_left()

    elif(direction == "3"):
        move_back_right()

    elif(direction == "a"):
        anticlock_rotate()

    elif(direction == "s"):
        clock_rotate()

    elif(direction == "5"):
        stop()

    else:
        # print("stop")
        stop()



def listener():
    rospy.init_node('receive_mtr_cmd', anonymous=False)
    rospy.Subscriber("motor_command", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


def move_front():#(fl,fr,bl,br)=(1,1,1,1)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.HIGH)  #1
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.HIGH)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.HIGH)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.HIGH)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("move front")

def move_back():#(fl,fr,bl,br)=(0,0,0,0)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.HIGH)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.HIGH)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.HIGH)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.HIGH)
    print("move back")

def move_left():#(fl,fr,bl,br)=(0,1,1,0)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.HIGH)
    GPIO.output(Motor_fr_a,GPIO.HIGH)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.HIGH)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.HIGH)
    print("move left")

def move_right():#(fl,fr,bl,br)=(1,0,0,1)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.HIGH)
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.HIGH)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.HIGH)
    GPIO.output(Motor_br_a,GPIO.HIGH)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("move right")

def move_front_left():#(fl,fr,bl,br)=(s,1,1,s)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.HIGH)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.HIGH)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("move front left")

def move_front_right():#(fl,fr,bl,br)=(1,s,s,1)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.HIGH)
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.HIGH)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("move front right")

def move_back_left():#(fl,fr,bl,br)=(0,s,s,0)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.HIGH)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.HIGH)
    print("move back left")

def move_back_right():#(fl,fr,bl,br)=(s,0,0,s)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.HIGH)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.HIGH)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("move back right")

def anticlock_rotate():#(fl,fr,bl,br)=(0,1,0,1)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.HIGH)
    GPIO.output(Motor_fr_a,GPIO.HIGH)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.HIGH)
    GPIO.output(Motor_br_a,GPIO.HIGH)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("anticlock rotate")

def clock_rotate():#(fl,fr,bl,br)=(1,0,1,0)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.HIGH)
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.HIGH)
    GPIO.output(Motor_bl_a,GPIO.HIGH)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.HIGH)
    print("clock rotate")

def stop():#(fl,fr,bl,br)=(s,s,s,s)
    p1.ChangeDutyCycle(a)
    p2.ChangeDutyCycle(a)
    p3.ChangeDutyCycle(a)
    p4.ChangeDutyCycle(a)
    GPIO.output(Motor_fl_a,GPIO.LOW)
    GPIO.output(Motor_fl_b,GPIO.LOW)
    GPIO.output(Motor_fr_a,GPIO.LOW)
    GPIO.output(Motor_fr_b,GPIO.LOW)
    GPIO.output(Motor_bl_a,GPIO.LOW)
    GPIO.output(Motor_bl_b,GPIO.LOW)
    GPIO.output(Motor_br_a,GPIO.LOW)
    GPIO.output(Motor_br_b,GPIO.LOW)
    print("move front")



if __name__ == '__main__':
    listener()
