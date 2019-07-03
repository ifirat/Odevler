
for b in range(1,100):
    if b%3==0 and b%5==0:
        print("FIZZBUZZ")
    elif b%3==0:
        print("FIZZ")
    elif b%5==0:
        print("BUZZ")
    else:
        print(b)
