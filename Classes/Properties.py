class Product:
    def __init__(self, price):
        self.__price = price
        # self.set_price(price)

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # price = property(get_price, set_price)


product = Product(50)
product.price = 2
print(product.price)