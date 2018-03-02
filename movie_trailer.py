"""
Tutorial Wed Feb 14 12:32:57 2018

@leraning: Nirali
"""
import webbrowser
import os
import re # used for regression match


# Styles and scripting for the Webpage
main_page_head = '''
<head>
	<!-- Meta charset for encoding and metadata for information -->
	<meta charset="utf8">
    <meta name="description" content="Movie Listing">
    <meta name="keywords" content="Early Man, Maze Runner The Death Cure, All The Money In The World, Fifty Shades Freed, Father Figures, Peter Rabbit, Trailers, Movies">
    <meta name="author" content="Nirali Shah">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	
	<!-- Bootstrap 3 / jquery -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	 <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script> 
	
	<!--  internal css None -->
	<style type = "text/css" media = "screen"></style>
	
	<!--  external css & Js -->
	<link rel="stylesheet" href="movie_trailer.css" type="text/css">
	<script type="text/javascript" charset="utf8" src="movie_trailer.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal fade" id="trailer" role="dialog">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <!-- Close image on Modal -->
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Movie review Modal -->
	
<!-- Modal -->
<div class="modal fade" id="review-modal"  role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title">Add Movie Review</h4>
      </div>
      <div class="modal-body">
        <div>
		<form action="/action_page.php">
		Movie Name:<br>
				<input type="text" name="movieName" value=""><br>
		Reviews:<br>
				<input type="text" name="movieReviews" value=""><br><br>
				<input type="submit" value="Submit" onclick();>
		</form> 
		</div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>

  </div>
</div>
    <!-- Main Page Content -->
    <!-- Header of the Web page -->
	
    <div class="container">
      <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container-fluid">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Show Movie Trailers: </a>
          </div>
		  <ul class="nav navbar-nav">
			<li class="active"><a href="#">Home</a></li>
			<li><a href="#">Page 2</a></li>
			<li><a href="#">Page 3</a></li>
		  </ul>
		  <form class="navbar-form navbar-left" action="/action_page.php">
			<div class="input-group">
				<input type="text" class="form-control" placeholder="Search" name="search">
					<div class="input-group-btn">
						<button class="btn btn-default" type="submit">
							<i class="glyphicon glyphicon-search"></i>
						</button>
					</div>
			</div>
		  </form> 
        </div>
      </nav>
    </div>
    
    <!-- Main page Movie Content - Trailers -->
    <div class = "container-fluid">
         {movie_tiles}
    </div> 
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
        <div class="col-md-4 col-lg-4 text-center">
                <div class="movie-text text-center">{movie_title}</div>
						<div class = "movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                	<a href="#" class = "movie-story-line" data-toggle="tooltip" data-placement="right" title="{movie_storyline}">					
                 <img class ="movie-frame" src="{poster_image_url}" width="220" height="342">
                 </a>
						</div>
						<div data-toggle="modal" data-target="#review-modal">
                  <span class="glyphicon glyphicon-plus movie-review-ratings">Add Review </span>
               </div>
        </div>
'''



def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url , search checks for anywhere inthe string
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('Movie_Trailer.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
  
  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible