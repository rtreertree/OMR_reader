
import cv2 as cv
from cv2 import aruco
import numpy as np
import copy

def warp_img(img):
    retImg = copy.copy(img)

    # preprocess
    kernel = np.array([[0, -1, 0],
                    [-1, 5,-1],
                    [0, -1, 0]])
    img = cv.filter2D(src=img, ddepth=-1, kernel=kernel)
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img = cv.threshold(img, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

    # detect the markers
    arucoDict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
    arucoParams = cv.aruco.DetectorParameters()
    detector = cv.aruco.ArucoDetector(arucoDict, arucoParams)

    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)
    if len(markerCorners) < 4:
        return None
    

    # warp the image
    pts1 = np.empty((4, 2), dtype=np.int32)
    for mark, id in zip(markerCorners, markerIds):
        match id:
            case 0:
                pts1[0] = mark[0][0]
            case 1:
                pts1[1] = mark[0][1]
            case 2:
                pts1[2] = mark[0][3]
            case 3:
                pts1[3] = mark[0][2]


    # draw marker
    for p in pts1:
        img = cv.circle(img, tuple(p), 5, (0, 0, 255), -1)
        
    pts1 = np.float32(pts1)
    pts2 = np.float32([[0, 0], [826, 0], [0 , 583], [826, 583]])
    
    matrix = cv.getPerspectiveTransform(pts1, pts2)
    retImg = cv.warpPerspective(retImg, matrix, (826, 583))

    return retImg