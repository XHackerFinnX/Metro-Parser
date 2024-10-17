import requests
import json

def var(city_code):
    url = 'https://api.metro-cc.ru/products-api/graph'
    payload = {
        "query": "query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: ["
                "FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, "
                "$eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\n    category (storeId: "
                "$storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, "
                "isPromo: $is_action, priceLevels: $price_levels) {\n      id\n      name\n      slug\n      "
                "id\n      parent_id\n      meta {\n        description\n        h1\n        title\n        "
                "keywords\n      }\n      disclaimer\n      description {\n        top\n        main\n        "
                "bottom\n      }\n      breadcrumbs {\n        category_type\n        id\n        name\n        "
                "parent_id\n        parent_slug\n        slug\n      }\n      promo_banners {\n        id\n      "
                "  image\n        name\n        category_ids\n        virtual_ids\n        type\n        "
                "sort_order\n        url\n        is_target_blank\n        analytics {\n          name\n         "
                " category\n          brand\n          type\n          start_date\n          end_date\n        "
                "}\n      }\n\n\n      dynamic_categories(from: 0, size: 9999) {\n        slug\n        name\n   "
                "     id\n      }\n      filters {\n        facets {\n          key\n          total\n          "
                "filter {\n            id\n            name\n            display_title\n            is_list\n    "
                "        is_main\n            text_filter\n            is_range\n            category_id\n       "
                "     category_name\n            values {\n              slug\n              text\n              "
                "total\n            }\n          }\n        }\n      }\n      total\n      prices {\n        "
                "max\n        min\n      }\n      pricesFiltered {\n        max\n        min\n      }\n      "
                "products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: "
                "$filters)  {\n        health_warning\n        limited_sale_qty\n        id\n        slug\n      "
                "  name\n        name_highlight\n        article\n        is_target\n        category_id\n       "
                " url\n        images\n        pick_up\n        icons {\n          id\n          "
                "badge_bg_colors\n          caption\n          image\n          type\n          "
                "is_only_for_sales\n          stores\n          caption_settings {\n            colors\n         "
                "   text\n          }\n          stores\n          sort\n          image_png\n          "
                "image_svg\n          description\n          end_date\n          start_date\n          status\n  "
                "      }\n        manufacturer {\n          id\n          image\n          name\n        }\n     "
                "   packing {\n          size\n          type\n          pack_factors {\n            instamart\n "
                "         }\n        }\n        stocks {\n          value\n          text\n          "
                "eshop_availability\n          scale\n          prices_per_unit {\n            old_price\n       "
                "     offline {\n              price\n              old_price\n              type\n              "
                "offline_discount\n              offline_promo\n            }\n            price\n            "
                "is_promo\n            levels {\n              count\n              price\n            }\n       "
                "     discount\n          }\n          prices {\n            price\n            is_promo\n       "
                "     old_price\n            offline {\n              old_price\n              price\n           "
                "   type\n              offline_discount\n              offline_promo\n            }\n           "
                " levels {\n              count\n              price\n            }\n            discount\n      "
                "    }\n        }\n      }\n    }\n  }",
        "variables": {
            "isShouldFetchOnlyProducts": True,
            "slug": "myaso",
            "storeId": city_code,
            "sort": "default",
            "size": 1000,
            "from": 0,
            "in_stock": True,
            "eshop_order": None,
            "is_action": None,
            "price_levels": None
        }
    }

    cookie = "_slid_server=6710dce6c57257d51a071779;"\
                    "pdp_abc_20=0; plp_bmpl_bage=0;"\
                    "_slid=6710dce6c57257d51a071779;"\
                    "metro_user_id=c341d14868dfcb6900238dcf5926c821;"\
                    "sl_top_promobanner_closed=true;"\
                    "_slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1729181500%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1729181500;"\
                    "XSRF-TOKEN=eyJpdiI6IldRdUpxOVB5aitFMm92TXhWd2dPckE9PSIsInZhbHVlIjoiTUYxYU5pUWRadGxEcndnL3ZnREZ5d1R3cndHNi9ITGJuVmdDY0FleVV0QU5zOFpSQzR2OFo5V0hmVk5VMUFFUFdvRmdEMWpVV3dJcW1xcUpkdFdrRVAxNk5XVGdrdlhXc3h3ZUJ2dFkvYnFMVzNrbUp5R1pWWXBOaWFtdEh6ZHoiLCJtYWMiOiI3MzMzM2NlOGVjOWYzNmY5ODc2YWYwMDVkYzYzMzllYjlkYjhlNWVmNDczZjg3ZTA2ZmJkZTcwNzI2ZGQxYzYzIiwidGFnIjoiIn0%3D;"\
                    "metro_api_session=kljmUopOgZEqpbr5WIVDn2g1U0rpd7eIwYm711iM;"\
                    "metroStoreId=10;"\
                    "_slsession=10B40332-814B-4EC1-BE5F-CFA0A825A44D;"

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/114.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Content-Type': 'application/json',
            'Referer': 'https://online.metro-cc.ru/',
            'Origin': 'https://online.metro-cc.ru',
            'Cookie': cookie,
        }
    
    response = requests.post(url, json=payload, headers=headers)
    data = json.loads(response.text)
    
    return data