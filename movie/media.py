#Movie details
import webbrowser

class Movie():

	def __init__(self,title,info,poster,trailer):
		self.title = title
		self.info = info
		self.poster = 'al.jpg'
		self.trailer = 'trailer.mp4'

	def show_trailer(self):
		webbrowser.open(self.trailer)
	def show_poster(self):
		webbrowser.open(self.poster)


		

	