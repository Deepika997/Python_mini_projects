import random

def create_markov_chain(l1, order=1):
    markov = {}
    for i in range(len(l1) - order):
        prefix = tuple(l1[i:i+order])
        suffix = l1[i+order]
        if prefix not in markov:
            markov[prefix] = []
        markov[prefix].append(suffix)
    return markov

def generate_text(markov, length=100):
    prefix = random.choice(list(markov.keys()))
    result = list(prefix)
    for _ in range(length):
        next_word = random.choice(markov.get(prefix, ['']))
        result.append(next_word)
        prefix = tuple(result[-len(prefix):])
    return ' '.join(result)

x = "The sun shone brightly in the clear blue sky. A gentle breeze whispered through the trees, causing the leaves to sway. Children played in the park, their laughter filling the air. Nearby, a dog barked happily, chasing its tail. It was a simple and cheerful day in the neighborhood."
l1 = x.split()
order = 2
markov = create_markov_chain(l1, order)
generated = generate_text(markov, length=50)
print(generated)

