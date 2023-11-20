# 포켓몬 이미지 유사도 구하기
![image](https://github.com/als63tjd68/Finding-Pokemon-Image-Similarity/assets/139251136/f56303c1-9183-4488-9d08-71a12604418f)
pokemon.csv를 df로 지정, 이미지 파일은 포켓몬 이름으로 저장
df의 [Name]에 속하며, 이에 해당하는 이미지 파일이 있다면 돌아감

예를 들어, 'araquanid.jpg' 라는 이미지 파일이 있다면
'araquanid'를 df 리스트에 있는지 체크하고 특징 값을 찾아, 유사한 이미지를 나타냄
