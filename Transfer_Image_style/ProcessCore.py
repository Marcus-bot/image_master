import cv2

import numpy as np
import random

from numpy.core.records import get_remaining_size

image_path = ''
image_befo_path = ''
floder_path = ''

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————

'''变换1：调整对比度，亮度'''


# def Image_Adjust(image, a, b):
#     a += 100
#     a /= 100.0
#     rows, cols, channels = image.shape
#     dst = image
#     for i in range(rows):
#         for j in range(cols):
#             for c in range(channels):
#                 color = image[i, j][c] * a + b  # 调整像素值
#                 if color > 255:
#                     dst[i, j][c] = 255
#                 elif color < 0:
#                     dst[i, j][c] = 0
#                 else:
#                     dst[i, j][c] = color
#     return dst
def Image_Adjust(image, a, b):
    a += 100
    a /= 100.0
    rows, cols, channels = image.shape
    dst = image
    color = np.array(image * a+b, dtype=int)  # 调整像素值
    mask = color > 255
    color[mask] = 255
    mask = color < 0
    color[mask] = 0
    dst = color.astype(np.uint8)
    return dst

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————


'''变换2：二值化图像'''


# def Image_Binarization(image, a, b):
#     a += 128
#     rows, cols, channels = image.shape
#     dst = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#     for i in range(rows):
#         for j in range(cols):  # 二值化图像
#             if b == 1:
#                 if dst[i, j] >= a:
#                     dst[i, j] = 255
#                 else:
#                     dst[i, j] = 0
#             else:
#                 if dst[i, j] <= a:
#                     dst[i, j] = 255
#                 else:
#                     dst[i, j] = 0
#     return dst

def Image_Binarization(image, a, b):
    rows, cols, channels = image.shape
    dst = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    mask = np.array(dst > a, dtype=int)
    mask = 255*mask
    dst = cv2.merge([mask, mask, mask]).astype(np.uint8)
    return dst


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————

'''变换3：图像滤波'''


def Image_Blur(image, a, b):
    if a == 0:
        return image
    if b == 1:
        img_mean = cv2.blur(image, (5, 5))
        for i in range(a - 1):
            img_mean = cv2.blur(img_mean, (5, 5))  # 均值滤波
        return img_mean
    elif b == 2:
        img_median = cv2.medianBlur(image, 5)
        for i in range(a - 1):
            img_median = cv2.medianBlur(img_median, 5)  # 中值滤波
        return img_median
    elif b == 3:
        img_bilater = cv2.bilateralFilter(image, 9, 75, 75)  # 双边滤波
        for i in range(a - 1):
            img_bilater = cv2.bilateralFilter(img_bilater, 9, 75, 75)
        return img_bilater
    else:
        img_Guassian = cv2.GaussianBlur(image, (5, 5), 0)  # 高斯滤波
        for i in range(a - 1):
            img_Guassian = cv2.blur(img_Guassian, (5, 5))

        return img_Guassian


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————

'''变换4：Canny算子边缘检测'''


def CannyEdge_detect(image, a, b, c):
    a += 50
    b += 150
    blur = cv2.GaussianBlur(image, (3, 3), 0)  # 高斯滤波预处理图像
    canny = cv2.Canny(blur, a, b)
    canny = cv2.merge([canny, canny, canny])
    return canny


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————

'''变换5：直线检测'''


def HoughLines_detect(image, a, b):
    a += 100
    b += 10
    color = (0, 255, 0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)  # Canny算子提取边缘
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50,
                            minLineLength=a, maxLineGap=b)  # Hough变换提取直线
    if lines is None:
        return image
    dst = image*1
    for line in lines:
        x1, y1, x2, y2 = line[0]
        dst = cv2.line(dst, (x1, y1), (x2, y2), color, 2)
    return dst


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————

'''变换6：圆形检测'''


def HoughCircle_detect(image, a, b, d):
    a += 50
    b += 300
    d += 200
    out_img = image*1
    color = (0, 0, 255)
    dst = cv2.pyrMeanShiftFiltering(out_img, 10, 100)  # 预滤波
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    circle = cv2.HoughCircles(
        dst, cv2.HOUGH_GRADIENT, 1, d, param1=50, param2=30, minRadius=a, maxRadius=b)
    if not circle is None:
        circle = np.uint16(np.around(circle))
        for i in circle[0, :]:
            cv2.circle(out_img, (i[0], i[1]), i[2], color, 3)
    return out_img


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————

'''变换7：轮廓检测'''


def contour_detect(image, width):
    dst = image*1
    color = (0, 255, 0)
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 灰度图轮廓检测
    cv2.drawContours(dst, contours, -1, color, width)
    return dst

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————


'''变换9：通道提取'''


def Channel_Select(image, r, g, b):
    dst = image*1
    dst[:, :, 2] = dst[:, :, 2]*r
    dst[:, :, 1] = dst[:, :, 1]*g
    dst[:, :, 0] = dst[:, :, 0]*b

    return dst


'''变换10 风格迁移'''


def style_transfer(image, model, median_filter):

    net = cv2.dnn.readNetFromTorch(model)

    frame = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    B_mean = np.mean(image[:, :, 0])
    G_mean = np.mean(image[:, :, 1])
    R_mean = np.mean(image[:, :, 2])

    inWidth = frame.shape[1]
    inHeight = frame.shape[0]
    # inp = cv2.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
    #                             (103.939, 116.779, 123.68), swapRB=False, crop=False)
    inp = cv2.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                (B_mean, G_mean, R_mean), swapRB=False, crop=False)

    net.setInput(inp)
    out = net.forward()

    out = out.reshape(3, out.shape[2], out.shape[3])
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.68
    out /= 255
    out = out.transpose(1, 2, 0)

    t, _ = net.getPerfProfile()

    out = cv2.medianBlur(out, median_filter)
    # out = 255*cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
    out = 255*out
    mask = out > 255
    out[mask] = 255
    mask = out < 0
    out[mask] = 0
    return out.astype(np.uint8)


def Rotate_image(image, angle):
    img = image*1
    rotated = img
    if angle == 1:
        pass
    elif angle == 2:
        rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 3:
        rotated = cv2.rotate(img, cv2.ROTATE_180)
    elif angle == 4:
        rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    return rotated
