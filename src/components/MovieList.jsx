import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
const MovieList = (props) => {
	const [movieList, updateMovieList] = useState([]);

	useEffect(() => {
		fetch('http://127.0.0.1:5000/movie/list')
			.then((res) => res.json())
			.then((data) => {
				updateMovieList(data);
			})
			.catch((err) => console.log(err));
	});

	return (
		<ul style={{ marginLeft: '0px' }}>
			{movieList.map((movie, idx) => {
				return (
					<li key={idx}>
						<Link to={`/movie/${movie.id}`}>{movie.movieTitle}</Link> <span>({movie.movieYear})</span>
					</li>
				);
			})}
		</ul>
	);
};

export default MovieList;
