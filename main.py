from database import chapters, creatures, names, objects, places, plants, spells
def answer(lst):
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
    the_dict={'sp':spells,'char':names,'cr':creatures,'ob':objects,'pl':plants,'chap':chapters,'place':places}
    while True:
        choice=input("What do you want to find: ")
        if choice=="done":
            break
        else:
            answer(the_dict[choice])

main()