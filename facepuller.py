import cv2
import os

face_count = 0

def pullface(imagePath, imageFormat, outputFolder):
    global face_count
    img = cv2.imread(imagePath)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    print("break1")

    for (x, y, w, h) in faces:
        # Extract the face from the image
        face_img = img[y:y+h, x:x+w]
        

        # save face image to "faces" folder
        image_name, _ = os.path.splitext(os.path.basename(imagePath))
        face_filename = os.path.join(outputFolder, f'{image_name}_face_{face_count}.{imageFormat}')
        cv2.imwrite(face_filename, face_img)
        print(face_filename)
        face_count += 1

    print("break2")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

