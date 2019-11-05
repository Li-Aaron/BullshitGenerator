#!/usr/bin/python

import os, re, sys
import random

def ReadJsonFile(fileName=""):
    import json
    if fileName!='':
        strList = fileName.split(".")
        if strList[len(strList)-1].lower() == "json":
            with open(fileName, mode='r', encoding = 'utf-8') as file:
                return json.loads(file.read())


data = ReadJsonFile("data.json")
FamousPeople = data["famous"] # a代表前面垫话，b代表后面垫话
FormerTrash  = data["before"] # 前面垫话 在名人名言前面弄点废话
AfterTrash   = data["after"]  # 后面垫话 在名人名言后面弄点废话
MainTrash    = data["bosh"]   # 代表文章主要废话来源

Repeats = 2

def Traverse(Array):
    global Repeats
    Pool = list(Array) * Repeats
    while True:
        random.shuffle(Pool)
        for element in Pool:
            yield element

NextTrash = Traverse(MainTrash)
NextFamous = Traverse(FamousPeople)

def GenerateFamous():
    global NextFamous
    xx = next(NextFamous)
    xx = xx.replace( "a",random.choice(FormerTrash) )
    xx = xx.replace( "b",random.choice(AfterTrash) )
    return xx

def NextParagraph():
    xx = ""
    xx += "\r\n"
    xx += "　　"
    return xx

if __name__ == "__main__":
    if len(sys.argv) > 1:
        topic = str(sys.argv[1])
    else:
        topic = "人的一生究竟有多少苦痛"

    tmp = "　　"
    while ( len(tmp) < 6000 ) :
        rand = random.randint(0,100)
        if rand < 5 and tmp[-1] == "。":
            tmp += NextParagraph()
        elif rand < 20 :
            tmp += GenerateFamous()
        else:
            tmp += next(NextTrash)
    tmp = tmp.replace("x", topic)

    print(topic)
    print(tmp)
    with open("{topic}.txt".format(topic = topic), 'w', encoding = "utf-8") as File:
        File.write(tmp)