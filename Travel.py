# Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

all_items = {
    'тент': 2,
    'спальник': 1.5,
    'еда': 1,
    'вода': 2,
    'ручка': 0.1,
    'тетрадь': 0.2
}


def fit_items_in_backpack(items, max_w):
    box = []
    all_weight = 0

    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)

    for thing, weight in sorted_items:
        if all_weight + weight <= max_w:
            box.append(thing)
            all_weight += weight

    return box, all_weight


max_weight = 5
backpack, total_weight = fit_items_in_backpack(all_items, max_weight)
print('В рюкзак уместятся:')

for item in backpack:
    print(item)
print(f'Вес {total_weight}/{max_weight}')
