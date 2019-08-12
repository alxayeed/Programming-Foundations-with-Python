#Movie details

import media
import time

toy_story = media.Movie('24th July','birthday of Al','Al.jpg','F:\Practice\Python\Courses\Programming Foundations with Python Videos\movie\trailer.mp4')
print(toy_story.title)
toy_story.show_poster()
time.sleep(10)
toy_story.show_trailer()

