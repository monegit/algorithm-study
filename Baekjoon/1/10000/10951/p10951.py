while True:
    try:
        _input = input()
        a,b=map(int, _input.split())
        print(a+b)
    except:
        break