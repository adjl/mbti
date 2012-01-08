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
		self.preferences = {}
		self.preferences['E'], self.preferences['I'] = self.get_preference('EI')
		self.preferences['S'], self.preferences['N'] = self.get_preference('SN')
		self.preferences['T'], self.preferences['F'] = self.get_preference('TF')
		self.preferences['J'], self.preferences['P'] = self.get_preference('JP')

		self.personality_type = self.get_personality_type()

	def __str__(self, verbose=False):
		output = self.personality_type

		if verbose:
			preference_names = {
				'E': 'Extraversion', 'I': 'Introversion',
				'S': 'Sensing',      'N': 'iNtuition',
				'T': 'Thinking',     'F': 'Feeling',
				'J': 'Judging',      'P': 'Perceiving'
			}

			preference_list = 'EISNTFJP'
			for preference in preference_list:
				output += '{0:12} ({1}): {2:3d}\n'.format(preference_names[preference], preference, self.preferences[preference])
			output = output.rstrip('\n')

		return output

	def get_preference(self, dichotomy):
		import random

		preferences = {
			'EI': 49.3,
			'SN': 73.3,
			'TF': 40.2,
			'JP': 54.1
		}

		preference = round(random.uniform(0, 100), 1)
		strength = random.randint(50, 100)

		if 0 <= preference <= preferences[dichotomy]:
			return strength, 100 - strength
		elif preferences[dichotomy] + 0.1 <= preference <= 100:
			return 100 - strength, strength

	def get_personality_type(self):
		personality_type = ''

		if self.preferences['E'] > self.preferences['I']:
			personality_type += 'E'
		elif self.preferences['E'] < self.preferences['I']:
			personality_type += 'I'
		else:
			personality_type += 'X'

		if self.preferences['S'] > self.preferences['N']:
			personality_type += 'S'
		elif self.preferences['S'] < self.preferences['N']:
			personality_type += 'N'
		else:
			personality_type += 'X'

		if self.preferences['T'] > self.preferences['F']:
			personality_type += 'T'
		elif self.preferences['T'] < self.preferences['F']:
			personality_type += 'F'
		else:
			personality_type += 'X'

		if self.preferences['J'] > self.preferences['P']:
			personality_type += 'J'
		elif self.preferences['J'] < self.preferences['P']:
			personality_type += 'P'
		else:
			personality_type += 'X'

		return personality_type
