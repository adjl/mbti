# personalityclasses.py

"""Module containing personality-related classes.

This module currently contains classes pertaining to the Myers-Briggs Type
Indicator. More models of personality type will be added in the future, namely
the Keirsey Temperament Sorter and the Enneagram of Personality. Other possible
ones are Jungian Psychological Types, Big Five and SLOAN.

Author: Helena 'Adei' Josol <helena.josol@gmail.com>

"""

class PersonalityType:
	def __init__(self, attitude='X', perceiving='X', judging='X', lifestyle='X'):
		if attitude == 'X':
			self.attitude = get_attitude()
		else:
			self.attitude = attitude
		if perceiving == 'X':
			self.perceiving = get_perceiving()
		else:
			self.perceiving = perceiving
		if judging == 'X':
			self.judging = get_judging()
		else:
			self.judging = judging
		if lifestyle == 'X':
			self.lifestyle = get_lifestyle()
		else:
			self.lifestyle = lifestyle
