# 라즈베리파이를 사용한 자율주행 RC카

스스로 라인을 따라 주행할 수 있는 자율주행 RC카를 구현해보았다. 기울기를 이용한 자
율주행 방법을 사용하였다. 라인의 기울기를 측정하기 위해서 openCV 기술을 이용하였다.
RC카를 제어하기 위해 하드웨어로 라즈베리파이를 사용하였다. 주행을 하기위한 DC모터를
모터드라이버를 사용했다. RC카를 제어하기 위한 코드들은 Python을 이용하여 제작했다. 적
당한 기울기 값에 방향전환을 하기위해 코드의 값을 바꿔서 코드를 시도해본다. 제작된 RC카
는 직진주행 뿐만 아니라 기울기를 이용한 방향전환이 가능하다.

## 1. 설계 과정
![image](https://user-images.githubusercontent.com/97801319/211216285-217638d2-d903-476e-ba45-8343e2bc74b7.png)
![image](https://user-images.githubusercontent.com/97801319/211216308-cc9acb5a-da32-45c2-aff5-a0f7bac5e4f8.png)

## 2. 라인 색상 추출
![image](https://user-images.githubusercontent.com/97801319/211216337-f78e6977-0892-4847-8256-01daf9a2be40.png)
![image](https://user-images.githubusercontent.com/97801319/211216339-32b8b5ac-2ad8-4420-bbff-9ce2b1e986de.png)

## 3. Cv2.HoughLinesP( ) -> 선분 그리기
![image](https://user-images.githubusercontent.com/97801319/211216450-da7ca547-57d6-4044-8e14-a5c5f95d6198.png)
![image](https://user-images.githubusercontent.com/97801319/211216454-7aa9f366-4224-4763-86fa-1b8ae4782a73.png)

## 4. Mjpg 스트리밍
![image](https://user-images.githubusercontent.com/97801319/211216482-ad12071b-ac2b-4e28-9fce-c132f0b93cd1.png)

## 5. 선분의 기울기 구하기
![image](https://user-images.githubusercontent.com/97801319/211216925-ad159d15-bae1-4155-a049-53f948d5d282.png)
y 좌표로 x 좌표의 시작과 끝을 구한다음 x의 증가량과 y의 증가량으로 전체적인 기울기를 구함

## 6. 주행 방향 판단
![image](https://user-images.githubusercontent.com/97801319/211216961-ce54c9c4-d9cc-43ea-8b56-30c4327b2e4b.png)
pwm.ChangeDutyCycle([duty cycle]) 함수를 사용하면, 0%~100% 사이의 [duty cycle] 값으로 바꿀 수 있다.

## 7. 주행 결과
https://user-images.githubusercontent.com/97801319/211217013-c2963108-c83a-4c4d-b65b-ce2ad915ccb4.mp4

