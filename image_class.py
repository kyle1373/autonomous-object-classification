import cv2
import numpy as np
import bin_detector

class image_functions():
    
    def __init__(self, image, model, t):
        self.image = image
        self.colorclassifier = model
        self.t = t
    
    def lowerbodyDetection(self):
        
        frame_lb = np.copy(self.image)
        image_lb = cv2.cvtColor(frame_lb, cv2.COLOR_BGR2GRAY)
        cascade_classifier = cv2.CascadeClassifier(
            f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
        detected_objects = cascade_classifier.detectMultiScale(
            image_lb, minSize=(20, 20))

        if len(detected_objects) != 0:
            return True
            for (x, y, height, width) in detected_objects:
                cv2.rectangle(frame_lb, (x, y), ((x + height), (y + width)), (0, 255, 0), 5)

    
    def binDetection(self):
        
        frame_bin = np.copy(self.image)
        image_bin = cv2.cvtColor(frame_bin, cv2.COLOR_BGR2RGB)

        # segment the image
        mask_img = bin_detector.segment_image(image_bin, self.colorclassifier)
        cv2.imshow('seg_img',mask_img)
        cv2.waitKey(0)
        
        # detect recycling bins
        estm_boxes = bin_detector.get_bounding_boxes(mask_img)
        
        if len(estm_boxes)>0:
            
            for good_box in estm_boxes:
            # get box size
                box_height = abs(good_box[3]-good_box[1])
                box_width = abs(good_box[2]-good_box[0])
                if max(box_height, box_width)>100:
                    return True
            # draw estm boxes
                cv2.rectangle(frame_bin, (good_box[0], good_box[1]), (good_box[2], good_box[3]), (0,255,0), 2)        

    def getSteeringAndThrottleFromImage(self):

        detected_lb = self.lowerbodyDetection()
        detected_bin = self.binDetection()
        flag = False
        ts = 0
        throttle = 0
        steering = 0
        
        while (not detected_lb):
            
            if flag:
                ts = np.copy(self.t)
                flag = False
            
            throttle = .20
            steering = 0
            
            if self.t-ts>400 and ts>0:
                steering = -0.2
                ts = 0
            
            if detected_bin:
                steering = 0.2
                flag = True
        
        return steering, throttle
        
