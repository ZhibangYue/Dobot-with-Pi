import cv2
import numpy as np


# 鼠标回调函数
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # 当鼠标左键被按下时打印坐标信息
        print(f'Mouse Position: (X: {x}, Y: {y})')


# 开启摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouse_click)
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('Frame', frame)
    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 释放摄像头资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
