#/bin/bash
# -*- coding: UTF-8 -*-

# 对生成的词典文件进行后处理

def main():
    with open("words.txt") as fi, open("final.txt", "w") as fo:
        words = set([])
        for line in fi:
            line = line.strip()
            cols = line.split("\t")
            words.add(cols[0])
        words_list = list(words)
        words_list = sorted(words_list)
        for w in words_list:
            fo.write(w + "\n")

if __name__ == '__main__':
    main()