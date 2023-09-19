# Project Overview:
Leverage TensorFlow and OpenCV to design and implement a vehicle system that can drive autonomously, identify movable and immovable obstacles, and take appropriate actions when encountering them.

## Key Features:
### Object Detection:
The system can differentiate between movable and immovable objects. This is crucial because the action the vehicle takes differs based on the nature of the obstacle.
### Navigation:
When the vehicle identifies an immovable object, it does not stop. Instead, it computes a new path to navigate around the obstacle, ensuring the vehicle's smooth movement.
### Decision Making:
For movable objects, the vehicle halts its progress. It remains stationary until the obstacle (for instance, a person walking) moves out of its path. Once the path is clear, the vehicle resumes its autonomous drive.

![image](https://user-images.githubusercontent.com/59634395/207244675-022f54e1-1556-47b2-bb5b-98217dabb3b0.png)

# Electrical Schematic

![image](https://user-images.githubusercontent.com/59634395/207242946-bb10e014-676c-411b-b30b-95ce3fc1ac43.png)

# Mechanical Architecture

![image](https://user-images.githubusercontent.com/59634395/207244818-06fce14b-50aa-4358-9635-0933b3fe7b17.png)
![image](https://user-images.githubusercontent.com/59634395/207244869-3c7f0ef0-7008-4579-9187-efbad4ac7f68.png)
![image](https://user-images.githubusercontent.com/59634395/207244952-d64b235d-5281-41d7-9483-23dca541e885.png)

# 3 autonomous laps driven with DonkeyCar (trained with TensorFlow)

https://youtu.be/FVNbY5uvjHg

# 3 autonomous laps driven with OpenCV

https://youtu.be/ephBjfgTWhA

# Software Implementation

To find movable and immovable objects, we wrote two detectors, one for movable objects and one for immovable objects. The code changes steering and throttle based on the detected object. We used SKLearn to train a GDA color classifier using Supervised Learning among different labeled datasets. We used a model inference with a threshold to determine if an object is there and if they are a human or an immovable object. Since the camera cannot see the full human, we architectured lower-body detection to infer the lower body part of the human body. This model is more sensitive with moving legs. We also wrote trash bin detection to use for testing immovable object using masks and predictions. The model is trained with recognizing certain colors like dark blue or gray and then deciding if it’s an obstacle that can be avoided by checking the size of the marked area.

# Demonstration Video

https://youtu.be/M4I5mHzLiq4

# How To Run

Make sure you have all of the dependencies installed, then run...

`python drive.py`

# Credits

Kyle Wade, Ziye Liu, and Zhuolin Niu
