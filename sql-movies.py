from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "programmer" table
class Movies(base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    movie_name = Column(String)
    directors = Column(String)
    release_date = Column(Integer)
    gross_income = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point ot our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating reords on our Programmer table
pulp_fiction = Movies(
    movie_name="Pulp Fiction",
    directors="Quentin Tarantino",
    release_date=1994,
    gross_income=2140000
)

trading_places = Movies(
    movie_name="Trading Places",
    directors="John Landis",
    release_date=1983,
    gross_income=1700000
)

robocop = Movies(
    movie_name="Robocop",
    directors="Paul Verhoeven",
    release_date=1976,
    gross_income=53000000
)

triangle_of_sadness = Movies(
    movie_name="Triangle Of Sadness",
    directors="Ruben Östlund",
    release_date=2022,
    gross_income=4600000
)

identity = Movies(
    movie_name="Identity",
    directors="James Mangold",
    release_date=2003,
    gross_income=16000000
)

as_good_as_it_gets = Movies(
    movie_name="As Good As It Gets",
    directors="James L. Brooks",
    release_date=1998,
    gross_income=314000000
)


# add each instance of our programmers to our session
# session.add(pulp_fiction)
# session.add(trading_places)
# session.add(robocop)
# session.add(triangle_of_sadness)
# session.add(identity)
# session.add(as_good_as_it_gets)

# commit our session to the database
session.commit()


# deleting a single record
# movie = input("Enter Movie Name: ")
# movies = session.query(Movies).filter_by(movie_name=movie).first()
# # defensive programming
# if movies is not None:
#     print("Movie found")
#     confirmation = input(f"Are you sure you want to delete {movie}? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(movies)
#         session.commit()
#         print(f"{movie} has been deleted")
#     else:
#         print(f"{movie} has not been deleted")
# else:
#     print("No record found")


# query the database to find all Programmers
movies = session.query(Movies)
for movie in movies:
    print(
        movie.id,
        movie.movie_name,
        movie.directors,
        movie.release_date,
        movie.gross_income,
        sep=" | "
    )
