# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:37:43 2018

@author: Nirali
"""
# import class file and Html python file

import media 
import movie_trailer 

# below declared each movie is instance of a class Movie

toy_story = media.Movie("Toy Story", 
                            "A story of a boy and his toys that come to life.",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie ("Avatar",
                      "A marine on a alien planet",
                      "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                      "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                             "Using Rock Music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", 
                          "A rat is a chef in paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality Show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpeg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Images are store on local machine for below declared Movies

peter_rabbit = media.Movie("Peter Rabbit",
                           "Peter Rabbit and his three sisters -- Flopsy, Mopsy, and Cotton -- enjoy"
                           " spending time in their vegetable garden.",
                           r"C:\Movie_Trailer_Website\movie_poster\peter_rabbit.jpg",
                           "https://www.youtube.com/watch?v=7Pa_Weidt08")
early_man = media.Movie("Early Man",
                           "A plucky cave man named Dug, his sidekick Hognob and the rest of"
                           " their tribe face a grave threat to their simple existence.",
                           r"C:\Movie_Trailer_Website\movie_poster\early_man.jpg",
                           "https://www.youtube.com/watch?v=ZRiPQ8YNrVs")

father_figures = media.Movie("Father Figures",
                           "Wilson and Helms are Kyle and Peter Reynolds, brothers whose eccentric"
                           " mother raised them to believe their father had died when they were young.",
                           r"C:\Movie_Trailer_Website\movie_poster\father_figures.jpg",
                           "https://www.youtube.com/watch?v=59uWyPklsy0")

fifty_shades_freed = media.Movie("Fifty Shades Freed",
                           "Believing they've left behind the shadowy figures from the past,"
                           " billionaire Christian Grey and his new wife, Anastasia, fully embrace their"
                           " inextricable connection and shared life of luxury.",
                           r"C:\Movie_Trailer_Website\movie_poster\fifty_shades_freed.png",
                           "https://www.youtube.com/watch?v=O5RZEt3arI0")

all_money_in_world = media.Movie("All The Money In The World",
                           "All The Money In The World follows the kidnapping of 16-year-old"
                           " John Paul Getty III.",
                           r"C:\Movie_Trailer_Website\movie_poster\all_money_in_world.jpg",
                           "https://www.youtube.com/watch?v=KXHrCBkIxQQ")

maze_runner = media.Movie("Maze Runner The Death Cure",
                           "Thomas leads some escaped Gladers on their final and most dangerous mission yet.",
                           r"C:\Movie_Trailer_Website\movie_poster\maze_runner.jpg",
                           "https://www.youtube.com/watch?v=4-BTxXm8KSg")

# create a list of movies to show

movies = [ all_money_in_world, maze_runner, fifty_shades_freed, 
          father_figures, early_man, peter_rabbit,
          school_of_rock, midnight_in_paris]

# open python file containing webpage HTML and Functions to supply data -- Open it

movie_trailer.open_movies_page(movies)
