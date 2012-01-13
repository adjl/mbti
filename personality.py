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
		self.temperament, probability = self.set_temperament()
		self.personality_type = self.set_personality_type(self.temperament, probability)
		self.cognitive_functions = self.set_cognitive_functions(self.personality_type)
		# self.strengths = self.set_strengths()


	def __str__(self):
		return self.personality_type


	def set_temperament(self):
		import random

		probabilities = {
			'SJ': 0.405,
			'SP': 0.33,
			'NF': 0.14,
			'NT': 0.125
		}

		probability = round(random.uniform(0, 1), 3)
		boundary = 0
		for temperament in probabilities.keys():
			if boundary < probability <= boundary + probabilities[temperament]:
				return temperament, probabilities[temperament]
			boundary += probabilities[temperament]


	def set_personality_type(self, temperament, temperament_probability):
		import random

		probabilities = {
			'SJ': {
				'ESTJ': 0.13,
				'ESFJ': 0.12,
				'ISTJ': 0.085,
				'ISFJ': 0.07
			},
			'SP': {
				'ESTP': 0.1,
				'ESFP': 0.11,
				'ISTP': 0.06,
				'ISFP': 0.06
			},
			'NF': {
				'ENFJ': 0.04,
				'ENFP': 0.07,
				'INFJ': 0.01,
				'INFP': 0.02
			},
			'NT': {
				'ENTJ': 0.04,
				'ENTP': 0.045,
				'INTJ': 0.015,
				'INTP': 0.025
			}
		}

		probability = round(random.uniform(0, 1), 3)
		boundary = 0
		for personality_type in probabilities[temperament].keys():
			if boundary < probability <= boundary + probabilities[temperament][personality_type] / temperament_probability:
				return personality_type
			boundary += probabilities[temperament][personality_type] / temperament_probability


	def set_cognitive_functions(self, personality_type):
		preference = {
			'Attitude': 0,
			'Perceiving': 1,
			'Judging': 2,
			'Lifestyle': 3
		}

		personality_type = list(personality_type)
		cognitive_functions = {}

		if personality_type[preference['Attitude']] == 'E':
			if personality_type[preference['Lifestyle']] == 'J':
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Dom'] = 'Te'
					cognitive_functions['Inf'] = 'Fi'
				else:
					cognitive_functions['Dom'] = 'Fe'
					cognitive_functions['Inf'] = 'Ti'
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Aux'] = 'Si'
					cognitive_functions['Ter'] = 'Ne'
				else:
					cognitive_functions['Aux'] = 'Ni'
					cognitive_functions['Ter'] = 'Se'
			else:
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Dom'] = 'Se'
					cognitive_functions['Inf'] = 'Ni'
				else:
					cognitive_functions['Dom'] = 'Ne'
					cognitive_functions['Inf'] = 'Si'
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Aux'] = 'Ti'
					cognitive_functions['Ter'] = 'Fe'
				else:
					cognitive_functions['Aux'] = 'Fi'
					cognitive_functions['Ter'] = 'Te'
		else:
			if personality_type[preference['Lifestyle']] == 'J':
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Aux'] = 'Te'
					cognitive_functions['Ter'] = 'Fi'
				else:
					cognitive_functions['Aux'] = 'Fe'
					cognitive_functions['Ter'] = 'Ti'
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Dom'] = 'Si'
					cognitive_functions['Inf'] = 'Ne'
				else:
					cognitive_functions['Dom'] = 'Ni'
					cognitive_functions['Inf'] = 'Se'
			else:
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Aux'] = 'Se'
					cognitive_functions['Ter'] = 'Ni'
				else:
					cognitive_functions['Aux'] = 'Ne'
					cognitive_functions['Ter'] = 'Si'
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Dom'] = 'Ti'
					cognitive_functions['Inf'] = 'Fe'
				else:
					cognitive_functions['Dom'] = 'Fi'
					cognitive_functions['Inf'] = 'Te'

		return cognitive_functions


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