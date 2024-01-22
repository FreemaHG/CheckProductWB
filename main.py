import json
from typing import Dict

import requests


ARTICLE = 23412083
SEARCH_PHRASE = "джинсы мужские зауженные черные"


def get_json_data(search_phrase: str = None) -> json:
    """
    Функция отправляет запрос на страницу поиска товара в WB и возвращает ответ в json-формате
    :param search_phrase: фраза для поиска товара (подставляется в URL)
    :return: ответ в формате json
    """

    _URL = f"https://search.wb.ru/exactmatch/ru/male/v4/search?TestGroup=no_test&TestID=no_test&appType=1&curr=" \
           f"rub&dest=-1299031&query={search_phrase}&resultset=catalog&sort=popular&" \
           f"spp=29&suppressSpellcheck=false&uclusters=8"
    _HEADERS = {
        "Accept": "*/*",
        "Accept-Language": "ru,en;q=0.9",
        "Connection": "keep-alive",
        "Origin": "https://www.wildberries.ru",
        "Referer": f"https://www.wildberries.ru",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36",
        "sec-ch-ua": "'Chromium';v='118', 'YaBrowser';v='23.11', 'Not=A?Brand';v='99', 'Yowser';v='2.5'",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
    }

    response = requests.get(url=_URL, headers=_HEADERS)

    return response.json()


def prepare_items(response: Dict) -> Dict:
    """
    Функция принимает json-данные о товарах и возвращает словарь с артикулом товара и его позиционным номером
    :param response: json с данными о товарах
    :return: словарь (ключ - артикул товара, значение - его позиционный номер)
    """
    products = {}
    products_raw = response.get("data", {}).get("products", None)

    if products_raw != None and len(products_raw) > 0:
        for i, product in enumerate(products_raw, 1):
            # Для дальнейшего удобства извлечения порядкового номера товара в выдаче
            # артикул сохраняем в виде ключа, а порядковый номер как значение
            products[product.get("id", None)] = i

    return products


def get_position(products: Dict, article: int) -> int | None:
    """
    Функция возвращает значение (порядковый номер) товара по ключу (артиклу)
    :param products: словарь вида {<артикул товара>: <порядковый номер в выдаче на странице поиска>}
    :param article: артикул товара
    :return: порядковый номер товара, если товар найден, иначе None
    """
    return products.get(article, None)


def main(article: int, search_phrase: str) -> int | str:
    """
    Функция принимает артикул товара и фразу для поиска товара в WB
    и возвращает порядковый номер товара на странице результатов
    :param article: артикул товара
    :param search_phrase: поисковая фраза
    :return: порядковый номер товара, если товар найден, иначе None
    """
    response_json = get_json_data(search_phrase=search_phrase)
    products_articles = prepare_items(response=response_json)
    position = get_position(products=products_articles, article=article)

    return position


if __name__ == "__main__":
    print(f"Поиск товара в WB с артикулом '{ARTICLE}' по фразе: '{SEARCH_PHRASE}'")

    product_position = main(article=ARTICLE, search_phrase=SEARCH_PHRASE)

    if product_position:
        print(f"Товар на позиции: {product_position}")
    else:
        print("Товар не найден")
