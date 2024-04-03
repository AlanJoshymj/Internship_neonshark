class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def sign_out(self):
        total_price = sum(item.product.price * item.quantity for item in self.items)
        self.items = []
        return total_price

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.cart = Cart()

class CartService:
    def add_product_to_cart(self, user, product, quantity):
        user.cart.add_item(product, quantity)

    def remove_product_from_cart(self, user, product_id):
        user.cart.remove_item(product_id)

    def sign_out_cart(self, user):
        return user.cart.sign_out()


if __name__ == "__main__":
  
    product1 = Product(1, "Phone", 500)
    product2 = Product(2, "Laptop", 1000)


    user = User(1, "John")

    cart_service = CartService()
    cart_service.add_product_to_cart(user, product1, 2)
    cart_service.add_product_to_cart(user, product2, 1)


    cart_service.remove_product_from_cart(user, 1)


    total_price = cart_service.sign_out_cart(user)
    print("Total Price:", total_price)
