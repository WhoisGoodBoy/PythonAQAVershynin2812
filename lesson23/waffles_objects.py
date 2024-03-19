from xml.etree import ElementTree
class Breakfast():
    def __init__(self, name, price, description, calories):
        self.name = name
        self.price = price
        self.description = description
        self.calories = calories

    @classmethod
    def parse_from_xml(cls, path):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        list_of_breakfasts = []
        for food in root.iter('food'):
            food_dict = {}
            for food_parameter in food:
                food_dict[food_parameter.tag] = food_parameter.text
            list_of_breakfasts.append(cls(**food_dict))
        return list_of_breakfasts

breakfasts = Breakfast.parse_from_xml('example.xml')
print(breakfasts)
