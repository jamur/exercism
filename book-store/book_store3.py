from itertools import combinations
from typing import List

PRICES = {k: int(800 * k * (1 - v)) for k, v in enumerate([0, .05, .1, .2, .25], 1)}

def total(books: List[int], shopping_price: int = 0) -> int:
    if not books:
        return shopping_price
    books_distinct = set(books)
    price_optimal = None
    for books_to_sell in [books_distinct] + list(combinations(books_distinct, 4)):
        books_remaining = books[:]
        for book in books_to_sell:
            books_remaining.remove(book)
        price = total(books_remaining, shopping_price + PRICES[len(books_to_sell)])
        price_optimal = price if price_optimal is None else min(price_optimal, price)
    return price_optimal

if __name__ == "__main__":
    # Exemplo de uso
    baskets = [
        [2, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 2, 2],
        [1,1,2,2,3,3,4,4,5]
    ]
    
    for basket in baskets:
        total_cost = total(basket)
        print(f"O custo total com o maior desconto é ${total_cost:.2f}")