import time
import picamera

with picamera.PiCamera() as camera:
    camera.image_effect = 'negative'
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('urmom2.png')
