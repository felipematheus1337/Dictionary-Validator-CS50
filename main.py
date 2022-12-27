from fileinput import close


def main(filename):
    words = set()

    def check(word):
        if word.lower() in words or word.upper():
            return True
        else:
            return False

    def load(dictionary):
        file = open(dictionary, "r")
        for line in file:
            word = line.rstrip()
            words.add(word)
        close()
        return True

    def size():
        return len(words)

    def unload():
        return True

    isTrue = load(filename)

    if isTrue:
        print(check('f'))
        print(size())
        print(unload())


if __name__ == '__main__':
    main("names")
