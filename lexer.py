class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0

    def tokenize(self):
        while self.position < len(self.source):
            current = self.source[self.position]

            if current.isalpha():
                word = []

                while self.position < len(self.source) and self.source[self.position].isalpha():
                    word.append(self.source[self.position])
                    self.position += 1

                word_str = "".join(word)
                print("見つけた単語:", word_str)
                if word_str == "print":
                    print("PRINT TOKEN")
                else:
                    print("IDENTIFIER TOKEN")

            else:
                self.position += 1

        return []