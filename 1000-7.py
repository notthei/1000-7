import time
num = 1000

def subtract_seven_sequence(start):
    num = start
    while num > 0:
        print(f"{num + 7} - 7 = {num - 7}")
        num -= 7
        time.sleep(0.3)

subtract_seven_sequence(num)
