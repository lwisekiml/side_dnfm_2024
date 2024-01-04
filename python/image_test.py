# 참고 : https://re-code-cord.tistory.com/entry/OpenCV-Template-Matching-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
import cv2
import numpy as np
import os

img_rgb = cv2.imread('test.jpg')

for (root, directories, files) in os.walk("data/Auxiliary_equipment_new"):
    for file in files:
        file_path = os.path.join(root, file)
        print("file_path : ", file_path)

        template = cv2.imread(file_path)
        h, w = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .76
        loc = np.where(res >= threshold)

        i = 0
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            i = i + 1
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

cv2.imshow("img_rgb", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
