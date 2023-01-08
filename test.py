from CKY import CKY
from grammar import grammar


# Parse the input string using the CKY algorithm
parse_tree = CKY("yüksek sesle müzik dinleme".split(), grammar)

# Print the parse tree
print(parse_tree)

# Output: S (NP (DT the) (NN dog)) (VP (VBP barks))
