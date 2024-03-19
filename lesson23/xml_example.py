from xml.etree import ElementTree
import xmltodict
tree = ElementTree.parse('example.xml')
root = tree.getroot()
for food in root:
    print(food)
decoded_to_str = ElementTree.tostring(root).decode()
changes = decoded_to_str.replace('<calories>950</calories>', '<calories>2000</calories>')
encoded_res = ElementTree.fromstring(changes)
print(type(encoded_res))
food_five = encoded_res[4]
for parameter in food_five:
    if parameter.tag == 'calories':
        print(parameter.text, parameter.attrib['waffle_name'])

parsed_xml = xmltodict.parse(decoded_to_str)
print(parsed_xml)
