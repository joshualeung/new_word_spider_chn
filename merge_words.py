#/bin/bash
# -*- coding: UTF-8 -*-
import os
# 对生成的词典文件进行后处理

def main():
    base_dir = "download/"
    target_file = "data/words.dic"
    files = [
        "baidu.txt", "baidu-hotword.txt", "star.txt"
    ]
    words = set([])
    with open(target_file) as fi:
        for line in fi:
            words.add(line.strip())
        fi.close()
    for f in files:
        f = base_dir + f
        with open(f) as fi:
            for line in fi:
                line = line.strip().lower()
                cols = line.split("\t")
                words.add(cols[0])
            fi.close()
    with open(target_file, "w") as fo:
        words_list = list(words)
        words_list = sorted(words_list)
        for word in words_list:
            fo.write(word + "\n")
        fo.close()

if __name__ == '__main__':
    main()