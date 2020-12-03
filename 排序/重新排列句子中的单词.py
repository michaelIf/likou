# 使用sorted
def arrangeWords(text):
    text_li = text.split()
    tmp_dict = {}
    for i, j in enumerate(text_li):
        tmp_dict[str(i) + '-' + text_li[i]] = len(j)
    res_dict = sorted(tmp_dict.items(), key=lambda x: (x[1]))
    res = ''
    for k, y in res_dict:
        res = res + k.split('-')[1] + ' '
    return res.capitalize().strip()

# text = "Keep calm and code on"
text = "Jtik hrzrvhbmk gbo cfhmiqwonj ojkew ufvledv bomoeqt ops jgi zdhvbpbb zczmepdfpm jry rjazc titttcu"
print(arrangeWords(text))


# 直接使用lambda
def way2(text):
    text_li = text.split(' ')
    text_li.sort(key=lambda x:len(x))
    return ' '.join(text_li).capitalize()
text = "Keep calm and code on"
print(way2(text))

# 一行代码
def way3(text):
    return ' '.join([x[2] for x in sorted([(len(x), i, x.lower()) for i, x in enumerate(text.split(' '))])]).capitalize()

text = "Keep calm and code on"
print(way3(text))