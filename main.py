import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_list = ["Miller's Crossing", "The Man Who Wasn't There", "O Brother, Where Art Thou?", "No Country for Old Men", "True Grit"]
        # TODO: randomly choose one of the movies, and return it
        selection = random.choice(movie_list)
        return selection

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        movie2 = self.getRandomMovie()
        while movie == movie2:
            movie2 = self.getRandomMovie()
        content += "<h1>Tommorrow's Movie</h1>"
        content += "<p>" + movie2 + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
