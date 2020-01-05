import fresh_tomatoes
import media

#The below lines are instances for the class 'Movie' previously defined in
#the python file 'media'
#They provide the respective movie title, storyline, poster image and trailer
#on YouTube
#There are 4 movies and are numbered accordingly

#Movie no.1
scarface = media.Movie("Scarface",
"In Miami in 1980, a determined Cuban immigrant takes over a drug cartel and succumbs to greed.",
"https://mvpo.us/img/P4988.jpg" ,
"https://www.youtube.com/watch?v=F_Xeb5o_Z0s")

#Movie no.2
pulp_fiction = media.Movie("Pulp Fiction",
"The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence.",
"https://images-na.ssl-images-amazon.com/images/I/717opCddMML._SY606_.jpg",
"https://www.youtube.com/watch?v=s7EdQ4FqbhY")

#Movie no.3
v_for_vendetta = media.Movie("V for Vendetta",
" An anonymous freedom fighter plots to overthrow the government with the help of a young woman.",
"https://i.pinimg.com/originals/76/29/62/762962775a8906aa120a52daadf0dc4e.jpg",
" https://www.youtube.com/watch?v=lSA7mAHolAw")

#Movie no.4
a_beautiful_mind = media.Movie("A Beautiful Mind",
"After John Nash, a brilliant but asocial mathematician, accepts secret work in cryptography, his life takes a turn for the nightmarish." ,
"https://m.media-amazon.com/images/M/MV5BMzcwYWFkYzktZjAzNC00OGY1LWI4YTgtNzc5MzVjMDVmNjY0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
" https://www.youtube.com/watch?v=WFJgUm7iOKw&pbjreload=10")

#The below list contains all the four movies mentioned below
#This has been made for the purpose of using it in the python
#file 'fresh_tomatoes' which takes in a list of movies
#and renders it on a webpage
movies = [scarface , pulp_fiction , v_for_vendetta , a_beautiful_mind]

fresh_tomatoes.open_movies_page(movies)
