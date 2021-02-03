# importing module from the package
# use the methods of the module with the namespace
# this is recommended due to no collisions between function names
from shopping.more_shopping import new_shopping_cart

print(new_shopping_cart.get_item('Chocolate'))
