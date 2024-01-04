import cv2
import numpy as np
import os

ae = {"athena" : 0, "bul" : 0, "ekey" : 0, "go" : 0, "hera" : 0, "jiben" : 0, "ni" : 0, "time" : 0}

img_rgb = cv2.imread('test1.jpg')


for (root, directories, files) in os.walk("data/Auxiliary_equipment_new"):
    for file in files:
        file_path = os.path.join(root, file)

        template = cv2.imread(file_path)
        h, w = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .76
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            # 문자열 파싱        
            file_name = file_path.split('\\')[1].split('.')[0]
            print("file_name : ", file_name)
            ae[file_name] += 1
            #######
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

print("ae : ", ae)

cv2.imshow("img_rgb", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
