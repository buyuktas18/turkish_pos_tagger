from Rule import Rule


# Define the grammar as a list of Rule objects
grammar = [
    Rule('S', ['NP', 'VP']),
    Rule('NP', ['DT', 'NN']),
    Rule('VP', ['VBP', 'NP']),
    Rule('DT', ['the']),
    Rule('NN', ['dog']),
    Rule('VP', ['barks'])
]