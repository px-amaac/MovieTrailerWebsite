class Movie():
    """
    Class movie describes a movie item that will be created from json.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url, running_time, release_date ):
        """
        initialize movie class.
        :param title: Title of the movie
        :param poster_image_url: URL to the poster image
        :param trailer_youtube_url: Url to the youtube trailer
        :param running_time: running time of the movie
        :param release_date: release date of the movie.
        :return:
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.running_time = running_time
        self.release_date = release_date



