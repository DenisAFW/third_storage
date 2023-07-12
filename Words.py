# В большой текстовой строке подсчитать количество встречаемых слов
# и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = "Let's imagine ...You're watching TV. It's a hot evening: You feel thirsty.\
 You see an advert for a refreshing drink. You see people looking cool and relaxed.\
  You notice the name of the refreshing drink because you think it could be useful\
   for you to satisfy your thirst."

text_list = text.lower().split()
text_dict = {}

for i in text_list:
    clear = i.strip(".,!;:")
    if clear not in text_dict:
        text_dict[clear] = 1
    else:
        text_dict[clear] += 1

print(text_dict)

result = dict(sorted(text_dict.items(), key=lambda x: x[1], reverse=True))
print(result)
