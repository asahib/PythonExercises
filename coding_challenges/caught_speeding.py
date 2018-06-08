def caught_speeding(speed, is_birthday):
    return (0 if speed < 66 else 1 if speed < 86 else 2) if is_birthday else (0 if speed < 61 else 1 if speed < 81 else 2)

    
print(caught_speeding(0, False))
print(caught_speeding(80, False))
print(caught_speeding(0, True))