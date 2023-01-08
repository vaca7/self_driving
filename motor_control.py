import RPi.GPIO as GPIO
import time
import threading
from socket import *

GPIO.setmode(GPIO.BCM)  # pin모드 사용
GPIO.setwarnings(False)  # 경고는 제외

# 핀번호

aEnable = 0
bEnable = 26
leftPwm = 5
rightPwm = 6
frontPwm = 13
backPwm = 19

GPIO.setup(aEnable, GPIO.OUT)  # 아웃풋 모드 전부 변경
GPIO.setup(bEnable, GPIO.OUT)
GPIO.setup(leftPwm, GPIO.OUT)  # 아웃풋 모드 전부 변경
GPIO.setup(rightPwm, GPIO.OUT)
GPIO.setup(frontPwm, GPIO.OUT)
GPIO.setup(backPwm, GPIO.OUT)
GPIO.output(aEnable, True)
GPIO.output(bEnable, True)

leftPWM = GPIO.PWM(leftPwm, 50)  # 소ㅓㄱ도를 결정하기위해 pwm으로 ㄱ설정
rightPWM = GPIO.PWM(rightPwm, 50)
frontPWM = GPIO.PWM(frontPwm, 50)
backPWM = GPIO.PWM(backPwm, 50)


def back(speed):  # 앞으로 가는함수
    leftPWM.ChangeDutyCycle(speed)  # 듀티비 변경
    rightPWM.ChangeDutyCycle(0)
    frontPWM.ChangeDutyCycle(speed)
    backPWM.ChangeDutyCycle(0)


def go(speed):  # 전진과 반대로 ㅈ동작
    leftPWM.ChangeDutyCycle(0)
    rightPWM.ChangeDutyCycle(speed)
    frontPWM.ChangeDutyCycle(0)
    backPWM.ChangeDutyCycle(speed)


def stop():  # 정지
    leftPWM.ChangeDutyCycle(0)
    rightPWM.ChangeDutyCycle(0)
    frontPWM.ChangeDutyCycle(0)
    backPWM.ChangeDutyCycle(0)


def right(speed):  # 왼쪽
    leftPWM.ChangeDutyCycle(50)
    rightPWM.ChangeDutyCycle(0)
    frontPWM.ChangeDutyCycle(0)
    backPWM.ChangeDutyCycle(speed)


def left(speed):  # 오른쪽

    leftPWM.ChangeDutyCycle(0)
    rightPWM.ChangeDutyCycle(speed)
    frontPWM.ChangeDutyCycle(50)
    backPWM.ChangeDutyCycle(0)


if __name__ == '__main__':
    go(60)
    time.sleep(0.3)
    back(60)
    time.sleep(0.3)
    right(100)
    time.sleep(3)
    left(100)
    time.sleep(3)
    stop()