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
		self.cognitive_functions = self.set_cognitive_functions()
		self.temperament = self.set_temperament()
		self.personality_type = self.set_personality_type()

	def __str__(self):
		return self.personality_type

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
		preferences = {}

		if self.strengths['E'] > self.strengths['I']:
			preferences['Attitude'] = 'E'
		elif self.strengths['E'] < self.strengths['I']:
			preferences['Attitude'] = 'I'
		else:
			preferences['Attitude'] = 'X'

		if self.strengths['S'] > self.strengths['N']:
			preferences['Perceiving'] = 'S'
		elif self.strengths['S'] < self.strengths['N']:
			preferences['Perceiving'] = 'N'
		else:
			preferences['Perceiving'] = 'X'

		if self.strengths['T'] > self.strengths['F']:
			preferences['Judging'] = 'T'
		elif self.strengths['T'] < self.strengths['F']:
			preferences['Judging'] = 'F'
		else:
			preferences['Judging'] = 'X'

		if self.strengths['J'] > self.strengths['P']:
			preferences['Lifestyle'] = 'J'
		elif self.strengths['J'] < self.strengths['P']:
			preferences['Lifestyle'] = 'P'
		else:
			preferences['Lifestyle'] = 'X'

		return preferences

	def set_cognitive_functions(self):
		cognitive_functions = {}

		if self.preferences['Attitude'] == 'E':
			if self.preferences['Lifestyle'] == 'J':
				if self.preferences['Judging'] == 'T':
					cognitive_functions['Dom'] = 'Te'
					cognitive_functions['Inf'] = 'Fi'
				else:
					cognitive_functions['Dom'] = 'Fe'
					cognitive_functions['Inf'] = 'Ti'

				if self.preferences['Perceiving'] == 'S':
					cognitive_functions['Aux'] = 'Si'
					cognitive_functions['Ter'] = 'Ne'
				else:
					cognitive_functions['Aux'] = 'Ni'
					cognitive_functions['Ter'] = 'Se'
			else:
				if self.preferences['Perceiving'] == 'S':
					cognitive_functions['Dom'] = 'Se'
					cognitive_functions['Inf'] = 'Ni'
				else:
					cognitive_functions['Dom'] = 'Ne'
					cognitive_functions['Inf'] = 'Si'

				if self.preferences['Judging'] == 'T':
					cognitive_functions['Aux'] = 'Ti'
					cognitive_functions['Ter'] = 'Fe'
				else:
					cognitive_functions['Aux'] = 'Fi'
					cognitive_functions['Ter'] = 'Te'
		else:
			if self.preferences['Lifestyle'] == 'J':
				if self.preferences['Judging'] == 'T':
					cognitive_functions['Aux'] = 'Te'
					cognitive_functions['Ter'] = 'Fi'
				else:
					cognitive_functions['Aux'] = 'Fe'
					cognitive_functions['Ter'] = 'Ti'

				if self.preferences['Perceiving'] == 'S':
					cognitive_functions['Dom'] = 'Si'
					cognitive_functions['Inf'] = 'Ne'
				else:
					cognitive_functions['Dom'] = 'Ni'
					cognitive_functions['Inf'] = 'Se'
			else:
				if self.preferences['Perceiving'] == 'S':
					cognitive_functions['Aux'] = 'Se'
					cognitive_functions['Ter'] = 'Ni'
				else:
					cognitive_functions['Aux'] = 'Ne'
					cognitive_functions['Ter'] = 'Si'

				if self.preferences['Judging'] == 'T':
					cognitive_functions['Dom'] = 'Ti'
					cognitive_functions['Inf'] = 'Fe'
				else:
					cognitive_functions['Dom'] = 'Fi'
					cognitive_functions['Inf'] = 'Te'

		return cognitive_functions

	def set_temperament(self):
		if self.preferences['Perceiving'] == 'S':
			return self.preferences['Perceiving'] + self.preferences['Lifestyle']
		else:
			return self.preferences['Perceiving'] + self.preferences['Judging']

	def set_personality_type(self):
		personality_type = self.preferences['Attitude']
		personality_type += self.preferences['Perceiving']
		personality_type += self.preferences['Judging']
		personality_type += self.preferences['Lifestyle']

		return personality_type
