class Cat:
    def __init__(self, name, breed, haircut, age):
        self.__name = name
        self.__breed = breed
        self.__haircut = haircut
        self.__age = age

    def grow(self):
        self.__age+=1

    @property
    def age(self):
        return self.__age

    def groom(self, new_groom):
        if new_groom not in ['fluffy', 'bold', 'middle']:
            raise Exception('what you did to my sweet kitten')
        self.__haircut = new_groom

    @property
    def haircut(self):
        return self.__haircut