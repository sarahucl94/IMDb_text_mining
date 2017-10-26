import serial #open serial device package
import vlc_ctrl
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
        x = arduino.read() #read the signal from the arduino
        print(x) #print the first byte incoming
        class Video(object):
            def __init__(self, path):
                self.path = ["/Volumes/MY DATA/Users/Sarah/Desktop/movie1.mpeg"] #open VLC app for movie playing
            def play(self):
                Movie = vlc.MediaPlayer("/Volumes/MY DATA/Users/Sarah/Desktop/movie1.mpeg")
                #plays the movie through the webbrowser
                Movie.play('file://'+ "/Volumes/MY DATA/Users/Sarah/Desktop/movie1.mpeg")
                #open movie file
        #class Movie_MP4(Video):
 ##       movie = Movie_MPEG(r"/Volumes/MY DATA/Users/Sarah/Desktop/movie1.mpeg")
#        movie.play() #read and play the movie
#        break
 #   if arduino.inWaiting() == False:
 #       self.Movie.pause('file://'+ "/Volumes/MY DATA/Users/Sarah/Desktop/movie1.mpeg")
 
        
