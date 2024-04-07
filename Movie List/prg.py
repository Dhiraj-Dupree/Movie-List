class Movie:
      def __init__(self, title, description, duration, rating, actors):
            self.title = title
            self.description = description
            self.duration = duration
            self.rating = rating
            self.actors = actors
            self.nextMovie = None

class WatchList:
      def __init__(self):
            self.head = None

      def add_movie(self, title, description, duration, rating, actors):
            new_movie = Movie(title, description, duration, rating, actors)
            if not self.head:
                  self.head = new_movie
            else:
                  current_movie = self.head
                  while current_movie.nextMovie:
                        current_movie = current_movie.nextMovie
                  current_movie.nextMovie = new_movie

      def displayMovieList(self):
            current_movie = self.head
            while current_movie:
                  print(f'{current_movie.title} by {current_movie.actors} (Extras info: {current_movie.description}, {current_movie.rating}, {current_movie.duration})')
                  current_movie = current_movie.nextMovie

if __name__ == "__main__":
    watchNext = WatchList()
    watchNext.add_movie('movie 1', 'actors 1', 180, '4.9', 'actor one, actor2., actor3')
    watchNext.add_movie('movie 2', 'actors 2', 120,  '4.5', 'actor four, actor5., actor6')
    watchNext.add_movie('movie 3', 'actors 3', 150, '4.7', 'actor seven, actor8., actor9')
    watchNext.displayMovieList()
