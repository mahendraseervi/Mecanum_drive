#!/usr/bin/env python
import rospy
import RPi.GPIO as GPIO
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Motor_fl_a = 23        #fl (front left)
Motor_fl_b = 24
Motor_fl_en = 25

Motor_fr_a = 21        #fr (front right)
Motor_fr_b = 20

Motor_br_a = 5       #br (back right)
Motor_br_b = 6

Motor_bl_a = 13     #bl (back left)
Motor_bl_b = 19


GPIO.setup(Motor_fr_a, GPIO.OUT)
GPIO.setup(Motor_fr_b, GPIO.OUT)
GPIO.setup(Motor_fl_a, GPIO.OUT)
GPIO.setup(Motor_fl_b, GPIO.OUT)
GPIO.setup(Motor_br_a, GPIO.OUT)
GPIO.setup(Motor_br_b, GPIO.OUT)
GPIO.setup(Motor_bl_a, GPIO.OUT)
GPIO.setup(Motor_bl_b, GPIO.OUT)

GPIO.setup(Motor_fl_en, GPIO.OUT)

p = GPIO.PWM(Motor_fl_en,100)
p.start(0)
a = 10


def callback(msg):
    # rospy.loginfo("Pose2D Components: [%f, %f, %f]"%(msg.x, msg.y, msg.theta))
    x_value = msg.x
    y_value = msg.y

    theta_value = msg.theta * (360 / (2 * 3.1415))
    # print(theta_value)

    # if(value > (theta_value)):
    #     print("clock wise")
    #       # clock_rotate()
    #
    # elif(value < (theta_value)):
    #     print("anti clock wise")
    #     # anticlock_rotate()
    #
    # else:
    #     stop()
    # # break


# def callback2(data):
    # rospy.loginfo("Callback2 heard %s",data.data)
    # print(data.data)
    # value = data.data
    # print(value)



def listener():
    rospy.init_node('receive_mtr_move', anonymous=False)
    rospy.Subscriber("/pose2d", Pose2D, callback)

    # rospy.Subscriber("/motor_command", String, callback2)
    # spin() simply keeps python from exiting until this node is stopped
    # print("testing")
    rospy.spin()


def move_front():#(fl,fr,bl,br)=(1,1,1,1)
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
    p.ChangeDutyCycle(a)
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
