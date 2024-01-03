# 참고 : https://re-code-cord.tistory.com/entry/OpenCV-Template-Matching-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
import cv2
import numpy as np
import os

# 보조장비
atena = 0
bulsadan = 0
ekey = 0
gomyung = 0
hela = 0
jiben = 0
nibe = 0
sigan = 0

# 확인 하고 싶은 스샷
image = cv2.imread('aa.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for (root, directories, files) in os.walk("data/Auxiliary_equipment"):
    # 폴더 전체 경로
    for d in directories:
        d_path = os.path.join(root, d)
        # print("d_path : ", d_path) # data\Auxiliary_equipment\atena.jpg

    # 파일 전체 경로
    for file in files:
        file_path = os.path.join(root, file)
        print("file_path : ", file_path)
        
        # 포함 되어있는지 확일할 이미지(data)
        template = cv2.imread(file_path, 0) # template = cv2.imread('data/bosojangbi.jpg', 0)
        w, h = template.shape[::-1]

        result = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.75 # 임계치 설정
        box_loc = np.where(result >= threshold) # 임계치 이상의 값들만 사용

        flag = 0

        for box in zip(*box_loc[::-1]):
            flag = 1
            print("flag: ", file_path)
            startX, startY = box
            endX, endY = startX + w, startY + h
            cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 10)
        
cv2.imwrite('result.jpg', image)


# # 확인 하고 싶은 스샷
# image = cv2.imread('aa.jpg')
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # 비교할 장비(data)
# # template = cv2.imread('data/bosojangbi.jpg', 0)
# template = cv2.imread('data/Auxiliary_equipment/ekey.jpg', 0)
# w, h = template.shape[::-1]
# result = cv2.matchTemplate(image_gray, template, cv2.TM_CCOEFF_NORMED)
# threshold = 0.75 # 임계치 설정
# box_loc = np.where(result >= threshold) # 임계치 이상의 값들만 사용
# flag = 0
# for box in zip(*box_loc[::-1]):
#     flag = 1
#     # print("flag: ", flag)
#     startX, startY = box
#     endX, endY = startX + w, startY + h
#     cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 10)

# cv2.imwrite('result.jpg', image)
