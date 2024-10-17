from variables import var
from write_catalog import catalog_csv_w

def parse_catalog(city_code):
    
    data = var(city_code)

    products_list = []
    # Извлечение информации о продукте
    products = data['data']['category']['products']
    for product in products:
        # Извлечение необходимых данных о продукте
        product_id = product['id']
        product_name = product['name']
        product_url = "https://online.metro-cc.ru" + product['url']
        product_price = product['stocks'][0]['prices_per_unit']['price']
        product_promo = product['stocks'][0]['prices_per_unit']['old_price']
        
        if product_promo is None:
            product_promo = 0
        
        product_brand = product['manufacturer']['name']
        product = product_id, product_name, product_url, product_price, product_promo, product_brand
        products_list.append(product)
    
    if city_code == 31:
        name = 'moscow'
    else:
        name = 'spb'
    
    catalog_csv_w(products_list, name)