import pyautogui
import win32gui
import imutils
import cv2
import audioop
import numpy as np 
import time 
import pyaudio
import sys
import win32com.client
import win32api, win32con
from datetime import datetime 
import pandas as pd 


class Fishy:
    def __init__(self):
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.x = None
        self.y = None
        while True: 
            self.start_fishing() 

    def click(self):
        win32api.SetCursorPos((int(self.x),int(self.y)))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,int(self.x),int(self.y),0,0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,int(self.x),int(self.y),0,0)
        time.sleep(1)

    def capture_wow(self,window_title=None):
        if window_title:
            hwnd = win32gui.FindWindow(None, window_title)
            if hwnd:
                win32gui.SetForegroundWindow(hwnd)
                x, y, x1, y1 = win32gui.GetClientRect(hwnd)
                x, y = win32gui.ClientToScreen(hwnd, (x, y))
                x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
                im = pyautogui.screenshot(region=(x, y, x1, y1))
                return im
            else:
                print('Window not found!')
        else:
            im = pyautogui.screenshot()
            return im
    def screenshot(self,window_title=None):
        if window_title:
            hwnd = win32gui.FindWindow(None, window_title)
            if hwnd:
                win32gui.SetForegroundWindow(hwnd)
                x, y, x1, y1 = win32gui.GetClientRect(hwnd)
                x, y = win32gui.ClientToScreen(hwnd, (x, y))
                x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
                im = pyautogui.screenshot(region=(x, y, x1, y1))
                return im
            else:
                print('Window not found!')
        else:
            im = pyautogui.screenshot()
            return im


    def set_coordinates(self):
        method = cv2.TM_SQDIFF_NORMED
        imgg = self.screenshot('World of Warcraft')
        im = np.array(imgg) 
        im = im[:, :, ::-1].copy()
        small_image = cv2.imread('Untitled.png', cv2.IMREAD_UNCHANGED)
        h, w, _ = small_image.shape
        heat_map = cv2.matchTemplate(im, small_image, cv2.TM_CCOEFF_NORMED)
        y, x = np.unravel_index(np.argmax(heat_map), heat_map.shape)
        
        print(x,y)
        self.x = x+w/2 
        self.y = y+h/2 
  
    def cast_fishing(self):
        self.shell.AppActivate('World of Warcraft')
        self.shell.SendKeys(1)

    def start_fishing(self):
        self.cast_fishing()
        self.set_coordinates()
        self.check_blob()


    def check_blob(self):
        blob_moved = False
        prev_x, prev_y = [self.x, self.x, self.x],  [self.y, self.y, self.y] 
        while not blob_moved:
            self.set_coordinates()
            if abs(sum(prev_y)/len(prev_y)-self.y)>3 and abs(sum(prev_x)/len(prev_x)-self.x)<5:               
                blob_moved = True 
            prev_x.pop(0)
            prev_y.pop(0)
            
            prev_x.append(self.x)
            prev_y.append(self.y) 
            if abs(sum(prev_x)/len(prev_x)-self.x)>3:
                self.cast_fishing()
            time.sleep(0.005)
        print('SPLASH')
        self.click() 


a = Fishy() 
