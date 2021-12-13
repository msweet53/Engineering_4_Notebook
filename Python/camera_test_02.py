import time
import picamera

with picamera.PiCamera() as camera:
    camera.image_effect = 'negative'
    print("capturing negative")
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('negative.jpg')
    camera.image_effect = 'solarize'
    print("capturing solarize")
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('solarize.jpg')
    camera.image_effect = 'sketch'
    print("capturing sketch")
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('sketch.jpg')
    camera.image_effect = 'denoise'
    print("capturing denoise")
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('denoise.jpg')
    camera.image_effect = 'emboss'
    print("capturing emboss")
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('emboss.jpg')
