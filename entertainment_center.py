import media
import fresh_tomatoes


toy_story = media.Movie(
	"Toy Story", 
	"Toys that talk", 
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://www.youtube.com/watch?v=4KPTXpQehio"
	)

avatar = media.Movie(
	"Avatar", 
	"Blue People", 
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://www.youtube.com/watch?v=5PSNL1qE6VY"
	)

star_wars  = media.Movie(
	"Star Wars: The Force Awakens", 
	"The war of stars", 
	"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", 
	"https://www.youtube.com/watch?v=sGbxmsDFVnE"
	)

ever_after = media.Movie(
	"Ever After", 
	"Cinderella Story", 
	"https://upload.wikimedia.org/wikipedia/en/6/6e/Everafterposter.jpg", 
	"https://www.youtube.com/watch?v=L3eMhbH_-nM"
	)

the_parent_trap = media.Movie(
	"The Parent Trap", 
	"Children and Parents", 
	"https://upload.wikimedia.org/wikipedia/en/f/f9/Parenttrapposter.jpg",
	"https://www.youtube.com/watch?v=32WeiH4TrIY"
	)

elizabeth_the_golden_age = media.Movie(
	"Elizabeth: The Golden Age", 
	"Queen Elizabeth", 
	"https://upload.wikimedia.org/wikipedia/en/c/c5/Elizabeth_golden_poster.jpg", 
	"https://www.youtube.com/watch?v=0wNboYbgYjo"
	)

movies = [toy_story, avatar, star_wars, ever_after, the_parent_trap, elizabeth_the_golden_age]
fresh_tomatoes.open_movies_page(movies)