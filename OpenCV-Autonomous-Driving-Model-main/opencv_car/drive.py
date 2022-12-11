import depthai as dai
import vesc_class as VESC
import image_class

def main():

    print("Running Team 15's car...")
    # Create pipeline
    pipeline = dai.Pipeline()

    # Define source and output
    camRgb = pipeline.create(dai.node.ColorCamera)
    xoutVideo = pipeline.create(dai.node.XLinkOut)

    xoutVideo.setStreamName("video")

    # Properties
    camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
    camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    camRgb.setVideoSize(1920, 1080)

    xoutVideo.input.setBlocking(False)
    xoutVideo.input.setQueueSize(1)

    # Linking
    camRgb.video.link(xoutVideo.input)
    
    with dai.Device(pipeline) as device:

        # get video from camera
        video = device.getOutputQueue(name="video", maxSize=1, blocking=False)

        # Create VESC Object
        carVESC = VESC.VESC('/dev/ttyACM0') 

        # smoothing variables
        instances = 1 # get n frame values and average to allow for smoothing
        steering_val = []; throttle_val = [] # array to hold values

        while True:
            for frame in range(instances):
                # get frame from camera
                videoIn = video.get()
                orig_frame = videoIn.getCvFrame()


                ## calculate steering and throttle based on lane_detection
                # steering, throttle = lane_detection.main(orig_frame)

                ## calculate steering adn throttle based on number of 
                steering, throttle = image_class.image_functions.getSteeringAndThrottleFromImage(orig_frame)

                steering_val.append(steering)
                throttle_val.append(throttle)
            
            # finds average value to input into VESC
            steering_avg = sum(steering_val)/instances
            throttle_avg = sum(throttle_val)/instances
            print(steering_avg, throttle_avg)
            

            # Use VESC.run() to set steering and throttle
            # carVESC.run(steering_avg,throttle_avg)

            carVESC.run(steering,throttle)

            # reset steering and throttle vals
            steering_val = []; throttle_val = []

if __name__ == '__main__':
    main()