#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

import termios, sys, os
#import termios, TERMIOS, sys, os
TERMIOS = termios

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
            c = os.read(fd, 1)
    finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


def talker():
    pub = rospy.Publisher('motor_command', String, queue_size=10)
    rospy.init_node('locomotion_input', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

	s = ''
	while 1:
		c = getkey()
		if c == '\n':     ## break on a Return/Enter keypress
			break
		#print 'got', c
		s = c
		print(s)
	
		#rospy.loginfo(s)
		pub.publish(s)
		rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



