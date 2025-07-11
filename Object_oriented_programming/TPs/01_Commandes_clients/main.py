# main.py

from classes.OrderSystem import OrderSystem
from classes.Product import Product
from classes.Order import Order
from services.csv_service import *
from services.user_menu_service import *

def exit_to_main():
    input("Veuillez appuyer sur 'Entrée' afin de revenir au menu principal :")
    main()

def main():
    products : list[Product] = []
    orders : list[Order] = []

    products_file_path = r"./Object_oriented_programming/TPs/01_Commandes_clients/data/products.csv"
    orders_file_path = r"./Object_oriented_programming/TPs/01_Commandes_clients/data/orders.csv"

    if file_exists(products_file_path) and file_is_not_empty(products_file_path) :
        products = items_list(products_file_path)
    else:
        create_file_with_header(products_file_path, ["id", "name", "price", "stock"])
    
    if file_exists(orders_file_path) and file_is_not_empty(orders_file_path):
        orders = items_list(orders_file_path)
    else:
        create_file_with_header(orders_file_path, ["order_id", "product_id", "quantity", "customer"])
    
    order_system = OrderSystem(products, orders)

    print("=== GESTION DES STOCKS ET COMMANDES ===")
    print()
    print("Que souhaitez-vous faire ?")
    print(" 1. Visualiser les stocks")
    print(" 2. Visualiser les commandes")
    print(" 3. Ajouter un nouveau produit")
    print(" 4. Ajouter un produit existant")
    print(" 5. Enregistrer une commande client")
    print(" 0. Quitter")

    while True:
        choice = int(input("Votre réponse : "))
        if 0 <= choice <= 5:
            break

    match choice:
        case 0:
            exit()
        case 1:
            order_system.print_products()
            print()
            exit_to_main()
        case 2:
            order_system.print_orders()
            print()
            exit_to_main()
        case 3:
            new_product = create_product()
            products = order_system.add_product(new_product)
            update_products_file(products_file_path, products)
            print()
            exit_to_main()
        case 4:
            product_id = select_product_id()
            amount = select_amount()
            products = order_system.add_stock(product_id, amount)
            update_products_file(products_file_path, products)
            print()
            exit_to_main()
        case 5:
            new_order = create_order()
            products, orders = order_system.add_order(new_order)
            update_products_file(products_file_path, products)
            update_orders_file(orders_file_path, orders)
            print()
            exit_to_main()

main()

