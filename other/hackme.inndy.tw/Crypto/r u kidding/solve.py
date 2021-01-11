message = "EKZF{Hs'r snnn dzrx, itrs bzdrzq bhogdq}"
LETTERS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

# 跑 52 次
for key in range(len(LETTERS)):
    output = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key
            if num < 0:
                num += len(LETTERS)
            output += LETTERS[num]
        else:
            output += symbol
    print('%s. %s' % (key, output))

