# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open(r'test_file/task_3.txt', 'r', encoding='utf-8') as price_list:
    purchases = [[]]
    sum_purchase = []
    for purchase in price_list.readlines():
        if purchase == '\n':
            purchases.append([])
        else:
            purchases[-1].append(int(purchase))
    for purchase in purchases:
        sum_purchase.append(sum(purchase))
    sum_purchase_sort = sorted(sum_purchase, reverse=True)
    three_most_expensive_purchases = sum(sum_purchase_sort[:3])


assert three_most_expensive_purchases == 202346