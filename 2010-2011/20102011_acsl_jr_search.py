import re


def main():
    words = input().split(", ")
    output = ""
    for i in range(5):
        search = input()
        search = search.replace("?", ".")
        search = search.replace("*", ".+")
        matching = []
        for word in words:
            if re.search(search, word):
                matching.append(word)
        output += (str(i+1)+". ")
        if len(matching) == 0:
            output += "No Match\n"
        else:
            for j in range(len(matching)):
                if j == len(matching)-1:
                    output += (matching[j]+"\n")
                else:
                    output += (matching[j]+", ")
    print(output)


if __name__ == "__main__":
    main()
