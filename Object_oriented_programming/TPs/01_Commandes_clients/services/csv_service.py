import csv, os
from classes.Product import Product
from classes.Order import Order

def items_list(file_path):
    items = []
    with open(file_path, "r", encoding="UTF_8") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)

        for row in reader:
            if 'products' in file_path.lower():
                product = Product(
                    id=int(row[0]), 
                    name=row[1], 
                    price=float(row[2]), 
                    stock=int(row[3])
                )
                items.append(product)
            elif 'orders' in file_path.lower():
                order = Order(
                    order_id=int(row[0]), 
                    product_id=int(row[1]), 
                    quantity=int(row[2]), 
                    customer=row[3]
                )
                items.append(order)
            
        return items

def file_exists(file_path):
    return os.path.exists(file_path)

def file_is_not_empty(file_path):
    return os.path.getsize(file_path) != 0

def create_file_with_header(file_path : str, columns : list[str]):
    with open(file_path, "a", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(columns)

def update_products_file(file_path, products : list[Product]):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "price", "stock"])
        for product in products:
            writer.writerow([product.id, product.name, product.price, product.stock])
    
def update_orders_file(file_path, orders : list[Order]):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id_order", "id_produit", "quantity", "customer"])
        for order in orders:
            writer.writerow([order.order_id, order.product_id, order.quantity, order.customer])