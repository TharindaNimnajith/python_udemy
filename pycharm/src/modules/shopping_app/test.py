from shopping import shopping_cart
from shopping.more_shopping import new_shopping_cart

if __name__ == '__main__':
    print(shopping_cart.buy('item'))
    print(new_shopping_cart.get_item('abc'))

    print(__name__)

    if __name__ == '__main__':
        print('test')
