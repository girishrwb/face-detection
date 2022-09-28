import cv2
import random

#load a shitload of pretrained data for feeding knowledge to the pc
trained_face_data = cv2.CascadeClassifier('Default_frontal_face.xml')

def for_image(image):
    #load in the image
    img = cv2.imread(image)

    #must convert to grayscale
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(grey_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    #print(face_coordinates)

    #show img
    cv2.imshow('Face App', img)
    cv2.waitKey()

#for_image('avengers.jpeg')

def video_capture():
    webcam = cv2.VideoCapture(0)
    while True:
        successful_frame_read, frame = webcam.read()
        grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_coordinates = trained_face_data.detectMultiScale(grey_img)
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0, 2))

        cv2.imshow('Face App', frame)
        key = cv2.waitKey(1)

        if key == 81 or key == 113:
            break

    webcam.release()



'''
        # detect faces
        face_coordinates = trained_face_data.detectMultiScale(grey_img)
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        # print(face_coordinates)

        # show img
        cv2.imshow('Face App', img)
        cv2.waitKey()
        '''

video_capture()
print("code works")