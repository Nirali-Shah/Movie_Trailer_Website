# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:32:57 2018

@author: Nirali
"""
import webbrowser

class Movie: # class
        
    """ This is a documentation for movie trailer website!"""
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    # constructor & self to access the particular instance, remaining are instance variables called using self 
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): 
                self.title = movie_title
                self.storyline = movie_storyline
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                                
