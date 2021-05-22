from expects import expect, be
from omdb_helper import OMDBHelper

class TestOMDBHelper:
    def test_get_movie_list(self):
        omdb = OMDBHelper()
        foo = omdb.get_movie_list()
        print(foo)
        # expect(1).to(be(1))