## GAN 기반 의류 디자인 프로그램



### Result

![image](https://user-images.githubusercontent.com/37769713/139530362-ef455ec9-f204-472c-ad48-50e74e49b07f.png)

- 시연 영상 : https://www.youtube.com/watch?v=MJOZAQpv04M



<br>


### 사용법
* vscode에서 [ctrl + shift + p] -> python interpreter 검색 후 가상환경 선택(Mask_RCNN, StarGAN모델 동시 구동환경)
* 데이터베이스 계정 별도 수정 필요
* MySQL 테이블 생성 (/Clothing_Design_Program/Clothes_Design_service/create_table.sql 파일 참조)
* /Clothing_Design_Program/Clothes_Design_service 폴더에서 [node app] 명령어 실행
* http://localhost:3003/auth/login 에서 회원가입, 로그인 후 구동

<br>

### 디렉토리 정보
* \Clothes_Design\public\uploads : input 이미지 디렉토리
* \Clothes_Design\public\mask_output : Mask_RCNN모델 결과 사진 저장 디렉토리
* \Clothes_Design\public\gan_output : StarGAN모델 결과 사진(6장) 저장 디렉토리
* \Clothes_Design\public\match_output : Histogram Matching 적용 결과 사진 저장 디렉토리
* \Clothes_Design\public\output : 최종 결과 사진 저장 디렉토리

<br><br>

### Overview 

- System Overview

![image](https://user-images.githubusercontent.com/37769713/139530668-51b79759-3e4d-48db-9a6e-e792c21260e9.png)

<br>

- 설계도

![image](https://user-images.githubusercontent.com/37769713/139529004-f9f58fc5-044f-43be-8f09-d7477e4f03b3.png)

<br>

- Improved StarGAN Architecture

![image](https://user-images.githubusercontent.com/37769713/139529049-715cf15e-4ee4-4ccf-ac04-9bc5a9a7303b.png)

