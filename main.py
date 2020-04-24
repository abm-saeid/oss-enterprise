__author__="Rafeed M. Bhuyian"
__version__='0.1Alpha'
""" How to use:
    Suppose you need to find a spell for crossword,
    imput 'sp',
    if the word is 3 letters and the 3rd letter is 'x',
    then imput '3 3 x'
    Output ['nox'] is your answer.
    Warning!
    There is a 80% possibility of multiple results."""
from database import chapters, creatures, names, objects, places, plants, spells #imports

def answer(lst):
    """The real function"""
    while True:
        blank_lst=[]
        a,b,c=map(str,input().split())
        a=int(a)
        b=int(b)
        for i in lst:
            if len(i)==a and i[b-1]==c:
                blank_lst.extend([i])
        lst=blank_lst.copy()
        print(lst)
        if len(lst)==1:
            break
    return lst[0]

def main():
    """ The other func"""
    the_dict={'sp':spells,'char':names,'cr':creatures,'ob':objects,'pl':plants,'chap':chapters,'place':places}
    while True:
        choice=input("What do you want to find: ")
        if choice=="done":
            break
        else:
            answer(the_dict[choice])

main()