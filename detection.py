import cv2     #face detection, objection tracking, landmark detection
import os      #File Path
import time
import uuid    #Use name of image file

IMAGES_PATH = 'Tensorflow\workspace\images\collectedimages'

labels = ['helo', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    path = 'Tensorflow\workspace\images\collectedimages\\'
    # os.mkdir {'Tensorflow\workspace\images\collectedimages\\' + label}    # Create Directory
    os.mkdir(path+label)
    cap = cv2.VideoCapture(0)       # Initilize Webcame
    print('Collecting images fo {}'.format(label))
    time.sleep(5)       # Sleep of 5 minutes Give a time to set position
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

