
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class KDGame(Widget):
	pass

class MyApp(App):
	def build(self):
		return KDGame()

if __name__ == '__main__':
	MyApp().run()