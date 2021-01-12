


mySentence = 'loves the color'

color_list = ['red','blue','black','pink','yellow','brown']


def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        lst.append(msg)
    return lst


def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("you need to provide your name!")
        elif name == 'Chris':
            print("Chris, you may not use this software.")
            
        else:
            go = False
    let = color_function(name)
    for i in let:
        print(i)


get_name()
