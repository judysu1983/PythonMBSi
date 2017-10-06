import xml.etree.cElementTree as ETXML

root = ETXML.Element("root")    # Create root element
sub = ETXML.SubElement(root, "sub")     # Create sub under root

ETXML.SubElement(sub, "sub1", name="sub1_name", category="CAT_A").text = "Sub_1 content" # Create sub1 and sub2 under sub
ETXML.SubElement(sub, "sub2", name="sub2_name", category="CAT_B").text = "Sub_2 content"

header = ETXML.SubElement(sub, "header")    # Create header under sub
ETXML.SubElement(header, "head1", name="header1").text = "Header_1 content" # Create head1 and head2 under header
ETXML.SubElement(header, "head2", name="header2").text = "Header_2 content"

body = ETXML.SubElement(sub, "body")        # Create body under sub

values = ETXML.SubElement(body, "values")   # Create values under body
for x in range(0, 4):
    ETXML.SubElement(values, "value", name="val"+str(x), type="string").text = "value_" + str(x) + " content"   # Create value under values

items = ETXML.SubElement(body, "items")     #Create items under body
for y in range(0, 3):
    ETXML.SubElement(items, "item", name="it"+str(x), type="int").text = str(y)     # Create item under items

rootWrite = ETXML.ElementTree(root)

rootWrite.write("createXml.xml")
