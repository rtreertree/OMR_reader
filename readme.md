# OMR reader project

---

### OMR (Optical mark recognition)
Opical mark recognition (OMR) is a process that can identifying the marking on the answer paper.

### About this project
This project is dedicated to gaining a thorough understanding of Optical Mark Recognition (OMR) and engaging in practical exercises centered around image preprocessing using Python and OpenCV.

### How it work
0. Read the image use `cv.imread()`
1. We capture the ArUco Marker in 4 position
2. After that we use `cv2.warpPerspective()` to align the input image
3. Now, We will extract the mark with image POI using functon `extract_data()` in dataExtractor.py
    1. Read the student ID by declare origin position,
    2. Read the answer from the captured POI
4. Return all extracted data

### Usage & Implement
This function is designed to operate with either the 'AnswerSheet.pdf' or 'AnswerSheet.png' pattern.
1. dowload file `omr.py`, `imageUtils.py`, `dataExtractor.py`
2. create a class
```python:
import omr
import cv2

image = cv2.imread("imgPath.png")

reader = omr.Reader(image)
student_id, answers = reader.read()

print(student_id, answers)
```