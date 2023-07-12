# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

def main():
    print(f'Список всех предметов - {all_items(items)}')
    print(f'Список уникальных предметов - {unique_item(items)}')
    print(f'Отсутствует {without_item(items)}')


def all_items(items):
    all_item = [item for sublist in items.values() for item in sublist]
    return all_item


def unique_item(items):
    unique_items = []
    for item in set(sum(items.values(), ())):
        count = sum(item in friends_items for friends_items in items.values())
        if count == 1:
            unique_items.append(item)
    return unique_items


def without_item(items):
    friend_count = len(items)
    item_count = {}

    for friend in items:
        for item in items[friend]:
            item_count[item] = item_count.get(item, 0) + 1

    common_items = [item for item, count in item_count.items() if count == friend_count - 1]

    missing_item = None

    for friend in items:
        if not any(item in items[friend] for item in common_items):
            missing_item = friend
            break
    return common_items, missing_item


items = {
    'Алекс': ('нож', 'репелент', 'компас', 'вода', 'салфетки'),
    'Иосиф': ('мыло', 'сковорода', 'котелок', 'вода', 'галеты'),
    'Споттер': ('гантели', 'курица', 'вода', 'салат', 'компас')}

if __name__ == '__main__':
    main()
#Всего лишь "немного" списано у больших умов =)