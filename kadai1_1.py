# 課題1-1 --------------------------------------------


def search():
    source = ["ねずこ","たんじろう","きゅうじろう","ぎゆう","げんや","かなお","せんいつ"]
    word = input("鬼滅の登場人物の名前を入力してください >>>")
    if word in source:
        print("{}が見つかりました".format(word))
    if word not in source:
        print("{}が見つかりませんでした".format(word))

search()