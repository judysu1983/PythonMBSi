from xml.dom import minidom

xmldoc=minidom.parse("EOL.xml")

kml=xmldoc.getElementsByTagName("Eol")[0]

project=kml.getElementsByTagName("Project")[0]

components=project.getElementsByTagName("Component")

for component in components:
    ItemGroup=component.getElementsByTagName("ItemGroup")[0]
    Files=ItemGroup.getElementsByTagName("File")
    for tfile in Files:
        print(tfile)
