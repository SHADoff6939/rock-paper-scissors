def menu():
    menu_op = ['1. start game', '2.exit']
    for i in menu_op:
        print(i)
    menu_ch = ''
    while menu_ch not in range(1, len(menu_op)):
        try:
            menu_ch = int(input())
        except ValueError:
            print('please type a numbeof the choice')
    return 0

if __name__ == '__main__':
    menu()
