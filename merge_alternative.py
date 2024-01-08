def mergelternate(word1,word2):
    string = ""
    count = 0
    while count < min(len(word1),len(word2)):
        string += word1[count]
        string += word2[count]
        count += 1
    return string + word1[count:] + word2[count:]

x = "ab"
y = "pqrs"

print(f'mergelternate---{mergelternate(x,y)}')
