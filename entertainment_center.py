import fresh_tomatoes
import media

the_conjuring = media.Movie("The Conjuring", "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM3NjA1NDMyMV5BMl5BanBnXkFtZTcwMDQzNDMzOQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=k10ETZ41q5o", "2013")

zodiac = media.Movie("Zodiac", "A San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxNjc2NzAwNF5BMl5BanBnXkFtZTcwMDg3NzMzMw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", "https://www.youtube.com/watch?v=eNnzriT0ymU", "2007")

hateful_eight = media.Movie("Hateful Eight", "In the dead of a Wyoming winter, a bounty hunter and his prisoner find shelter in a cabin currently inhabited by a collection of nefarious characters.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA1MTc1NTg5NV5BMl5BanBnXkFtZTgwOTM2MDEzNzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=6_UI1GzaWv0", "2015")

fight_club = media.Movie("Fight Club", "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg", "https://www.youtube.com/watch?v=BdJKm16Co6M", "1999")

the_green_mile = media.Movie("The Green Mile", "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_.jpg", "https://www.youtube.com/watch?v=ctRK-4Vt7dA", "1999")

don_jon = media.Movie("Don Jon", "A New Jersey guy dedicated to his family, friends, and church, develops unrealistic expectations from watching porn and works to find happiness and intimacy with his potential true love.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQxNTc3NDM2MF5BMl5BanBnXkFtZTcwNzQ5NTQ3OQ@@._V1._CR28,28.649993896484375,1271,1991.0000305175781_SY1000_CR0,0,638,1000_AL_.jpg", "https://www.youtube.com/watch?v=6615kYTpOSU", "2013")

movies = (the_conjuring, zodiac, hateful_eight,
          fight_club, the_green_mile, don_jon)

fresh_tomatoes.open_movies_page(movies)
