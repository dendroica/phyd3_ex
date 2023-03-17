import xml.dom.minidom as m
def getText(nodelist):
     rc = []
     for node in nodelist:
         if node.nodeType == node.TEXT_NODE:
             rc.append(node.data)
     return ''.join(rc)

tree = m.parse(r"/home/jess/Documents/phyd3_ex/euteleostomi.xml")
p_list = doc.getElementsByTagName("name")
for item in p_list:
     getText(item.childNodes)
