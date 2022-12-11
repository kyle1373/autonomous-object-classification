import cv2

def doNothing(x):
    pass

def main():
    cv2.namedWindow('Track Bars', cv2.WINDOW_NORMAL)
    #creating track bars for gathering threshold values of red green and blue
    cv2.createTrackbar('min_blue', 'Track Bars', 0, 255, doNothing)
    cv2.createTrackbar('min_green', 'Track Bars', 0, 255, doNothing)
    cv2.createTrackbar('min_red', 'Track Bars', 0, 255, doNothing)

    cv2.createTrackbar('max_blue', 'Track Bars', 0, 255, doNothing)
    cv2.createTrackbar('max_green', 'Track Bars', 0, 255, doNothing)
    cv2.createTrackbar('max_red', 'Track Bars', 0, 255, doNothing)

    image_path = 'dayimages/data/images/775_cam_image_array_.jpg'
    # reading the image
    object_image = cv2.imread(image_path)

    #resizing the image for viewing purposes
    resized_image = cv2.resize(object_image,(300, 200))
    #converting into HSV color model
    hsv_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

    #showing both resized and hsv image in named windows
    cv2.imshow('Base Image', resized_image)
    cv2.imshow('HSV Image', hsv_image)

    #creating a loop to get the feedback of the changes in trackbars
    while True:
    #reading the trackbar values for thresholds
        min_blue = cv2.getTrackbarPos('min_blue', 'Track Bars')
        min_green = cv2.getTrackbarPos('min_green', 'Track Bars')
        min_red = cv2.getTrackbarPos('min_red', 'Track Bars')
    
        max_blue = cv2.getTrackbarPos('max_blue', 'Track Bars')
        max_green = cv2.getTrackbarPos('max_green', 'Track Bars')
        max_red = cv2.getTrackbarPos('max_red', 'Track Bars')
    
        #using inrange function to turn on the image pixels where object threshold is matched
        mask = cv2.inRange(hsv_image, (min_blue, min_green, min_red), (max_blue, max_green, max_red))
        #showing the mask image
        cv2.imshow('Mask Image', mask)
        # checking if q key is pressed to break out of loop
        key = cv2.waitKey(25)
        if key == ord('q'):
            break

    #printing the threshold values for usage in detection application
    print(f'min_blue {min_blue}  min_green {min_green} min_red {min_red}')
    print(f'max_blue {max_blue}  max_green {max_green} max_red {max_red}')
    #destroying all windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()