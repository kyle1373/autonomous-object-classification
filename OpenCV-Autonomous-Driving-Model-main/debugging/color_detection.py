# TechVidvan Object detection of similar color

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    # ret, frame = cap.read()

    used_image_link = 'dayimages/data/images/775_cam_image_array_.jpg'
    # It will turn right when more blue pixels. Left when more green pixels.
    img = cv2.imread(used_image_link)

    imageToUse = cv2.resize(img,(300, 200))
    # convert to hsv colorspace
    hsv = cv2.cvtColor(imageToUse, cv2.COLOR_BGR2HSV)

    # lower bound and upper bound for blue color
    lower_blue = np.array([97, 26, 0])	 
    upper_blue = np.array([255, 255, 160])

    # lower bound and upper bound for blue color
    lower_green = np.array([50, 45, 52])	 #[50, 12, 52]
    upper_green = np.array([100, 160, 222])   #[100, 71, 222]

    # find the colors within the boundaries
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # filter noise
    #define kernel size  
    kernel = np.ones((7,7),np.uint8)

    # Remove unnecessary noise from mask

    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_CLOSE, kernel)
    mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)

    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)

    # Showing the output

    resultblue = cv2.bitwise_and(imageToUse, imageToUse, mask=mask_blue)
    resultgreen = cv2.bitwise_and(imageToUse, imageToUse, mask=mask_green)

    bluepixels = np.sum(resultblue != 0)
    greenpixels = np.sum(resultgreen != 0)

    print("{} and {}".format("bluepixels is ", bluepixels))
    print("{} and {}".format("greenpixels is ", greenpixels))

    turnresult = greenpixels - bluepixels

    if(turnresult < 0):
        print("left")
    else:
        print("right")

    cv2.imshow("Original Filtering", imageToUse)
    cv2.imshow("Blue Filtering", resultblue)
    cv2.imshow("Green Filtering", resultgreen)
    while True:

        key = cv2.waitKey(25)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
    
if __name__ == "__main__":
    main()