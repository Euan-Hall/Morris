import Node

el = Node.Element()
el.localName = "p"
el.namespace = "HTML"
print(el.getNodeType(), el.getNodeName())
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