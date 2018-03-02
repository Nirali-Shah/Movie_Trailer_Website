 
	// Start playing the video whenever the trailer modal is opened
	// use following code method : document.method(eventtype, eventdata, handler{}
		   
		$(document).on('click','.movie-tile',function(event){
			  var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
			  var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
			   $("#trailer-video-container").empty().append($("<iframe></iframe>", {
				  'id': 'trailer-video',
				  'type': 'text-html',
				  'src': sourceUrl,
				  'frameborder': 0
				}));
				
			// to hide tool tip when trailer video is played	
			   $("[data-toggle='tooltip']").tooltip('hide');
			    
			// to make background color of trailer video black on click 
			   $('#trailer').css("background-color","black");
			   
			   
			// to reduce the opacity of the background while trailer video is played
			   $(".movie-frame").fadeTo("slow", 0.15);
			   $(".movie-text").fadeTo("slow", 0.15);
			   $(".review-ratings").fadeTo("slow", 0.15);

	   });
	  
		
	// Pause the video when the modal is closed
	
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
			
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
			
            $("#trailer-video-container").empty();
			
			// to restore the opacity after the trailer video is closed
			$(".movie-frame").fadeTo("slow", 1);
			$(".movie-text").fadeTo("slow", 1);
			$(".review-ratings").fadeTo("slow", 1);
			
        });
		
	/* Animate in the movies when the page loads [Currently, it is under comment to check the ADD Review Modal ]
	
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
		});
	*/
	
	// Display tooltip for storyline of the active movie
		$(document).ready(function(){
			$('[data-toggle="tooltip"]').tooltip();   
		});