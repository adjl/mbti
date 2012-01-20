# personality.py

"""Module containing a personality type class.

This module currently contains classes pertaining to the Myers-Briggs Type
Indicator and Jungian Cognitive Functions. Currently adding functionality for
the Keirsey Temperament Sorter. Another model of personality type will be added in
the future, namely the Enneagram of Personality.

Author: Helena 'Adei' Josol <helena.josol@gmail.com>

"""

class Personality:

	temperament_names = {
		'SJ': ['Guardian', 'Protector'],
		'SP': ['Artisan', 'Creator'],
		'NF': ['Idealist', 'Visionary'],
		'NT': ['Rational', 'Intellectual']
	}

	personality_type_names = {
		'SJ': {
			'ESTJ': ['Supervisor', 'Overseer', 'Guardian'],
			'ESFJ': ['Provider', 'Supporter', 'Caregiver'],
			'ISTJ': ['Inspector', 'Examiner', 'Duty Fulfiller'],
			'ISFJ': ['Protector', 'Defender', 'Nurturer']
		},
		'SP': {
			'ESTP': ['Promoter', 'Persuader', 'Doer'],
			'ESFP': ['Performer', 'Entertainer', 'Performer'],
			'ISTP': ['Crafter', 'Craftsman', 'Mechanic'],
			'ISFP': ['Composer', 'Artist', 'Artist']
		},
		'NF': {
			'ENFJ': ['Teacher', 'Mentor', 'Giver'],
			'ENFP': ['Champion', 'Advocate', 'Inspirer'],
			'INFJ': ['Counselor', 'Confidant', 'Protector'],
			'INFP': ['Healer', 'Dreamer', 'Idealist']
		},
		'NT': {
			'ENTJ': ['Fieldmarshal', 'Chief', 'Executive'],
			'ENTP': ['Inventor', 'Originator', 'Visionary'],
			'INTJ': ['Mastermind', 'Strategist', 'Scientist'],
			'INTP': ['Architect', 'Engineer', 'Thinker']
		}
	}

	preference_names = {
		'E': ['Extraversion', 'Extravert', 'Extraverted'],
		'I': ['Introversion', 'Introvert', 'Introverted'],
		'S': ['Sensing', 'Sensor'],
		'N': ['iNtuition', 'iNtuitor', 'iNtuitive'],
		'T': ['Thinking', 'Thinker'],
		'F': ['Feeling', 'Feeler'],
		'J': ['Judging', 'Judger'],
		'P': ['Perceiving', 'Perceiver']
	}

	cognitive_function_names = {
		'Se': 'Extraverted Sensing',
		'Si': 'Introverted Sensing',
		'Ne': 'Extraverted iNtuition',
		'Ni': 'Introverted iNtuition',
		'Te': 'Extraverted Thinking',
		'Ti': 'Introverted Thinking',
		'Fe': 'Extraverted Feeling',
		'Fi': 'Introverted Feeling'
	}

	temperament_probabilities = {
		'SJ': 0.405,
		'SP': 0.33,
		'NF': 0.14,
		'NT': 0.125
	}

	personality_type_probabilities = {
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


	def __init__(self):
		self.temperament = self.set_temperament()
		self.personality_type = self.set_personality_type(self.temperament)
		self.cognitive_functions = self.set_cognitive_functions(self.personality_type)


	def __str__(self):
		return self.personality_type


	def set_temperament(self):
		import random

		probability = 0
		while probability <= 0:						# probability can never be <= 0
			probability = abs(1 - random.random())	# results in range (0.0, 1.0]
		boundary = 0

		# find which temperament range probability lies
		for temperament in self.temperament_probabilities.keys():
			if boundary < probability <= boundary + self.temperament_probabilities[temperament]:
				return temperament
			boundary += self.temperament_probabilities[temperament]


	def set_personality_type(self, temperament):
		import random

		probability = 0
		while probability <= 0:
			probability = abs(1 - random.random())
		boundary = 0

		# find which personality type range probability lies
		for personality_type in self.personality_type_probabilities[temperament].keys():
			personality_type_probability = self.personality_type_probabilities[temperament][personality_type] / self.temperament_probabilities[temperament]
			if boundary < probability <= boundary + personality_type_probability:
				return personality_type
			boundary += personality_type_probability


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
					cognitive_functions['Dominant'] = 'Te'
					cognitive_functions['Inferior'] = 'Fi'
				else:
					cognitive_functions['Dominant'] = 'Fe'
					cognitive_functions['Inferior'] = 'Ti'
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Auxiliary'] = 'Si'
					cognitive_functions['Tertiary'] = 'Ne'
				else:
					cognitive_functions['Auxiliary'] = 'Ni'
					cognitive_functions['Tertiary'] = 'Se'
			else:
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Dominant'] = 'Se'
					cognitive_functions['Inferior'] = 'Ni'
				else:
					cognitive_functions['Dominant'] = 'Ne'
					cognitive_functions['Inferior'] = 'Si'
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Auxiliary'] = 'Ti'
					cognitive_functions['Tertiary'] = 'Fe'
				else:
					cognitive_functions['Auxiliary'] = 'Fi'
					cognitive_functions['Tertiary'] = 'Te'
		else:
			if personality_type[preference['Lifestyle']] == 'J':
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Auxiliary'] = 'Te'
					cognitive_functions['Tertiary'] = 'Fi'
				else:
					cognitive_functions['Auxiliary'] = 'Fe'
					cognitive_functions['Tertiary'] = 'Ti'
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Dominant'] = 'Si'
					cognitive_functions['Inferior'] = 'Ne'
				else:
					cognitive_functions['Dominant'] = 'Ni'
					cognitive_functions['Inferior'] = 'Se'
			else:
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Auxiliary'] = 'Se'
					cognitive_functions['Tertiary'] = 'Ni'
				else:
					cognitive_functions['Auxiliary'] = 'Ne'
					cognitive_functions['Tertiary'] = 'Si'
				if personality_type[preference['Judging']] == 'T':
					cognitive_functions['Dominant'] = 'Ti'
					cognitive_functions['Inferior'] = 'Fe'
				else:
					cognitive_functions['Dominant'] = 'Fi'
					cognitive_functions['Inferior'] = 'Te'

		return cognitive_functions
