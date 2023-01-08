from ParseTree import ParseTree
from grammar import grammar
from Node import Node

def CKY(words, grammar):
    # Initialize the table with empty sets
    table = [[set() for _ in range(len(words))] for _ in range(len(words))]

    # Iterate over the words and fill in the table
    for i, word in enumerate(words):
        # Find all the rules that could produce this word
        for rule in grammar:
            if word in rule.rhs:
                node = Node(rule.lhs)
                table[i][i].add(node)

        # Iterate over the possible spans of length 2 to len(words)
        for span in range(2, len(words) + 1):
            # Iterate over the start indices of the span
            for start in range(len(words) - span + 1):
                # Calculate the end index of the span
                end = start + span - 1

                # Iterate over the split point of the span
                for split in range(start, end):
                    # Get the B and C sets from the table
                    B = [c for c in table[start][split]]
                    C = [c for c in table[split + 1][end]]

                    B_data = [x.data for x in B]
                    C_data = [x.data for x in C]
                    # Iterate over the rules that could potentially produce the span
                    for rule in grammar:
                        if rule.rhs[0] in B_data and rule.rhs[1] in C_data:
                            # Add the left-hand side of the rule to the table
                            idx1 = B_data.index(rule.rhs[0])
                            idx2 = C_data.index(rule.rhs[1])

                            node = Node(rule.lhs)
                            left_node = B[idx1]
                            right_node = C[idx2]
                            node.prev = left_node
                            node.next = right_node
                            table[start][end].add(node)

    #print out the CKY table
    for i in range(len(words)):
        s = i * '\t'
        for j in range(len(words) - i):
            for k in table[i][i+j]:
                s += k.data 
            s += '\t'
        print(s)




    # Return the parse tree if it exists, or None if it doesn't
    result_tags = [x for x in table[0][len(words) - 1]]
    for n in result_tags:
        if 'S' == n.data:
            print(n.data)
            node = n
            print_tree(n)


def buildParseTree(table, words, start, end, nonterminal):
    # Create a new parse tree with the given nonterminal as the root
    tree = ParseTree(nonterminal)

    # Iterate over the rules that could have produced the span
    for rule in grammar:
        if rule.lhs == nonterminal:
            # Check if the right-hand side of the rule is in the table
            print(rule.rhs[0])
            if rule.rhs[0] in table[start]:
                print("foo")
                # Recursively build the parse tree for the first symbol in the right-hand side
                child = buildParseTree(table, words, start, end, rule.rhs[0])
                tree.addChild(child)
            elif rule.rhs[1] in table[start][end]:
                # Recursively build the parse tree for the second symbol in the right-hand side
                child = buildParseTree(table, words, start, end, rule.rhs[1])
                tree.addChild(child)
            else:
                # If the right-hand side of the rule is not in the table,
                # it must be a terminal symbol, so add it as a child of the tree
                tree.addChild(ParseTree(rule.rhs[0]))
                tree.addChild(ParseTree(rule.rhs[1]))

    return tree

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.next, level+1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.prev, level+1)

