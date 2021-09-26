
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

open_file = open('list.csv')
raw_data = open_file.read()
open_file.close()

def search():
    word = input("鬼滅の登場人物の名前を入力してください >>>")
    if word in raw_data:
        print("{}が見つかりました".format(word))
    if word not in raw_data:
        print("{}が見つかりませんでした".format(word))
        append_file = open("list.csv","a")
        append_file.write(word)
        append_file.close()

search()

open_file = open('list.csv')
raw_data = open_file.read()
open_file.close()

print(raw_data)


