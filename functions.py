from random import randint


def funcTest():
    return "facciamo un test con numero random: " + str(randint(1, 100))
    

if __name__ == '__main__':
    print(funcTest())
