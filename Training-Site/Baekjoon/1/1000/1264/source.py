while (True):
    _input = input().lower()

    if (_input == '#'):
        break

    a = _input.count("a")
    e = _input.count('e')
    i = _input.count('i')
    o = _input.count('o')
    u = _input.count('u')

    print(a+e+i+o+u)
