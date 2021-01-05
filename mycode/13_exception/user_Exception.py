# User-defined Exception class

class NavigatePriceException(Exception):
    # constructor
    def __init__(self):
        print("Price can't be negative")
        raise AttributeError


def calc_price(value):
    price = value * 100
    if price < 0:
        # NavigatePriceException 강제 발생
        raise NavigatePriceException
    return price


print(calc_price(10))
print(calc_price(-12))
