"""API Query Helper Methods"""
import os
import requests
import json
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
  "contentType": "movie"
}]

class OMDBHelper:
    def __init__(self) -> None:
        self.omdb_api_key = os.getenv('OMDB_API_KEY', 'a6a008eb')
        self.omdb_base_url = 'https://omdbapi.com'

    def _createMovieList(self, movie_list: list) -> list:
      movies = []
      for movie in movie_list['Search']:
        movies.append({
          'id': movie['imdbID'],
          'movieTitle': movie['Title'],
          'movieYear': movie['Year'],
          'contentType': "summary"
        })
      return jsonify(movies)


    def _createMovieDetail(self, movie: dict) -> dict:
      return jsonify({
        'id': movie['imdbID'],
        'movieTitle': movie['Title'],
        'movieYear': movie['Year'],
        'movieLength': movie['Runtime'],
        'moviePlot': movie['Plot'],
        'moviePoster': movie['Poster'],
        'contentType': 'movie'

      })


    def get_movie_list(self) -> list:
      try:
        query = f'{self.omdb_base_url}/?apikey={self.omdb_api_key}&s=star+wars'
        resp = requests.get(query)
        return self._createMovieList(resp.json())
      except Exception as e:
        return jsonify(sampleMovieList)

    def get_movie_details(self, imdb_id: str) -> dict:
      try:
        query = f'{self.omdb_base_url}/?apikey={self.omdb_api_key}&i={imdb_id}'
        resp = requests.get(query)
        return self._createMovieDetail(resp.json())
      except Exception:
        return jsonify(sampleMovieDetail)