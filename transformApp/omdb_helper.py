"""API Query Helper Methods"""
import os
import requests
from flask import jsonify

sampleMovieDetail = {
  "id": "tt0110357",
  "movieTitle": "The Lion King",
  "movieYear": "1994",
  "movieLength": "88 min",
  "moviePlot": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
  "moviePoster": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SX300.jpg",
  "contentType": "movie"
}

sampleMovieList = [{
  "id": "tt0110357",
  "movieTitle": "The Lion King",
  "movieYear": "1994",
  "contentType": "movies"
}]

class OMDBHelper:
    def __init__(self) -> None:
        self.omdb_api_key = os.getenv('OMDB_API_KEY', None)
        self.omdb_base_url = 'https://omdbapi.com'
      
    def get_movie_list(self):
      return jsonify(sampleMovieList)

    def get_movie_details(self, imdb_id):
      return jsonify(sampleMovieDetail)