#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead", "could"]


def NextWordProbability(sampletext, word):

    words = sampletext.split()
    likelihood = {}

    # Subtract 1 from length because last word doesn't have a 'next word'
    for i in range(len(words) - 1):

        this_word = words[i]
        if word == this_word:
            next_word = words[i + 1]

            if next_word not in likelihood:
                likelihood[next_word] = 0
            likelihood[next_word] += 1

    # convert total of occurences into probability
    probability = {}
    for w, t in likelihood.items():
        probability[w] = float(t) / sum(likelihood.values())

    return probability

NextWordProbability(sample_memo, 'and')


def LaterWords(sample, word, distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum
    # likelihood exercise.
    previous_words_prob = NextWordProbability(sample, word)

    # print 'total probs', sum(previous_words_prob.values())  # should be 1

    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.

    for i in range(1, distance):
        final = {}  # Where we'll put the words that should be considered for position

        for previous_word, previous_word_prob in previous_words_prob.items():
            this_words_prob = NextWordProbability(sample, previous_word)

            # For each word we have to multiply its probability with the one
            # before
            for this_word, this_word_prob in this_words_prob.items():
                final[this_word] = this_word_prob * previous_word_prob

        previous_words_prob = final

    # print 'total probs', sum(final.values())  # should be 1

    return max(final, key=final.get)


print LaterWords(sample_memo, "ahead", 2)
