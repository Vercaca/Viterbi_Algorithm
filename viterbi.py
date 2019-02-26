import operator

class Viterbi:
    def __init__(self, states, start_probs, trans_prob, emit_prob):
        self.__states, self.__start_prob, self.__trans_prob, self.__emit_prob\
            = states, start_probs, trans_prob, emit_prob

        self.__counter = 0

    def run(self, obs):
        self.__counter += 1
        states, start_probs, trans_prob, emit_prob \
            = self.__states, self.__start_prob, self.__trans_prob, self.__emit_prob

        if not obs:
            return None


        tmp_probs = {}

        # initial observation
        x = obs[0]
        for y in states:
            tmp_probs[y] = start_probs[y] * emit_prob[y][x]

        state, curr_prob = max(tmp_probs.items(), key=operator.itemgetter(1))
        process_results = [(state, curr_prob)]

        if len(obs) > 1:
            # other observations
            for x in obs[1:]:
                for y in states:
                    tmp_probs[y] = curr_prob * trans_prob[state][y] * emit_prob[y][x]
                state, curr_prob = max(tmp_probs.items(), key=operator.itemgetter(1))
                process_results.append((state, curr_prob))

        # print Report
        print_report(self.__counter, obs, process_results)

        return process_results[-1]

def print_report(patient_no, observations, process_results):
    print()
    print('\n' + '*' * 60 + '\n')
    print('Patient #{} with following observations: {}'.format(patient_no, observations))
    print()
    print('>>> Dignosis Reports')
    print('Date\t| Observation\t\t| Report')
    print('----\t| -----------\t\t| ------')
    for i, result in enumerate(process_results):
        print('Day {}\t| "{}"\t\t| {}'.format(i+1, observations[i], result))
    print()
    print('>>> Final Dignosis')
    print(process_results[-1])
    print('\n' + '*' * 60 + '\n')

def main():
    # setting parameters
    states = ('health', 'fever')
    start_probabilities = {'health': 0.6, 'fever': 0.4}
    transition_probabilities = {
                        'health' : {'health': 0.7, 'fever': 0.3},
                        'fever' : {'health': 0.4, 'fever': 0.6}
                        }
    emission_probabilities = {
                        'health' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
                        'fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
                        }

    # Build a Viterbi model (doctor)
    myViterbi = Viterbi(states, start_probabilities,
                    transition_probabilities, emission_probabilities)

    # Start Observations
    obs_1 = ('normal', 'cold', 'dizzy')   # features that
    dignosis = myViterbi.run(obs_1)

    obs_2 = ('dizzy',)
    dignosis = myViterbi.run(obs_2)



if __name__ == '__main__':
    main()
