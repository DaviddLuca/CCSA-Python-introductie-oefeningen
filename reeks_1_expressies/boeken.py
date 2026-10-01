book_price = 24.95
discount_rate = 0.4
nb_books = 60
shipping_cost = 3 +(nb_books-1) * 0.75
total_price = nb_books * book_price * (1-discount_rate) + shipping_cost

print(total_price)