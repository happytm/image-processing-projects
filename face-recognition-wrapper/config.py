#image is resized by width before processing to increase performance (speed)
resize_image_by_width = 400

# angle to rotate camera in degreeds
rotate_camera_by = 180

# delay between processing frames, frames are skipped for better performance
process_image_delay_ms = 100

# number of threads that will be spawned and that will handle actual face detection
frame_processing_threads = 1

mqtt = {
    'host' : 'localhost',
    'port' : 1883, # mosquitto default port
    'user' : 'user',
    'password' : 'your_password'
}

# folder containing faces images
faces_path = './faces/'

# folder containing thumbnails
thumbs_path = './thumbs/'

# temporary folder path for images
temporary_path = './temp/'

mongodb_uri = 'mongodb://localhost:27017/'