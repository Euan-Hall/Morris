import Node

class Parser:
    def __init__(self, input=""):
        self.pos = 0
        self.input = input

    def next_char(self):
        # Returns next char, or none for EOL.
        if len(self.input) > 0 or self.pos < len(self.input)-1:
            return self.input[self.pos+1]
        return None
    
    def starts_with(self, s):
        return self.input[self.pos] == s
    
    def parse_node(self):
        if self.starts_with("<"):
            self.parse_element()
        else:
            self.parse_text()

    def expect(self, c):
        if self.starts_with(c):
            self.pos += len(c)
        else:
            raise ValueError(f"Expected {c} at {self.post} but got none")
        
    def parse_name(self):
        name = ""
        inp = self.input[self.pos:]
        for c in inp:
            # If C is whitespace:
            # Ignores symbols and numbers, for now.
            if c == " ":
                self.pos += len(name)+1
                break
            if c == ">":
                self.pos += len(name)
                break 

            name += c
        return name
            

    def parse_attr(self):
        attr_list = []
        inp = self.input[self.pos:]
        
        # Handling multiple attr
        while not self.next_char(">"):
            name = self.parse_name()
            self.expect("=")
            value = self.parse_attr_value()
            attr_list.append((name, value))

    def parse_attr_value(self):
        pass

    def parse_element(self):
        # Allowed: [a-z]|A-Z]. \ only at the beginning.

        # Opening tag
        self.expect("<")
        tag_name = self.parse_name()        
        attr = self.parse_attr()
        self.expect("<")

        # Children / Contents
        children = self.parse_node()

        # Opening tag
        self.expect("<\\")
        self.expect(tag_name)
        self.expect(">")
        
        return Node.Element(tag_name, attr)

    def parse_text(self):
        # If < in input, throw erorr. Else make a Text Node.
        if "<" in self.input:
            raise ValueError("Text element cannot contain '<'. Please use \<.")
        return Node.Text(self.input)
        


# <html>
# <head>
# </head>
# <body>
# hello 
# </body>
# </html>
#
#
#