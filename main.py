from lexer import Lexer

def main():
    with open("examples/hello.mxr", encoding="utf-8") as f:
        source = f.read()

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()