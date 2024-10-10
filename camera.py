from picamzero import Camera
from time import sleep
def using_camera():
    cam = Camera()
    cam.capture_sequence("~\Desktop\astro pi project.jpg", num_image=10, interval=1)
def exporting_images():
    
