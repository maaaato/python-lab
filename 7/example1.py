import b64
import sys

print(dir(b64))


def main():
    target = sys.argv[1]
    print(type(b64))
    print(dir(b64))
    print(b64.str_to_base64(target))  # 頭のbはbytes型を意味する


if __name__ == "__main__":
    main()
