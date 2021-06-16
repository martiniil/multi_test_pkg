#!/usr/bin/env python3

PKG = 'multi_test_pkg'
SLEEP_TIME_PARAM = '~sleep_time'

import rospy
import sys
import unittest


class MyRosTest(unittest.TestCase):
    def displayCurrentTime(self, place="MyRosTest"):
        now = rospy.get_rostime()
        rospy.logwarn("Current time[s] (%s): %i", place, now.secs)

    def getSleepTime(self):
        self.assertTrue(rospy.has_param(SLEEP_TIME_PARAM))
        self.sleep_time = rospy.get_param(SLEEP_TIME_PARAM)

    def setUp(self):
        self.displayCurrentTime("MyRosTest.setUp")
        self.getSleepTime()

    def tearDown(self):
        self.displayCurrentTime("MyRosTest.tearDown")

    def test_nothing_just_sleep(self):
        rospy.sleep(self.sleep_time)
        self.assertTrue(True)


if __name__ == '__main__':
    import rostest

    rospy.init_node('my_rostest')
    rostest.rosrun(PKG, 'my_rostest', MyRosTest)
