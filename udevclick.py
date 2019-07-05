#!/usr/bin/python36

import os
import cv2

import socket 

s = socket.socket()
ip  = "192.168.43.115"
port = 5
s.bind((ip,port))
s.listen(5)
session , addr = s.accespt()
ch = session.recv(100).decode()

cap=cv2.VideoCapture(0)
ret, photo=cap.read()
cv2.imwrite("/root/USBClick.png", photo)
cap.release()
os.system("ansible-playbook /root/Desktop/project/udev_mail.yml")


