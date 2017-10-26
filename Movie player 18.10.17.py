import time
class Video(object):
    #create an object for a class that can be modified
    def __init__(self, path):
        #init is a constructor, so you can "build on class
        self.path = ["/Users/Sarah/Desktop/VLC.app"]
        #open file with VLC

    def play(self):
        import webbrowser
        #opens file in a webpage
        webbrowser.open('file://'+ "/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
        #choose file to open from directory
        
class Movie_MP4(Video):
    type = "MP4"
    #class of object is a video in mp4 format

movie = Movie_MP4(r"/Volumes/MY DATA/Users/Sarah/Desktop/movie.mp4")
#reads the file of the movie
if input("Press enter to play") == '':
    movie.play()
    #asks user to play movie by pressing "Enter" button
else:
    print("error")
    #if user presses other button, no movie played
    #can modify this last part to make it automated with the signal generator
