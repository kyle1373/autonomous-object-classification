# Autonomous Object Classification

By Kyle Wade (ECE), Ziye Liu (MAE), and Zhuolin Niu (MAE). Team 15 in ECE 148 at UC San Diego.

# 3 autonomous laps driven with DonkeyCar

https://youtu.be/FVNbY5uvjHg

# 3 autonomous laps driven with OpenCV

https://youtu.be/ephBjfgTWhA

# Project Overview 

Train a vehicle to drive until it detects an object that is either movable or immovable. If it is immovable, it will navigate around the object. If it is movable, it will stop until the movable object is no longer in range.

![image](https://user-images.githubusercontent.com/59634395/207244675-022f54e1-1556-47b2-bb5b-98217dabb3b0.png)

# Electrical Schematic

![image](https://user-images.githubusercontent.com/59634395/207242946-bb10e014-676c-411b-b30b-95ce3fc1ac43.png)

# Mechanical Architecture

![image](https://user-images.githubusercontent.com/59634395/207244818-06fce14b-50aa-4358-9635-0933b3fe7b17.png)
![image](https://user-images.githubusercontent.com/59634395/207244869-3c7f0ef0-7008-4579-9187-efbad4ac7f68.png)
![image](https://user-images.githubusercontent.com/59634395/207244952-d64b235d-5281-41d7-9483-23dca541e885.png)

# Software Implementation

To find movable and immovable objects, we wrote two detectors, one for movable objects and one for immovable objects. The code changes steering and throttle based on the detected object. We used SKLearn to train a GDA color classifier using Supervised Learning among different labeled datasets. We used a model inference with a threshold to determine if an object is there and if they are a human or an immovable object. Since the camera cannot see the full human, we architectured lower-body detection to infer the lower body part of the human body. This model is more sensitive with moving legs. We also wrote trash bin detection to use for testing immovable object using masks and predictions. The model is trained with recognizing certain colors like dark blue or gray and then deciding if it’s an obstacle that can be avoided by checking the size of the marked area.

# Demonstration Video

https://youtu.be/M4I5mHzLiq4

# How To Run

Make sure you have all of the dependencies installed, then run...

`python drive.py`
