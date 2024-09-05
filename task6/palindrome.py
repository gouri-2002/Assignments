

words=["madam","aba","bcb","hello","pythom"]

#print palindromic string from the above words

for i in range(0,len(words)):

    reverse=words[i][::-1]

    if words[i]==reverse:

        print(words[i])