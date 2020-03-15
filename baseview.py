# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

class BaseView():
    def __init__(self,driver):
        self.driver = driver
        self.windowsize = self.get_window()

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def get_window(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width,height

    def swipe_screen(self,X1,Y1,X2,Y2,time):
        # size = self.get_window()
        # x1 = int(size[0] * X1)
        # y1 = int(size[1] * Y1)
        # x2 = int(size[0] * X2)
        # y2 = int(size[1] * Y2)
        x1 = int(self.windowsize[0] * X1)
        y1 = int(self.windowsize[1] * Y1)
        x2 = int(self.windowsize[0] * X2)
        y2 = int(self.windowsize[1] * Y2)
        self.driver.swipe(start_x=x1,start_y=y1,end_x=x2,end_y=y2,duration=time)

    def tap(self,X,Y):
        tap_point = TouchAction(self.driver)
        tap_point.tap(x=X,y=Y)

    # 获取元素的坐标
    def elment_location(self,*loc):
        el_location = self.find_element(*loc).location
        return el_location