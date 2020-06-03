import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    def SetUp(self):
        self.new_movie = Movie(1234,'Python must be crazy','A thrilling Python Thriller','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

        def test_instance(self):
            self.AssertTrue(isinstance(self.new_movie,Movie))

if __name__ =='__main__':
    unittest.main()
