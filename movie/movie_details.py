#Movie details

import media
import time

toy_story = media.Movie('24th July','birthday of Al','Al.jpg','F:\Practice\Python\Courses\Programming Foundations with Python Videos\movie\trailer.mp4')
# print(toy_story.title)
# toy_story.show_poster()
# time.sleep(10)
# toy_story.show_trailer()

#Predefined variables
print(media.Movie.__module__) #gives the  module name
print(media.Movie.__name__) #gives name of the class 
print(media.Movie.__doc__) #gives the documentation

