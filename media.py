import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_year):
        """ This Docstring explains the constructor method """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = movie_year

    def show_trailer(self):
        """ This Docstring explains what the show trailer function does """
        webbrowser.open(self.trailer_youtube_url)
