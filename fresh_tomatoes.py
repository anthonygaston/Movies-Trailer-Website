import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title></themovies></title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" type="text/css" href="css/font-awesome.css">
    <link href="https://fonts.googleapis.com/css?family=Palanquin+Dark" rel="stylesheet">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        .navbar {
            border-bottom: 1px solid #2f2f2f;
            background: rgb(29,29,29);
        }
        body {
            color: white;
            text-align: center;
            margin: 0;
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-image: url(images/the-conjuring-screenshot.png);
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            background-color rgb(88, 249, 126);
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            font-family: 'Palanquin Dark', sans-serif;
            margin-bottom: 20px;
            padding-top: 20px;
            color: rgb(255, 255, 255);
            text-decoration: none;
        }
        .img-rounded:hover {
            color: rgba(0, 0, 0, 0.2);
            cursor: pointer;
        }
        .movie-tile a {
            margin-top: 0.8px;
            font-size: 16px;
            color: rgb(255, 255, 255);
        }
        .movie-tile a:hover {
            color: rgb(198, 198, 198);
            text-decoration: none;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .img-rounded {
            border: 5px solid rgb(255, 255, 255);
        }
        .fa-star {
            margin-right: 10px;
            color: #ff8400;
        }
        .home-content h1 {
            font-size: 44px;
            font-weight: 700;
            margin-bottom: 15px;
            text-shadow: 0 2px 2px rgba(0,0,0,.4);
        }

        .home-content p {
            font-size: 16px;
            color: rgb(209, 209, 209);
            width: 650px;
            margin: 0 auto;
            line-height: 21px;
            margin-bottom: 30px;
        }
        .top-6 h2 {
            font-size: 20px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-left" href="#"><img src="http://res.cloudinary.com/frogpond/image/upload/c_scale,w_156/v1493751340/tm-logo_vbzkhj.png"></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container home-content">
      <div class="hidden-xs hidden-sm">
        <h1>The World's Best Movie List</h1>
        <p>
        Welcome to <b>The Movies</b>. Here you'll find some of the best, most compelling films the galaxy has to offer. Watch the trailers, and see the ratings. Browse the greats here: <b>The Movies</b>.
        </p>
      </div>
    </div>
    <div class="top-6">
      <div class="row">
      <h2><i class="fa fa-star" aria-hidden="true"></i>Popular Movies</h2>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342" class="img-rounded">
    <div class="movie-poster-bottom">
      <a class="movie-title" href="#">{movie_title}</a>
      <div class="movie-title-year">{movie_year}</div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_year=movie.year

        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
