import webbrowser

#The below class contains two functions/constructors:
    #The contstructor '__init__' Takes four attributes:
             #movie's title, storyline, poster image and trailer
    #The contructor 'show_trailer' opens the web browser to show chosen movie trailer

class Movie():
    """
    This class provides a way to store movie related information

    Movie Class is the template of all the instances (movie objects) to be created
    """

    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
