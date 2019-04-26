import random
def main():
    number_file = open('random', 'w')

    random_amount = int(input('Please enter how many random numbers the file will hold: '))

    for x in range(random_amount):
        number = random.randint(1,500)
        print(number)
        number_file.write(str(number) + '\n')
    number_file.close()


main()