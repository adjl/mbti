# personalityclasses.py

"""Module containing personality-related classes.

This module currently contains classes pertaining to the Myers-Briggs Type
Indicator. More models of personality type will be added in the future, namely
the Keirsey Temperament Sorter and the Enneagram of Personality. Other possible
ones are Jungian Psychological Types, Big Five and SLOAN.

Author: Helena 'Adei' Josol <helena.josol@gmail.com>

"""

class PersonalityType:
	def __init__(self):
		self.extraversion, self.introversion = attitude()
		self.sensing, self.intuition = perceiving()
		self.thinking, self.feeling = judging()
		self.judging, self.perceiving = lifestyle()

	def attitude(self):
		pass

	def perceiving(self):
		pass

	def judging(self):
		pass

	def lifestyle(self):
		pass
