import requests
import flask
from flask_cors import CORS, cross_origin
from omdb_helper import OMDBHelper

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
omdb = OMDBHelper()


@app.route('/movie/list', methods=['GET'])
@cross_origin()
def movie_list():
    return omdb.get_movie_list()

@app.route('/movie/detail/<string:movie_id>', methods=['GET'])
@cross_origin()
def movie_detail(movie_id):
  return omdb.get_movie_details(movie_id)

app.run()