# TechVidvan Object detection of similar color

import cv2
import numpy as np

class image_functions():

    def getSteeringAndThrottleFromImage(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # lower bound and upper bound for blue color
        lower_blue = np.array([97, 26, 0])	  # [97, 26, 0]
        upper_blue = np.array([255, 255, 160]) # [255, 255, 160]

        # lower bound and upper bound for blue color
        lower_green = np.array([50, 45, 52])	 #[50, 45, 52]
        upper_green = np.array([100, 160, 222])   #[100, 160, 222]

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

        resultblue = cv2.bitwise_and(image, image, mask=mask_blue)
        resultgreen = cv2.bitwise_and(image, image, mask=mask_green)

        bluepixels = np.sum(resultblue != 0)
        greenpixels = np.sum(resultgreen != 0)

        # print("{} and {}".format("bluepixels is ", bluepixels))
        # print("{} and {}".format("greenpixels is ", greenpixels))


    
        throttle = .20

        # if(bluepixels == 0):
        #     steering = 0
        #     return steering, throttle
        
        # if(greenpixels == 0):
        #     steering = 1
        #     return steering, throttle
        

        # turnresult = (greenpixels*1.0)/bluepixels
        # if(turnresult < 1):
        #     # turn right

        #     steering = turnresult / 2.0
            
        #     return steering, throttle
        
        # #turn left
        # turnresult = (bluepixels*1.0)/greenpixels
        
        # # We have a spectrum from 0 to 1 that as it further deviates.
        # # We flip the spectrum, add 1 to move it forward, then divide by 2 to shrink it
        # convertedresult = ((1 - turnresult) + 1.0) / 2.0

        # steering = convertedresult

        # return steering, throttle


        # Original:

        turnresult = bluepixels - greenpixels
        print(turnresult)
        if(turnresult < -1000000):
            #left
            steering = 1
        elif(turnresult < -800000):
            steering = .9
        elif(turnresult < -600000):
            steering = .8
        elif(turnresult < -400000):
            steering = .7
        elif(turnresult < 200000):
            steering = .6
        elif(turnresult < 0):
            steering = .5
        elif(turnresult < 200000):
            steering = .4
        elif(turnresult < 400000):
            steering = .3
        elif(turnresult < 600000):
            steering = .2
        elif(turnresult < 800000):
            steering = .1
        else:
                # right
            steering = 0 # 1
        
        return steering, throttle