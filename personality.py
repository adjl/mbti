# personality.py

"""Module containing personality-related classes.

This module currently contains classes pertaining to the Myers-Briggs Type
Indicator. More models of personality type will be added in the future, namely
the Keirsey Temperament Sorter and the Enneagram of Personality. Other possible
ones are Jungian Psychological Types, Big Five and SLOAN.

Author: Helena 'Adei' Josol <helena.josol@gmail.com>

"""

class PersonalityType:
	def __init__(self):
		self.strengths = self.set_strengths()
		self.preferences = self.set_preferences()
		self.personality_type = self.set_personality_type()

	def __str__(self, verbose=False):
		output = self.personality_type

		if verbose:
			strength_names = {
				'E': 'Extraversion', 'I': 'Introversion',
				'S': 'Sensing',      'N': 'iNtuition',
				'T': 'Thinking',     'F': 'Feeling',
				'J': 'Judging',      'P': 'Perceiving'
			}

			strength_list = 'EISNTFJP'
			for strength in strength_list:
				output += '{0:12} ({1}): {2:3d}\n'.format(strength_names[strength], strength, self.strengths[strength])
			output = output.rstrip('\n')

		return output

	def set_strengths(self):
		import random

		probabilities = {
			'EI': 49.3,
			'SN': 73.3,
			'TF': 40.2,
			'JP': 54.1
		}

		strengths = {}

		for dichotomy in probabilities.keys():
			probability = round(random.uniform(0, 100), 1)
			strength = random.randint(50, 100)

			if probability <= probabilities[dichotomy]:
				strengths[dichotomy[0]] = strength
				strengths[dichotomy[1]] = 100 - strength
			else:
				strengths[dichotomy[0]] = 100 - strength
				strengths[dichotomy[1]] = strength

		return strengths

	def set_preferences(self):
		preferences = []

		if self.strengths['E'] > self.strengths['I']:
			preferences.append('E')
		elif self.strengths['E'] < self.strengths['I']:
			preferences.append('I')
		else:
			preferences.append('X')

		if self.strengths['S'] > self.strengths['N']:
			preferences.append('S')
		elif self.strengths['S'] < self.strengths['N']:
			preferences.append('N')
		else:
			preferences.append('X')

		if self.strengths['T'] > self.strengths['F']:
			preferences.append('T')
		elif self.strengths['T'] < self.strengths['F']:
			preferences.append('F')
		else:
			preferences.append('X')

		if self.strengths['J'] > self.strengths['P']:
			preferences.append('J')
		elif self.strengths['J'] < self.strengths['P']:
			preferences.append('P')
		else:
			preferences.append('X')

		return preferences

	def set_personality_type(self):
		personality_type = ''
		for preference in self.preferences:
			personality_type += preference
		return personality_type
