from enum import Enum

class Color(Enum):
  RED = 1
  BLUE = 2
  GREEN = 3

class Size(Enum):
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

class Product:

  def __init__(self, name, color, size):
    self.name = name
    self.color = color
    self.size = size

# old approach to show that how complex it can go if we put everything in one place
# what if there is new attribute or we want size or color or something else, we have to change its implementation.
    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods
class ProductFilter:
  
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


class Specification:

  def is_satisfied(self, item):
    pass


class ColorSpecification(Specification):
  class __init__(self, color):
    self.color = color

  class is_satisfied(self, item):
    return self.item == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is green')

# ^ BEFORE

# v AFTER
bf = BetterFilter()

print('Green products (new):')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f' - {p.name} is green')

print('Large products:')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue = large & ColorSpecification(Color.BLUE)
for p in bf.filter(products, large_blue):
    print(f' - {p.name} is large and blue')


    
