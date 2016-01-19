
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.core.window import Window

class KDGame(Widget):
	aTower = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(KDGame, self).__init__(**kwargs)
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_down=self._on_keyboard_down)
	def _keyboard_closed(self):
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard = None
	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		if keycode[1] == 'w':
			self.aTower.moveU()
		if keycode[1] == 's':
			self.aTower.moveD()
		if keycode[1] == 'a':
			self.aTower.moveL()
		if keycode[1] == 'd':
			self.aTower.moveR()
			return True	
	def update(self,dt):
		pass
	

class Tower(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    def moveU(self):
		self.pos = Vector(*self.velocity) + self.pos + Vector(0, 10)
    def moveD(self):
		self.pos = Vector(*self.velocity) + self.pos + Vector(0, -10)
    def moveL(self):
		self.pos = Vector(*self.velocity) + self.pos + Vector(-10, 0)
    def moveR(self):
		self.pos = Vector(*self.velocity) + self.pos + Vector(10, 0)


class MyApp(App):
	def build(self):
		game = KDGame()
		Clock.schedule_interval(game.update,1.0/60.0)
		return game

if __name__ == '__main__':
	MyApp().run()