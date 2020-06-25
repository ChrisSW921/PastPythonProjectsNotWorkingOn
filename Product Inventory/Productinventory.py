files = ['store1.txt','store2.txt','store3.txt']
master_product_list = []
inventories = []


class product:
    def __init__(self, price, ID, quantity,genre):
        self.price = float(price)
        self.ID = int(ID)
        self.quantity = int(quantity)
        self.genre = genre
        
    def __repr__(self):
        return f'Price: {self.price}  ID: {self.ID}  Quantity: {self.quantity}  Genre: {self.genre}'
    
class inventory:
    def __init__(self, products):
        self.products = products
        
    def show_genre_inv(self,genre):
        self.inv = 0
        for item in self.products:
            if item.genre == genre:
                self.inv += item.quantity
        print(f'{genre} in stock: {self.inv}')
    
    def compute_full_value(self):
        self.sum = 0
        for product in self.products:
            self.sum += (product.price * product.quantity)
        print(f'Full value of inventory: ${self.sum}')
    
    def show_full_quantity(self):
        self.sum = 0
        for product in self.products:
            self.sum += product.quantity
        print(f'Full quantity of inventory: {self.sum}')
    
    def show_all_prods(self):
        print("Full Inventory")
        print('-----------------------------------------')
        for product in self.products:
            print(product)
    
class store:
    def __init__(self,inventory):
        self.inventory = inventory
        
    def show_genre_inv(self,genre):
        self.inventory.show_genre_inv(genre)
    
    def compute_full_value(self):
        self.inventory.compute_full_value()
    
    def show_full_quantity(self):
        self.inventory.show_full_quantity()
    
    def show_all_prods(self):
        self.inventory.show_all_prods() 
        
    
def load_products():   
    for item in files:
        raw_products= []
        new_inv = []
        with open(item, 'r') as prods:
            for line in prods:
                raw_products.append(line.strip().split(','))
            for item in raw_products:
                new_inv.append(product(item[0],item[1],item[2],item[3]))
        master_product_list.append(new_inv)
                
def load_inventories(products):
    for item in products:
        inventories.append(inventory(item))
        
def find_product_by_id(ID):
    for item in store1_list:
        if item.ID == ID:
            return item       
            
load_products()
load_inventories(master_product_list)

store1 = store(inventories[0])
store2 = store(inventories[1])
store3 = store(inventories[2])

store1.show_all_prods()
store2.show_all_prods()
store3.show_all_prods()

store1.show_genre_inv('Food')
store1.compute_full_value()
store1.show_full_quantity()




