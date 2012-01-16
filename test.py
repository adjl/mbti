# test.py

def create_sample(function, argument, sample_space):
	sample_results = {}

	for i in range(sample_space):
		result = str(function(argument))

		if sample_results.has_key(result):
			sample_results[result] += 1
		else:
			sample_results[result] = 1

	for result in sample_results.keys():
		sample_results[result] /= float(sample_space)

	return sample_results


def run_trial(function, argument, trials, sample_space):
	trial_results = {}

	for i in range(trials):
		sample = create_sample(function, argument, sample_space)

		for result in sample.keys():
			if trial_results.has_key(result):
				trial_results[result] += sample[result]
			else:
				trial_results[result] = sample[result]

	for result in trial_results.keys():
		trial_results[result] /= float(trials)

	return trial_results


def output_results(result_a, result_b):
	personality_type_probabilities = {
		'ESTJ': 0.13,
		'ESFJ': 0.12,
		'ISTJ': 0.085,
		'ISFJ': 0.07,

		'ESTP': 0.1,
		'ESFP': 0.11,
		'ISTP': 0.06,
		'ISFP': 0.06,

		'ENFJ': 0.04,
		'ENFP': 0.07,
		'INFJ': 0.01,
		'INFP': 0.02,

		'ENTJ': 0.04,
		'ENTP': 0.045,
		'INTJ': 0.015,
		'INTP': 0.025,
	}

	personality_types = [
		'ESTJ', 'ESFJ', 'ISTJ', 'ISFJ',
		'ESTP', 'ESFP', 'ISTP', 'ISFP',
		'ENFJ', 'ENFP', 'INFJ', 'INFP',
		'ENTJ', 'ENTP', 'INTJ', 'INTP'
	]

	header = '{:^9} {:^9} {:^9} {:10} {:^9} {:10}'.format('Type', 'Expected', 'Result A', '', 'Result B', '')

	print header
	print len(header) * '-'

	result_a_accuracy = result_b_accuracy = 0

	for personality_type in personality_types:
		result_a_difference = personality_type_probabilities[personality_type] - result_a[personality_type]
		result_b_difference = personality_type_probabilities[personality_type] - result_b[personality_type]

		if abs(result_a_difference) < abs(result_b_difference):
			result_a_accuracy += 1
		elif abs(result_a_difference) > abs(result_b_difference):
			result_b_accuracy += 1
		else:
			result_a_accuracy += 1
			result_b_accuracy += 1

		print '{:^9} {:<9f} {:<9f} {:<+10f} {:<9f} {:<+10f}'.format(personality_type, personality_type_probabilities[personality_type], \
		result_a[personality_type], result_a_difference, result_b[personality_type], result_b_difference)

	print
	print 'Result A accuracy: {}/{} ({:.2%})'.format(result_a_accuracy, len(personality_types), result_a_accuracy / float(len(personality_types)))
	print 'Result B accuracy: {}/{} ({:.2%})'.format(result_b_accuracy, len(personality_types), result_b_accuracy / float(len(personality_types)))


def test(trials=100, sample_space=100):
	from personality import PersonalityType

	result_a = run_trial(PersonalityType, False, trials, sample_space)
	result_b = run_trial(PersonalityType, True, trials, sample_space)
	output_results(result_a, result_b)
