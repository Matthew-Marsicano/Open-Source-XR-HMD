from picamera2 import Picamera2 
from time import sleep

picam2 = Picamera2()

try:
		config = picam2.create_still_configuration()
		picam2.configure(config)
		
		picam2.start()
		print("camera preview")
		
		sleep(5)
		
		image_path = "/home/test_image.jpg"
		picam2.capture_file(image_path)
		print("captured image")
		
except Exception as e:
		print("error")
finally:
	picam2.stop()
	print("camera Stopped")	
