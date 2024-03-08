"""
stringf is a Python modules that has some functions related to lists and mainly strings
Functions-
list_to_str(word):Convert a list into a string e.g. ['p','y','t','h','o','n']-'python'

join(word,word2):joins two words e.g. 'pyt','hon'-'python'

add(word,pos,word2):Like the join() functions but can join word after the letter at the specified position
e.g. add("bore",1,"ef")-'before'

reverse(word):Reverses a string 
e.g. reverse("python")-"nohtyp"

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
