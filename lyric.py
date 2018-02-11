#!/usr/bin/python
# coding: UTF-8

html = '''Content-Type: text/html

<html>
<head>
    <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>「松本隆」歌詞自動生成サイト</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<h1>「松本隆」歌詞自動生成</h1>
<h2>松本隆がこれまで書いた詞より自動で生成されています。</h2>
<p>%s</p>
<p><a href="http://soda-lab.com/sam/day30/kashi2.py">再生成</a></p>
<p class="copy"><small> &#169; <a target="_blank" href="https://twitter.com/sam__1210">Fumiya Fukumoto</a> @<a target="_blank" href="http://sodatower.com/">SODA TOWER</a></small></p>
</body>
</html>
'''
content=''

import MeCab
import cgi
import cgitb
import random
cgitb.enable()


def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result

if __name__ == "__main__":
    filename = "lryric.txt"
    src = open(filename, "r").read()
    wordlist = wakati(src)
    markov = {}
    w1 = ""
    w2 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word
    count = 0
    sentence = ""
    w1, w2  = random.choice(markov.keys())
    while count < 200:
        tmp = random.choice(markov[(w1, w2)])
        sentence += tmp
        sentence += " "
        w1, w2 = w2, tmp
        count += 1

content += "%s " % sentence
print html % (content)
