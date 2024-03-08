"""
stringf is a Python modules that has some functions related to lists and mainly strings
Functions-
list_to_str(word):Convert a list into a string e.g. ['p','y','t','h','o','n']-'python'

join(word,word2):joins two words e.g. 'pyt','hon'-'python'

add(word,pos,word2):Like the join() functions but can join word after the letter at the specified position
e.g. add("bore",1,"ef")-'before'

reverse(word):Reverses a string 
e.g. reverse("python")-"nohtyp"
-NEW-
plural(word):Converts most words into plural form!
e.g. plural("python")-"pythons"
More functions coming soon!
"""

class string:
    
    def list_to_str(list):
        strl=""
        for e in list:
            strl+= e
        return strl
    def join(word,word2):
        return str(word)+str(word2)
    def add(word,pos,word2):
        word=list(word)
        word.insert(pos,word2)
        strl=""
        for e in word:
            strl+= e
        return strl
    def reverse(word):
        word=list(word)
        nword=word[::-1]
        strl=""
        for e in nword:
            strl+= e
        return strl
    def plural(word):
        vowel=list("aeiou")
        consonant=list("bcdfghjklmnpqrstvwxyz")
        word=list(word)
        if word[-1]=="f" or word[-1]=="ef":
            word.append("s")
        elif word[-1]=="s" or word[-1] == "x" or word[-1] == "z":
            word.append("es")
        elif (word[-1]=="s" and word[-2]=="s") or (word[-1]=="s" and word[-2]=="h") or (word[-1]=="c" and word[-2]=="h"):
            word.append("es")
        elif word[-1]=="s":
            word.append("ses")
        elif word[-1]=="z":
            word.append("zes")
        elif word[-1]=="y"and word[-2] in vowel:
            word.append("s")
        elif word[-1]=="y" and word[-2] in consonant:
            word[-1]="ies"
        elif word[-1]=="o":
            word.append("es")
        elif word[-2]=="u"and word[-1]=="s":
            word.pop(-1)
            word[-2]="i"
        elif word[-2]=="i"and word[-1]=="s":
            word[-2]="e"
        elif word[-2]=="o"and word[-1]=="n":
            word.pop(-1)
            word[-2]="a"
        else:
            word.append("s")
        strl=""
        for e in word:
            strl+= e
        return strl