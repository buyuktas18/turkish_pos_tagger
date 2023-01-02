# Application Project II
## Progress Report

### CKY Parser

As a first step, I implemented CKY parser. Then I will generate the grammar to cover all of the sentences. 

## Implementation

The Python code provided consists of four main components:

- The Rule class, which represents a rule in the grammar with a left-hand side (lhs) and a right-hand side (rhs).
  
- The ParseTree class, which represents a parse tree with a label (the symbol at the root of the tree) and a list of children (the sub-trees rooted at the children of the root).
  
- The CKY function, which implements the CKY algorithm.
  
- The buildParseTree function, which builds a parse tree from the table produced by the CKY algorithm.


### The Rule Class

The Rule class has a constructor (__init__) that takes two arguments: the left-hand side (lhs) and the right-hand side (rhs) of the rule. It stores these as instance variables.

```python
class Rule:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

```

### The ParseTree Class

The ParseTree class has a constructor (__init__) that takes a single argument: the label (label) of the root of the tree. It stores this as an instance variable and initializes an empty list of children (children).

The class has two methods:

- addChild, which adds a child to the list of children.
- __str__, which returns a string representation of the tree.

```python
class ParseTree:
    def __init__(self, label):
        self.label = label
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)
    
    def __str__(self):
        if not self.children:
            return self.label
        else:
            children_str = ' '.join(str(child) for child in self.children)
            return f'{self.label} ({children_str})'

```

### The CKY Function
The CKY function takes two arguments: a list of words (words) and a grammar (grammar) represented as a list of Rule objects. It returns a parse tree for the input string if it is grammatically well-formed according to the given grammar, or None if it is not.

After filling in the table for single words, the CKY function iterates over the possible spans of length 2 to len(words). For each span, it iterates over the start indices of the span and calculates the end index of the span. It then iterates over the split point of the span and gets the B and C sets from the table (B is the set of nonterminal symbols that could produce the words from index start to index split, and C is the set of nonterminal symbols that could produce the words from index split + 1 to index end).

Finally, it iterates over the rules that could potentially produce the span (i.e., rules with right-hand sides that consist of a symbol in B followed by a symbol in C) and adds the left-hand side of the rule to the table at the entry for the span (table[start][end]).

At the end of the CKY function, it checks if the S nonterminal (the start symbol of the grammar) is present in the table at the entry for the full span of the input string (table[0][len(words) - 1]). If it is, it calls the buildParseTree function to build a parse tree for the span, with S as the root, and returns the tree. If S is not present in the table, it returns None, indicating that the input string is not grammatically well-formed according to the given grammar.

```python
def CKY(words, grammar):
    # Initialize the table with empty sets
    table = [[set() for _ in range(len(words))] for _ in range(len(words))]

    # Iterate over the words and fill in the table
    for i, word in enumerate(words):
        # Find all the rules that could produce this word
        for rule in grammar:
            if word in rule.rhs:
                table[i][i].add(rule.lhs)

        # Iterate over the possible spans of length 2 to len(words)
        for span in range(2, len(words) + 1):
            # Iterate over the start indices of the span
            for start in range(len(words) - span + 1):
                # Calculate the end index of the span
                end = start + span - 1

                # Iterate over the split point of the span
                for split in range(start, end):
                    # Get the B and C sets from the table
                    B = table[start][split]
                    C = table[split + 1][end]

                    # Iterate over the rules that could potentially produce the span
                    for rule in grammar:
                        if rule.rhs[0] in B and rule.rhs[1] in C:
                            # Add the left-hand side of the rule to the table
                            table[start][end].add(rule.lhs)

    # Return the parse tree if it exists, or None if it doesn't
    if 'S' in table[0][len(words) - 1]:
        return buildParseTree(table, words, 0, len(words) - 1, 'S')
    else:
        return None

```

### The buildParseTree Function


The buildParseTree function takes five arguments:

table: the table produced by the CKY function, where table[i][j] is the set of nonterminal symbols that could produce the words from index i to index j inclusive.
words: the list of words (the input string).
start: the start index of the span for which to build the parse tree.
end: the end index of the span for which to build the parse tree.
nonterminal: the nonterminal symbol at the root of the parse tree.
The function first creates a new ParseTree object with the given nonterminal as the root. It then iterates over the rules in the grammar that could have produced the span (i.e., rules with a left-hand side equal to nonterminal).

For each of these rules, it checks if either symbol in the right-hand side is in the table at the entry for the span (table[start][end]). If it is, it recursively calls the buildParseTree function to build a parse tree for the symbol, and adds the resulting tree as a child of the current tree.

If neither symbol in the right-hand side is in the table, it means that both symbols must be terminal symbols (since all nonterminal symbols in the table are represented by their left-hand sides). In this case, the function adds the terminal symbols as children of the current tree.

Finally, the function returns the resulting parse tree.

```python
def buildParseTree(table, words, start, end, nonterminal):
    # Create a new parse tree with the given nonterminal as the root
    tree = ParseTree(nonterminal)

    # Iterate over the rules that could have produced the span
    for rule in grammar:
        if rule.lhs == nonterminal:
            # Check if the right-hand side of the rule is in the table
            if rule.rhs[0] in table[start][end]:
                # Recursively build the parse tree for the first symbol in the right-hand side
                child = buildParseTree(table, words, start, end, rule.rhs[0])
                tree.addChild(child)
            elif rule.rhs[1] in table[start][end]:
                # Recursively build the parse tree for the second symbol in the right-hand side
                child = buildParseTree(table, words, start, end, rule.rhs[1])
                tree.addChild(child)
            elif len(rule.rhs) == 2 and rule.rhs[0] in table[start][split] and rule.rhs[1] in table[split+1][end]:
                # Recursively build the parse trees for the two symbols in the right-hand side
                for split in range(start, end):
                    if rule.rhs[0] in table[start][split] and rule.rhs[1] in table[split+1][end]:
                        left_child = buildParseTree(table, words, start, split, rule.rhs[0])
                        right_child = buildParseTree(table, words, split+1, end, rule.rhs[1])
                        tree.addChild(left_child)
                        tree.addChild(right_child)

    return tree

```