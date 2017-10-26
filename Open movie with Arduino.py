import serial
import numpy
arduino = serial.Serial('/dev/tty.usbserial-AH03J5N6', 9600)
signal = arduino.readline().decode().strip('\r\n')
print(signal)

if signal:
    class Video(object):
        def __init__(self, path):
            self.path = ["/Users/Sarah/Desktop/VLC.app"]
        def play(self):
            import webbrowser
            webbrowser.open('file://'+ "/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
    class Movie_MP4(Video):
        type = "MP4"
    movie = Movie_MP4(r"/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
    movie.play()
