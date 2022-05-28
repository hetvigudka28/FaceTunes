# import the required modules
import cv2
# import matplotlib.pyplot as plt
from deepface import DeepFace

# read image
def func():
    print("coming")
    img = cv2.imread('webapp/emotion.jpg')
    print(type(img))

    # # call imshow() using plt object
    # plt.imshow(img[:,:,::-1])
    #
    # # display that image
    # plt.show()

    # storing the result
    result = DeepFace.analyze(img,actions=['emotion'])

    # print result
    print(result)
    print(result['dominant_emotion'])
    emot = result['dominant_emotion']
    return emot

    print("ED")
