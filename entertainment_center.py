import fresh_tomatoes
import media

# Information required for media.py
the_conjuring = media.Movie("The Conjuring",
                            "Paranormal investigators help a family.",
                            "https://goo.gl/z83Fsc",
                            "https://www.youtube.com/watch?v=k10ETZ41q5o",
                            "2013")

zodiac = media.Movie("Zodiac",
                     "A San Francisco cartoonist obsessed with down Killer.",
                     "https://goo.gl/1sIIVO",
                     "https://www.youtube.com/watch?v=eNnzriT0ymU",
                     "2007")

hateful_eight = media.Movie("Hateful Eight",
                            "Bounty hunter and prisoner find shelter.",
                            "https://goo.gl/dN73US",
                            "https://www.youtube.com/watch?v=6_UI1GzaWv0",
                            "2015")

fight_club = media.Movie("Fight Club",
                         "An office worker form an underground fight club.",
                         "https://goo.gl/ikljAN",
                         "https://www.youtube.com/watch?v=BdJKm16Co6M",
                         "1999")

the_green_mile = media.Movie("The Green Mile",
                             "Man accused of rape has a mysterious gift.",
                             "https://goo.gl/5OC1FM",
                             "https://www.youtube.com/watch?v=ctRK-4Vt7dA",
                             "1999")

don_jon = media.Movie("Don Jon",
                      "A New Jersey guy is obsessed with porn.",
                      "https://goo.gl/n9CQ7V",
                      "https://www.youtube.com/watch?v=6615kYTpOSU",
                      "2013")

movies = (the_conjuring, zodiac, hateful_eight,
          fight_club, the_green_mile, don_jon)

fresh_tomatoes.open_movies_page(movies)
