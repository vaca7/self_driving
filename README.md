# 라즈베리파이를 사용한 자율주행 RC카

스스로 라인을 따라 주행할 수 있는 자율주행 RC카를 구현해보았습니다. 기울기를 이용한 자
율주행 방법을 사용하였습니다. 라인의 기울기를 측정하기 위해서 openCV 기술을 이용하였습니다.
RC카를 제어하기 위해 하드웨어로 라즈베리파이를 사용하였습니다. 주행을 하기위한 DC모터를
모터드라이버를 사용했습니다. RC카를 제어하기 위한 코드들은 Python을 이용하여 제작했습니다. 적
당한 기울기 값에 방향전환을 하기위해 코드의 값을 바꿔서 코드를 시도해보았습니다. 제작된 RC카
는 직진주행 뿐만 아니라 기울기를 이용한 방향전환이 가능합니다.

## 1. 설계 과정
파이캠을 이용하여 라인색상 추출 후 직선 검출을 합니다. 그 직선들의 기울기를 실시간으로 검출해주고 그 기울기를 이용해 방향을 판단합니다. 마지막으로 모터드라이버로 dc모터를 제어하여 rc카 주행을 하게 됩니다. 
![image](https://user-images.githubusercontent.com/97801319/211216285-217638d2-d903-476e-ba45-8343e2bc74b7.png)
<img src="https://user-images.githubusercontent.com/97801319/211216308-cc9acb5a-da32-45c2-aff5-a0f7bac5e4f8.png" width="500">

## 2. 라인 색상 추출
첫번째로 라인의 특정 색상을 추출해 줍니다. 특정 색상을 추출할 수 있는 inrange 함수를 이용하였습니다. 제가 만든 라인은 검정색으로 검정색을 추출해준 모습입니다. 검정색을 추출한 사진은 p.jpg로 저장해준 모습입니다.
<img src="https://user-images.githubusercontent.com/97801319/211216337-f78e6977-0892-4847-8256-01daf9a2be40.png" width="500">
<img src="https://user-images.githubusercontent.com/97801319/211216339-32b8b5ac-2ad8-4420-bbff-9ce2b1e986de.png" width="250">

## 3. Cv2.HoughLinesP( ) -> 선분 그리기
이제 선분을 그려줍니다. 허프라인 함수는 사진에서 선분을 추출해줄 수 있는 함수입니다. 정확성을 위해 캐니 함수로 윤곽선을 추출하고 허프라인 함수로 라인을 검출한 후 라인 함수를 사용해서 원본 frame2에 선분을 그려줍니다.
<img src="https://user-images.githubusercontent.com/97801319/211216450-da7ca547-57d6-4044-8e14-a5c5f95d6198.png" width="500">
<img src="https://user-images.githubusercontent.com/97801319/211216454-7aa9f366-4224-4763-86fa-1b8ae4782a73.png" width="500">

## 4. Mjpg 스트리밍
자유롭게 화면을 확인할 수 있게 mjpg 스트리밍 설정을 해주었습니다. 아까 원본에 기울기가 나타나게한 사진을 실시간으로 갱신하여 스트리밍을 해줍니다. 스트리밍 모습입니다.

<img src="https://user-images.githubusercontent.com/97801319/211216482-ad12071b-ac2b-4e28-9fce-c132f0b93cd1.png" width="500">

## 5. 선분의 기울기 구하기
위에서 허프라인 함수로 선분을 나타내주었고 그 선분의 기울기를 구합니다. y좌표로 x 좌표의 시작과 끝을 구한 다음 x의 증가량과 y의 증가량으로 전체적인 기울기를 구해줍니다. 

<img src="https://user-images.githubusercontent.com/97801319/211216925-ad159d15-bae1-4155-a049-53f948d5d282.png" width="500">

## 6. 주행 방향 판단
구한 기울기를 이용해 주행 방향을 판단해줍니다. 이 코드에서는 count를 이용해서 15까지 어떤 선분도 검출되지 않으면 멈추게 해주었습니다. 그리고 디렉션이 -6보다 작으면 우회전 6보다 크면 좌회전을 해주고 나머지는 직진하게 코드를 설정해 주었습니다. 여기서 나오는 직진, 우회전, 좌회전은 이와 같이 함수로 만들어 주었습니다. 여기서 사용하는 체인지 두티사이클 함수를 사용하면 0퍼에서 100퍼 사이의 두티사이클 값으로 바꿀 수 있게됩니다. 

<img src="https://user-images.githubusercontent.com/97801319/211216961-ce54c9c4-d9cc-43ea-8b56-30c4327b2e4b.png" width="500">

## 7. 주행 결과
https://user-images.githubusercontent.com/97801319/211217013-c2963108-c83a-4c4d-b65b-ce2ad915ccb4.mp4

