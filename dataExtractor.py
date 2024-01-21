import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt




def extract_data(imglist):
    offet = 3
    size = 19
    minscore = 10000
    secondscore = 10000
    maxindex = -1
    for i, img in enumerate(imglist):
        # preprocess
        img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        img = cv.threshold(img, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
        score = cv.countNonZero(img)

        if score < minscore:
            secondscore = minscore
            minscore = score
            maxindex = i
        elif score < secondscore:
            secondscore = score

        if i == -1:
            cv.imshow(f"img score : {score}", img)
            cv.waitKey(0)
            cv.destroyAllWindows()
        
    # print(minscore, secondscore, maxindex+1)
    if secondscore - minscore > 100:
        return maxindex + 1
    else:
        return -1


def get_student_id(img) -> str:
    x = 34
    y = 115
    width = 256
    height = 190

    image = img[y:y+height, x:x+width]
    height, width = image.shape[:2]

    num_rows = 10
    num_cols = 6

    cell_width = width // num_cols
    cell_height = height // num_rows

    x_axis_images_dict = {}
    answerList = []
    # Iterate through each X-axis column
    for x in range(num_cols):
        x_axis_images_list = []
        for y in range(num_rows):
            x_image = image[y * cell_height: (y + 1) * cell_height, x * cell_width: (x + 1) * cell_width]
            x_axis_images_list.append(x_image)
        x_axis_images_dict[x + 1] = x_axis_images_list
        answerList.append(extract_data(x_axis_images_list))
    return "".join(map(str, answerList))

def read_answers(img, orgin, size, num_rows, last_row = 0):
    x = orgin[0]
    y = orgin[1]
    width = size[0]
    height = size[1]

    image = img[y:y+height, x:x+width]
    height, width = image.shape[:2]

    num_rows = num_rows
    num_cols = 5

    cell_width = width // num_cols
    cell_height = height // num_rows

    answerList = {}

    for i in range(num_rows):
        x_axis_images_list = []
        for j in range(num_cols):
            x_image = image[i * cell_height: (i + 1) * cell_height, j * cell_width: (j + 1) * cell_width]
            x_axis_images_list.append(x_image)
        answerList[last_row+i+1] = extract_data(x_axis_images_list)
    return answerList

def get_answers(img):
    list1 = read_answers(img, (42, 318), (172, 212), 10, 0)
    list2 = read_answers(img, (375, 73), (183, 465), 22, 10)
    list3 = read_answers(img, (622, 66), (183, 380), 18, 32)
    result = {}
    result.update(list1)
    result.update(list2)
    result.update(list3)
    return result