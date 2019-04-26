import random
def main():
    try:
        number_file = open('random', 'w')

        random_amount = int(input('Please enter how many random numbers the file will hold: '))

        for x in range(random_amount):
            number = random.randint(1,500)
            number_file.write(str(number) + '\n')
        number_file.close()
    except ValueError:
        print('Error: you must enter a number')

main()
