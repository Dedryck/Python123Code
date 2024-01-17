import string

def caesar_cipher(text):
    #在下面函数填充代码
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    table = ''.maketrans(lowers + uppers + digits,"defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC3456789012")
    str = text.translate(table)###
    return str###

if __name__ == '__main__':
    plaintext = input()
    print(caesar_cipher(plaintext))