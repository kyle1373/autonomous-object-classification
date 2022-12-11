'''
ECE276A WI22 PR1: Color Classification and Recycling Bin Detection
'''

import os, cv2
import numpy as np
from skimage.measure import label, regionprops
import pickle
import matplotlib
matplotlib.use('TkAgg')


def segment_image(img, model):
    '''
        Obtain a segmented image using a color classifier,
        e.g., Logistic Regression, Single Gaussian Generative Model, Gaussian Mixture, 
        call other functions in this class if needed
        
        Inputs:
            img - original image
        Outputs:
            mask_img - a binary image with 1 if the pixel in the original image is red and 0 otherwise
    '''

    # generate data from img
    X_orig = img.reshape((img.shape[0]*img.shape[1]), img.shape[2])
    X = X_orig.astype(np.float64)/255
        
    # label data
    y = model.predict(X)
    
    # get segmented image
    mask = np.full([y.size, 3], 0, int)
    mask[np.argwhere(y==1),:] = int(255)
    mask_img = mask.reshape((img.shape[0], img.shape[1], img.shape[2]))
    mask_img = mask_img.astype(np.uint8)
    
    # refine img
    kernel1 = np.ones((3,3), np.uint8)
    kernel2 = np.ones((1,1), np.uint8)
    mask_img1 = cv2.erode(mask_img, kernel1, iterations=1)
    mask_img2 = cv2.dilate(mask_img1, kernel2, iterations=1)

    return mask_img2

def get_bounding_boxes(mask_img):
    '''
        Find the bounding boxes of the recycling bins
        call other functions in this class if needed
        
        Inputs:
            img - original image
        Outputs:
            boxes - a list of lists of bounding boxes. Each nested list is a bounding box in the form of [x1, y1, x2, y2] 
            where (x1, y1) and (x2, y2) are the top left and bottom right coordinate respectively
    '''
    
    # segment img preprocessing
    gray_img = cv2.cvtColor(mask_img, cv2.COLOR_RGB2GRAY)
    contours, _= cv2.findContours(gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    lb_img = label(gray_img, connectivity=1).astype(np.uint8)
    regp = regionprops(lb_img)
    
    # detect recycling bins
    boxes = []
    good_box = []
    for reg in regp:
      box = reg.bbox
      if 0.4<=(box[3]-box[1])/(box[2]-box[0])<=1 and reg.area/reg.bbox_area>=0.25 \
        and reg.bbox_area/(mask_img.shape[0]*mask_img.shape[1])>0.015:
        good_box = [box[1], box[0], box[3], box[2]]
        boxes.append(good_box)   
    return boxes

def iou(box1,box2):
  '''
    Computes the intersection over union of two bounding boxes box = [x1,y1,x2,y2]
    where (x1, y1) and (x2, y2) are the top left and bottom right coordinates respectively
  '''
  x1, y1 = max(box1[0], box2[0]), max(box1[1], box2[1])
  x2, y2 = min(box1[2], box2[2]), min(box1[3], box2[3])
  inter_area = max(0, (x2 - x1 + 1)) * max(0, (y2 - y1 + 1))
  union_area = (box1[2] - box1[0] + 1) * (box1[3] - box1[1] + 1) + (box2[2] - box2[0] + 1) * (box2[3] - box2[1] + 1) - inter_area
  return inter_area/union_area




if __name__ == '__main__':
    
  modelname = 'colorclassifier.sav'
  colorclassifier = pickle.load(open(modelname, 'rb'))

  folder = "data/test"
  # n = 0

  for filename in os.listdir(folder):
    # if filename.endswith(".jpg"):
    if filename.endswith(".jpg") and filename.startswith('006'):
      # read one test image
      img = cv2.imread(os.path.join(folder,filename))
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

      # segment the image
      mask_img = segment_image(img, colorclassifier)
      cv2.imshow('seg_img',mask_img)
      cv2.waitKey(0)
      
      # detect recycling bins
      estm_boxes = get_bounding_boxes(mask_img)
      
      # draw estm boxes
      for good_box in estm_boxes:
        cv2.rectangle(img, (good_box[0], good_box[1]), (good_box[2], good_box[3]), (0,255,0), 2)        
      cv2.imshow('box_img', img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

