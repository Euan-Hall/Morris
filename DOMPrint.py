import nodes


el = nodes.Element()
print(el.getNodeType())
# Generate DOM Tree from tokenizer
def generateDict(self):
    child = []

# If this node has children, generate a dictionary
    if self.children:
        for c in self.children:
            temp =c.generateDict()
            child.append(temp)

    return {"Type" : type(self), 
            "Children" : child}