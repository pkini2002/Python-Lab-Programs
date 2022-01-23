#Simple to do list generation app built using python
user_input = 'random'
data= []

def show_menu():
    print('Menu')
    print('1.Add an item')
    print('2.Mark as done')
    print('3.View items')
    print('4.Exit')

while user_input != '4':
    show_menu()
    user_input=input('>>>')
    
    if user_input == '1':
        item = input('What is to be done?')
        data.append(item)
        print('Added item',item)

    elif user_input == '2':
        item = input('What is to be marked as done?')
        data.remove(item)
        print('Removed item:',item)

    elif user_input == '3':
        print('List of to do items')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Good bye')
    else:
        print('Please enter one of 1,2,3 or 4')
   