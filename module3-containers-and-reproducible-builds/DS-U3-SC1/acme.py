from random import randint


class Product:
    """ Product of Acme:
            Name = Name of product
            price = cost to consumer
            weight = how many 1lb rocks it weighs
            flammability = Acme flammabilty risk scale unit value(tm)
            identifier = 'Unique-ish' id number
    """
    def __init__(self, name=None, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        """Calculates the price divided by the weight,
            and then returns a message:
                if the ratio is less than 0.5
                return "Not so stealable...",
             if it is greater or equal to 0.5
                but less than 1.0 return "Kinda stealable.",
             and otherwise return "Very stealable!"
        """
        if self.price/self.weight < 0.5:
            return "Not so stealable..."
        elif self.price/self.weight > 1:
            return "Very stealable!"
        return "Kinda stealable."

    def explode(self):
        """
         Calculates the flammability times the weight,
          and then returns a message:
            if the product is less than 10 return "...fizzle.",
           if it is greater or equal to 10 but less than 50 return "...boom!",
            and otherwise return "...BABOOM!!"
        """
        if self.flammability * self.weight < 10:
            return "...fizzle."
        elif self.flammability * self.weight > 50:
            return "...BABOOM!!"
        return "...boom!"


class BoxingGlove(Product):
    """Just a glove, man. What do you need help with? """

    def __init__(self, name=None, price=10, weight=10, flammability=0.5):
            super().__init__(
                name=name,
                price=price,
                weight=weight,
                flammability=flammability
            )

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight > 15:
            return "OUCH!"
        return "Hey that hurt!"
