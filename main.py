from LD06 import LD06_DRIVER
import numpy as np
import threading
import math
import cv2

size_window = 700

points = {
}
for i in range(225, 316):
    points = points | {i: 0} 
points[240] = 2

max_range = 2
mashtab = (size_window / 2)

font = cv2.FONT_HERSHEY_COMPLEX
tables = 5
rows = 3
radiant_row = 3


step_rows = max_range / (rows - 1)
ldar = LD06_DRIVER()

def update_points():
    while 1:
        data = ldar.read_data()
        for point in data: 
            dist = point[0]
            angle = int(round(point[2], 0))
            if 225 < angle < 315:
                if dist > max_range:
                    dist = max_range
                try:
                    points[angle] = dist
                except:
                    pass
            
def draw_rows(img):
    cv2.line(img, (0 , 0), (size_window // 2  , size_window), (0, 0, 0), 2)
    cv2.line(img, (size_window//2 , size_window), (size_window, 0), (0, 0, 0), 2)
    for i in range(rows):
        y =  int(max( min(size_window / (rows - 1) * i, size_window-1) , 1))
        y_text =  y + 25 if y ==  1 else  y - 5
        cv2.putText(img, str(round(max_range - (step_rows * i), 2)),(10,y_text),font,0.7,(255,0,0),2)
        for d in range(size_window ):
            if d % radiant_row == 0:
                cv2.line(img, ( d * radiant_row , y), (radiant_row * d + radiant_row  , y), (255, 0, 0), 2)


def draw_point(img):

    a_min = max_range * math.cos(math.radians(225))
    a_max = max_range * math.cos(math.radians(315))

    for angle, c in points.items():
        if c != 0:
            c = abs(c)
            radians = math.radians(angle)
            a = c * math.cos(radians)
            b = c * math.sin(radians)
            x = int((a - a_min) / (a_max - a_min) * size_window)
            y = int((1 - c / max_range) * size_window)

            cv2.circle(img, (x, y), 5, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)




thread = threading.Thread(target=update_points, daemon= True).start()
while 1:
    img = np.full((size_window, size_window, 3), 255, dtype=np.uint8)
    draw_rows(img)
    
    # for point in points:
    draw_point(img)

    cv2.imshow('1', img) 
    cv2.waitKey(500)

cv2.destroyAllWindows()

