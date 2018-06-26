import datetime
import os
from time import sleep
import picamera



dt = datetime.datetime.now()


def capture_picture(dest_folder, imgTextSize):
    '''
    Function for capturing image and saving to folder as jpg
    
        dest_folder -> /path/for/captured/image.jpg
        imgTextSize -> 'number' size of annotated text on image
    '''

    with picamera.PiCamera() as camera:
        # set camera resolution
        camera.resolution = (1920, 1080)
        # start camera to warm up
        camera.start_preview()
        # annote text (with options)
        ##camera.annotate_foreground = picamera.Color(y=?, u=?, v=?)
        camera.annotate_text_size = imgTextSize
        camera.annotate_text = '{} kl {}'.format(dt.strftime("%a %d/%b/%Y"), dt.strftime("%H:%M:%S"))
        # wait 2 seconds
        sleep(2)
        
        try:
            # take picture
            camera.capture('{}image{}.jpg'.format(dest_folder, dt.strftime("%Y-%m-%d_%H-%M-%S")))
        
        finally:
            camera.stop_preview()
    
def syncronizeToNextcloud():
    '''
    Function for synchronizing images in folder to Nextcloud folder
    '''
    os.system("rsync -azP /home/pi/projekter/timelapse_projekter/madagascar_jewel/timelapse_pics_new/* /home/pi/nextcloud/engineering/projects/plant_timelapse/new_pictures/")

    
capture_picture('./pictures/', 50)
#syncronizeToNextcloud()




### Quick test for capturing images
'''
with picamera.PiCamera() as c:
    c.resolution = (3280, 2464)
    c.start_preview()
    sleep(2)
    c.capture('./timelapse_pics/image01.jpg')
    c.stop_preview()
'''
