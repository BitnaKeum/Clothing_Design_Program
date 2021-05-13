# Clothing_Design_Program
GAN based clothing design program

## USAGE
* vscode에서 [ctrl + shift + p] -> python interpreter 검색 후 가상환경 선택(Mask_RCNN, StarGAN모델 동시 구동환경)
* 데이터베이스 계정 별도 수정 필요
* MySQL 테이블 생성 (Clothes_Design/create_table.sql 파일 참조)
* Clothes_Design/ 폴더에서 [node app] 명령어 실행
* http://localhost:3003/auth/login 에서 회원가입, 로그인 후 구동

---
## 디렉토리 정보
* \Clothes_Design\public\uploads : input 이미지 디렉토리
* \Clothes_Design\public\mask_output : Mask_RCNN모델 결과 사진 저장 디렉토리
* \Clothes_Design\public\gan_output : StarGAN모델 결과 사진(6장) 저장 디렉토리
* \Clothes_Design\public\match_output : Histogram Matching 적용 결과 사진 저장 디렉토리
* \Clothes_Design\public\output : 최종 결과 사진 저장 디렉토리
