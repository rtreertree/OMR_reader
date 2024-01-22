import omr
import cv2

image = cv2.imread("AnswerSheet.png")

reader = omr.Reader(image)
student_id, answers = reader.read()

print(student_id, answers)