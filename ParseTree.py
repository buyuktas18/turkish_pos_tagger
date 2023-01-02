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