#Stores people's birthdays

birthdays = {'Juana':'Oct 2','Mikee':'March 30', 'Mike':'March 27',\
             'Jeiel':'March 28','Fritz':'May 1','Nico':'April 25',\
             'Cai':'Nov 7','Jobii':'Sep 29','Jeff':'Sep 11',\
             'Mark':'Sep 7','Josh':'June 2'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == "":
        break


    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have the birthday information for ' + name)
        print('When is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated')

        
