import usb.core
import usb.util
arduino = usb.core.find(idVendor=0x0403, idProduct=0x6001)
if arduino is None:
    raise ValueError('Device not found')
else:
    signal = arduino.readline()
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
#elif signal == b'\r\n'or signal == b'0\r\n':
#    import os
#    os.system("pkill" + "/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
#    quit("/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
