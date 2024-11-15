from shop.models import Product, Profile

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_quantity)
        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            kart = str(self.cart)
            kart = kart.replace('\'', '\"')
            current_user.update(old_cart=str(kart))

    def db_add(self, product, quantity):
        product_id = str(product)
        product_quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_quantity)
        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            kart = str(self.cart)
            kart = kart.replace('\'', '\"')
            current_user.update(old_cart=str(kart))

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_product(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quantity(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_quantity = int(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_quantity
        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            kart = str(self.cart)
            kart = kart.replace('\'', '\"')
            current_user.update(old_cart=str(kart))
        stuff = self.cart
        return stuff
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        if self.request.user.is_authenticated:
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            kart = str(self.cart)
            kart = kart.replace('\'', '\"')
            current_user.update(old_cart=str(kart))