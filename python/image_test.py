import cv2
import numpy as np
import os

auxiliary_equipment = {"ekey":0, "hera":0, "jiben":0, "bul":0, "athena":0, "time":0, "ni":0, "go":0}
accessories = {"am":0, "pi":0, "zip":0, "botiban":0, "botipal":0, "botimok":0, "geoban":0, "geopal":0, "geomok":0, "jungban":0, "jungpal":0, "jungmok":0, "superring":0, "superarm":0, "supermok":0}
armor = {}

# 분석할 이미지
img_rgb = cv2.imread('2.jpg')
i = 1
for (root, directories, files) in os.walk("data/Armor"):

    # 폴더 전체 경로
    for d in directories:
        d_path = os.path.join(root, d)
        print("d_path : ", d_path) # data\Auxiliary_equipment

    for file in files:
        file_path = os.path.join(root, file) # data\Accessories_new\am.jpg
        print("file_path : ", file_path)

        template = cv2.imread(file_path)
        h, w = template.shape[:-1]

        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        # threshold = .76
        # loc = np.where(res >= threshold)

        # 스크린샷에 없는 이미지일 경우 for에 안들어 온다.
        # for pt in zip(*loc[::-1]):  # Switch collumns and rows
            # 문자열 파싱
            # directory_name = file_path.split('\\')[1].split('.')[0]
            # file_name = file_path.split('\\')[2].split('.')[0]
            # print("directory_name : ", directory_name)
            # print("file_name : ", file_name)

            # if directory_name == 'Accessories':
            #     accessories[file_name] += 1
            # elif directory_name == 'Auxiliary_equipment':
            #     auxiliary_equipment[file_name] += 1

            # elif directory_name == 'Armor':
            #     armor[file_name] += 1
            #######
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 10)

        # 어떤 이미지 때문에 제대로 인식이 안되는지 확인 필요할 때 사용
        # print("i : ", i, " / file_path : ", file_path)
        # cv2.imwrite("result_"+str(i)+".jpg", img_rgb)
        # i += 1
        ##########################################################

print("auxiliary_equipment : ", auxiliary_equipment)
print("accessories : ", accessories)

cv2.imwrite('result.jpg', img_rgb)

# cv2.imshow("img_rgb", img_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
