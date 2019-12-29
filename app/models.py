class Movie:
    '''
    Movie class to define Movie objects
    '''
    
    def __init__(self, id, title, overview, poster, vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    all_reviews = []

    def __init__(self, movie_id, title, imageurl, rebiew):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = Review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews:
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):

        response = []

        for review in cls.all_reviews:
            if review.mocie_id == id:
                response.append(review)
        
        return response