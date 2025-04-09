import nodes

document = nodes.Document(url="gorp")
html = nodes.Element("HTML", parent=document)
head = nodes.Element("Head", parent=html)
body = nodes.Element("Body", parent=html)
heading = nodes.Element("h1", parent=body)
text = nodes.Text("Hello there!", parent=heading)

# {
#   "Type" : Document,
#   "Children" : {
#       { "Type" : HTML, 
#         "Children" : { ... }
#       }
# }


print(document.generateDict())