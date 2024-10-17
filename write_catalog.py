import csv

def catalog_csv_w(product_list, name_city):
    
    with open(file=f"data/{name_city}.csv", encoding="utf-8", mode="w", newline='') as file_write:
        
        file = csv.writer(file_write, delimiter=',', quotechar='"')
        file.writerow(['ID товара', 'Наименование', 'Ссылка на товар', 'Регулярная цена', 'Промо цена', 'Бренд'])
        
        for i in product_list:
            prod_l = list(i)
            file.writerow(prod_l)
        