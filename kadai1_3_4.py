
#課題1-3 --------------------------------------------

# open_file = open('list.csv')
# raw_data = open_file.read()
# open_file.close()

# def search():
#     word = input("鬼滅の登場人物の名前を入力してください >>>")
#     if word in raw_data:
#         print("{}が見つかりました".format(word))
#     if word not in raw_data:
#         print("{}が見つかりませんでした".format(word))
#         raw_data.append(word)

# search()

# print(raw_data)

#課題1-4 --------------------------------------------

# def search():
#     word = input("鬼滅の登場人物の名前を入力してください >>>")
#     open_file = open('list.csv')
#     raw_data = open_file.read()
#     open_file.close()
#     if word in raw_data:
#         print("{}が見つかりました".format(word))
#     if word not in raw_data:
#         print("{}が見つかりませんでした".format(word))
#         append_file = open("list.csv","a")
#         append_file.write(word)
#         append_file.close()
#         open_file = open('list.csv')
#         raw_data = open_file.read()
#         open_file.close()
#         print(raw_data)

# search()


def search():
    word = input("鬼滅の登場人物の名前を入力してください >>>")
    with open("list.csv", mode="r") as f:
        source = f.read()
    if word in source:
        print("{}が見つかりました".format(word))
    if word not in source:
        print("{}が見つかりませんでした".format(word))
        with open("list.csv", mode="a") as f:
            f.write(word)
        with open("list.csv", mode="r") as f:
            source = f.read()
            print(source)

search()


