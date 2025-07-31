from LD06 import LD06_DRIVER
import numpy as np
import cv2

size_window = 700
mashtab = size_window / 10

min_angle = 225
max_angle = 315
max_range = 2

font = cv2.FONT_HERSHEY_COMPLEX
tables = 5
rows = 3

radiant_row = 3

step_table = (max_angle-min_angle) / (tables - 1)
step_rows = max_range / (rows - 1)

img = np.full((size_window, size_window, 3), 255, dtype=np.uint8)

for i in range(tables):
    x =  int(max( min(size_window / (tables - 1) * i, size_window-1) , 1))
    x_text = x -60 if size_window == x +1 else x + 5
    cv2.putText(img, str(int(min_angle + i * step_table)),(x_text,size_window - 5),font,0.7,(0,0,255),2)
    cv2.line(img, (x, 0), (x, size_window), (0, 0, 255), 2)

value = max_angle
for i in range(rows - 1):
        y =  int(max( min(size_window / (rows - 1) * i, size_window-1) , 1))
        y_text =  y + 25 if y ==  1 else  y - 5
        cv2.putText(img, str(round(max_range - (step_rows * i), 2)),(5,y_text),font,0.7,(255,0,0),2)
        for d in range(size_window ):
            if d % radiant_row == 0:
                cv2.line(img, ( d * radiant_row , y), (radiant_row * d + radiant_row  , y), (255, 0, 0), 2, cv2.LINE_4)
cv2.imshow('1', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# ldar = LD06_DRIVER()
# data = ldar.read_data()
# print(data)