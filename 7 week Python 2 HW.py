
import urllib.request
url = "https://www.py4e.com/code3/romeo.txt"


urllib.request.urlretrieve(url, "romeo.txt")


Special_word = []


with open("romeo.txt", "r") as file:

    for line in file:

        words = line.split()

        for word in words:
            if word not in Special_word:
                Special_word.append(word)

Special_word.sort()

for word in Special_word:
    print(word)
