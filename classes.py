class Book:
    def __init__(self,  title, author, pages, price, year) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.year = year
        
class Movie:
    def __init__(self, title, director, playtime, price, year) -> None:
        self.title = title
        self.director = director
        self.playtime = playtime
        self.price = price
        self.year = year
        
class CD:
    def __init__(self, title, artist, tracks, playtime, price) -> None:
        self.title = title
        self.artist = artist
        self.tracks = tracks
        self.playtime = playtime
        self.price = price