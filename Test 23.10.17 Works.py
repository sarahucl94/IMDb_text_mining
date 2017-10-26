import serial #open serial device package
connected = None #default is "device NOT connected"
locations = ['/dev/tty.usbserial-AH03J5N6'] #find the USB arduino device
for device in locations: 
    try:
        print("Trying..", device) #if device present print this
        arduino = serial.Serial('/dev/tty.usbserial-AH03J5N6', 9600) #open the USB arduino device
        break
    except:
        print("Failed to connect to", device) #if USB not found print this instead
while not connected: #means while it IS connected
    signal = arduino.read() #read signal from arduino
    connected = True #change default to connected
while 1: #make a loop for arduino signal reception
    if arduino.inWaiting(): #while signal in bytes is incoming
        x = arduino.readline() #read the signal from the arduino
        print(x) #print the first byte incoming
        if x:
            class Video(object):
                def __init__(self, path):
                    self.path = ["/Users/Sarah/Desktop/VLC.app"] #open VLC app for movie playing
                def play(self):
                    import webbrowser #plays the movie through the web-browser
                    webbrowser.open('file://'+ "/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
                    #open movie file
            class Movie_MP4(Video):
                type = "MP4"
            movie = Movie_MP4(r"/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
            movie.play() #read and play the movie
            break
    while True:
            if x == '\n':
                movie = False
                import os
                os.system("pkill" + "/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
 
        
    
