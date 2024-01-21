import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from imageUtils import warp_img
from dataExtractor import get_student_id, get_answers

class Reader:
    def __init__(self, img):
        self.img = img
        self.student_id = None
        self.answers = None

    def read(self):
        self.img = warp_img(self.img)
        if self.img is None:
            raise Exception("Failed to warp image")

        self.student_id = get_student_id(self.img)
        self.answers = get_answers(self.img)

        return self.student_id, self.answers
    
if __name__ == "__main__":
    img = cv.imread("/Users/tanakornpisuchpen/Program/python/imgProcessing/production/IMG_2341.png")
    reader = Reader(img)
    student_id, answers = reader.read()
    print(student_id)