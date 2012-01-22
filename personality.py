# personality.py

"""Module containing a personality type class.

This module currently contains classes pertaining to the Myers-Briggs Type
Indicator and Jungian Cognitive Functions. Currently adding functionality for
the Keirsey Temperament Sorter. Another model of personality type will be added in
the future, namely the Enneagram of Personality.

Author: Helena 'Adei' Josol <helena.josol@gmail.com>

"""

PREF_STR_UPPER_BOUNDARY = 100
PREF_STR_LOWER_BOUNDARY = PREF_STR_UPPER_BOUNDARY / 2 + 1

class Personality:

	_temperament_names = {
		'SP': ['Artisan', 'Creator'],
		'SJ': ['Guardian', 'Protector'],
		'NF': ['Idealist', 'Visionary'],
		'NT': ['Rational', 'Intellectual']
	}

	_personality_type_names = {
		'SP': {
			'ESFP': ['Performer', 'Entertainer', 'Performer'],
			'ESTP': ['Promoter', 'Persuader', 'Doer'],
			'ISFP': ['Composer', 'Artist', 'Artist'],
			'ISTP': ['Crafter', 'Craftsman', 'Mechanic']
		},
		'SJ': {
			'ESFJ': ['Provider', 'Supporter', 'Caregiver'],
			'ESTJ': ['Supervisor', 'Overseer', 'Guardian'],
			'ISFJ': ['Protector', 'Defender', 'Nurturer'],
			'ISTJ': ['Inspector', 'Examiner', 'Duty Fulfiller']
		},
		'NF': {
			'ENFP': ['Champion', 'Advocate', 'Inspirer'],
			'ENFJ': ['Teacher', 'Mentor', 'Giver'],
			'INFP': ['Healer', 'Dreamer', 'Idealist'],
			'INFJ': ['Counselor', 'Confidant', 'Protector']
		},
		'NT': {
			'ENTP': ['Inventor', 'Originator', 'Visionary'],
			'ENTJ': ['Fieldmarshal', 'Chief', 'Executive'],
			'INTP': ['Architect', 'Engineer', 'Thinker'],
			'INTJ': ['Mastermind', 'Strategist', 'Scientist']
		}
	}

	_preference_names = {
		'E': ['Extraversion', 'Extravert', 'Extraverted'],
		'I': ['Introversion', 'Introvert', 'Introverted'],
		'S': ['Sensing', 'Sensor'],
		'N': ['iNtuition', 'iNtuitor', 'iNtuitive'],
		'F': ['Feeling', 'Feeler'],
		'T': ['Thinking', 'Thinker'],
		'P': ['Perceiving', 'Perceiver'],
		'J': ['Judging', 'Judger']
	}

	_cognitive_function_names = {
		'Se': 'Extraverted Sensing',
		'Si': 'Introverted Sensing',
		'Ne': 'Extraverted iNtuition',
		'Ni': 'Introverted iNtuition',
		'Fe': 'Extraverted Feeling',
		'Fi': 'Introverted Feeling',
		'Te': 'Extraverted Thinking',
		'Ti': 'Introverted Thinking'
	}

	_temperament_probabilities = {
		'SP': {'All': 0.33, 'Male': 0.34, 'Female': 0.32},
		'SJ': {'All': 0.405, 'Male': 0.375, 'Female': 0.435},
		'NF': {'All': 0.14, 'Male': 0.105, 'Female': 0.175},
		'NT': {'All': 0.125, 'Male': 0.18, 'Female': 0.07}
	}

	_personality_type_probabilities = {
		'SP': {
			'ESFP': {'All': 0.11, 'Male': 0.08, 'Female': 0.14},
			'ESTP': {'All': 0.1, 'Male': 0.125, 'Female': 0.075},
			'ISFP': {'All': 0.06, 'Male': 0.05, 'Female': 0.07},
			'ISTP': {'All': 0.06, 'Male': 0.085, 'Female': 0.035}
		},
		'SJ': {
			'ESFJ': {'All': 0.12, 'Male': 0.07, 'Female': 0.17},
			'ESTJ': {'All': 0.13, 'Male': 0.16, 'Female': 0.1},
			'ISFJ': {'All': 0.07, 'Male': 0.04, 'Female': 0.1},
			'ISTJ': {'All': 0.085, 'Male': 0.105, 'Female': 0.065}
		},
		'NF': {
			'ENFP': {'All': 0.07, 'Male': 0.06, 'Female': 0.08},
			'ENFJ': {'All': 0.04, 'Male': 0.025, 'Female': 0.055},
			'INFP': {'All': 0.02, 'Male': 0.015, 'Female': 0.025},
			'INFJ': {'All': 0.01, 'Male': 0.005, 'Female': 0.015}
		},
		'NT': {
			'ENTP': {'All': 0.045, 'Male': 0.06, 'Female': 0.03},
			'ENTJ': {'All': 0.04, 'Male': 0.055, 'Female': 0.025},
			'INTP': {'All': 0.025, 'Male': 0.04, 'Female': 0.01},
			'INTJ': {'All': 0.015, 'Male': 0.025, 'Female': 0.005}
		}
	}


	def __init__(self, gender='All'):
		self._temperament = self._set_temperament(gender)
		self._personality_type = self._set_personality_type(self._temperament, gender)
		self._preference_strengths = self._set_preference_strengths(self._personality_type)
		self._cognitive_functions = self._set_cognitive_functions(self._personality_type)


	def __str__(self):
		return self._personality_type


	def _set_temperament(self, gender):
		import random

		probability = 0
		while probability <= 0:						# probability can never be <= 0
			probability = abs(1 - random.random())	# results in range (0.0, 1.0]
		boundary = 0

		# find which temperament range probability lies
		for temperament in self._temperament_probabilities.keys():
			if boundary < probability <= boundary + self._temperament_probabilities[temperament][gender]:
				return temperament
			boundary += self._temperament_probabilities[temperament][gender]


	def _set_personality_type(self, temperament, gender):
		import random

		probability = 0
		while probability <= 0:
			probability = abs(1 - random.random())
		boundary = 0

		# find which personality type range probability lies
		for personality_type in self._personality_type_probabilities[temperament].keys():
			personality_type_probability = self._personality_type_probabilities[temperament][personality_type][gender] / self._temperament_probabilities[temperament][gender]
			if boundary < probability <= boundary + personality_type_probability:
				return personality_type
			boundary += personality_type_probability


	def _set_preference_strengths(self, personality_type):
		import random

		personality_type = list(personality_type)
		preference_strengths = {}

		for preference in personality_type:
			preference_strengths[preference] = random.randint(PREF_STR_LOWER_BOUNDARY, PREF_STR_UPPER_BOUNDARY)

		return preference_strengths


	def _set_cognitive_functions(self, personality_type):
		preference = {
			'Attitude': 0,
			'Perceiving': 1,
			'Judging': 2,
			'Lifestyle': 3
		}

		personality_type = list(personality_type)
		cognitive_functions = {}

		if personality_type[preference['Attitude']] == 'E':
			if personality_type[preference['Lifestyle']] == 'P':
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Dominant'] = 'Se'
					cognitive_functions['Inferior'] = 'Ni'
				else:
					cognitive_functions['Dominant'] = 'Ne'
					cognitive_functions['Inferior'] = 'Si'
				if personality_type[preference['Judging']] == 'F':
					cognitive_functions['Auxiliary'] = 'Fi'
					cognitive_functions['Tertiary'] = 'Te'
				else:
					cognitive_functions['Auxiliary'] = 'Ti'
					cognitive_functions['Tertiary'] = 'Fe'
			else:
				if personality_type[preference['Judging']] == 'F':
					cognitive_functions['Dominant'] = 'Fe'
					cognitive_functions['Inferior'] = 'Ti'
				else:
					cognitive_functions['Dominant'] = 'Te'
					cognitive_functions['Inferior'] = 'Fi'
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Auxiliary'] = 'Si'
					cognitive_functions['Tertiary'] = 'Ne'
				else:
					cognitive_functions['Auxiliary'] = 'Ni'
					cognitive_functions['Tertiary'] = 'Se'
		else:
			if personality_type[preference['Lifestyle']] == 'P':
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Auxiliary'] = 'Se'
					cognitive_functions['Tertiary'] = 'Ni'
				else:
					cognitive_functions['Auxiliary'] = 'Ne'
					cognitive_functions['Tertiary'] = 'Si'
				if personality_type[preference['Judging']] == 'F':
					cognitive_functions['Dominant'] = 'Fi'
					cognitive_functions['Inferior'] = 'Te'
				else:
					cognitive_functions['Dominant'] = 'Ti'
					cognitive_functions['Inferior'] = 'Fe'
			else:
				if personality_type[preference['Judging']] == 'F':
					cognitive_functions['Auxiliary'] = 'Fe'
					cognitive_functions['Tertiary'] = 'Ti'
				else:
					cognitive_functions['Auxiliary'] = 'Te'
					cognitive_functions['Tertiary'] = 'Fi'
				if personality_type[preference['Perceiving']] == 'S':
					cognitive_functions['Dominant'] = 'Si'
					cognitive_functions['Inferior'] = 'Ne'
				else:
					cognitive_functions['Dominant'] = 'Ni'
					cognitive_functions['Inferior'] = 'Se'

		return cognitive_functions


	def get_temperament(self):
		return self._temperament


	def get_personality_type(self):
		return self._personality_type


	def get_preference_strengths(self):
		return self._preference_strengths


	def get_cognitive_functions(self):
		return self._cognitive_functions
