"""
Dictionary created in the lab:
top_books={}
fp=open('top-books.txt')
for line in fp:
    line=line.replace("\n","")
    book_record=line.split(',')
    book_dict={}
    book_dict["author"]=book_record[1]
    book_dict["language"]=book_record[2]
    book_dict["type"]=book_record[3]
    book_dict["sold"]=book_record[4]
    top_books[line[0]]=book_dict
"""
fp=open('top-books.txt')
top_books=dict()
line=fp.readline()
while line:
    words=line.split(',')
    words[4]=words[4].rstrip('\n')
    top_books[words[0]]={'Author':words[1],'language':words[2],'type':words[3],'count':int(words[4])}
    line=fp.readline()
fp.close()
types={}
for val in top_books.values():
    if val['type'] in types:
        types[val['type']]+=val['count']
    else:
        types[val['type']]=val['count']
print(types)
#Program menu
print("1- How many different languages are there?")
print("2- What language has the most books?")
print("3- Display all books in a given language.")
print("4- What are the different types of books? Which type has sold most copies?")
print("5- List all authors who have more than 1 book on the list.")
print("6- For a given author, what is the total number of books sold?")
print("7- List all books of a given type.")
print("8- What are the top 8 types of books?")
print("9- Display a plot to show the distribution of books among the top 8 types of books.")
print("10- Exit.")
choice=int(input("Select an option by entering its number or 10 to exit:"))
while choice != 10:
    if choice == 1:
        language=[]
        for i in top_books.values():
            if i['language'] not in language:
                language.append(i['language'])
        print("There are", len(language), "languages.", "The language list is:", language)
    elif choice == 2:
        lan=dict()
        for key, val in top_books.items():
            for k,v in val.items():
                if k == 'language':
                    lan[v]=lan.get(v,0)+1
        maxi=0
        for k,v in lan.items():
            if v>maxi:
                maxi=v
        for k,v in lan.items():
            if v==maxi:
                print("The", k, "language has the most books.")
    elif choice == 3:
        q=0
        langu=input("Enter the language:")
        print("The books with", langu, "as language are:")
        for key, val in top_books.items():
            q=0
            for k,v in val.items():
                if k == 'language':
                    if v == langu:
                        q=1
            if q==1:
                print("Book Title:",key)
                for k,v in val.items():
                    if k != 'language':
                        print(k,":",v)
    elif choice == 4:
        w=dict()
        for key,val in top_books.items():
            for k,v in val.items():
                if k == 'type':
                    w[v]=w.get(v,0)+1
        print("The different types of books are:")
        for key,val in w.items():
            print(key)
        mmm=0
        for k,v in w.items():
            if v>mmm:
                mmm=v
        for k,v in w.items():
            if v==mmm:
                print("The", k, "type book has sold most copies.")
    elif choice == 5:
        auth=dict()
        for key,val in top_books.items():
            for k,v in val.items():
                if k == 'Author':
                    auth[v]=auth.get(v,0)+1
        print("The authors have multiple books:")
        for k,v in auth.items():
            if v>1:
                print(k,':',v)
    elif choice == 6:
        sold=0
        name=input("Enter the author name:")
        for key,val in top_books.items():
            o=0
            for k,v in val.items():
                if v==name:
                    o=1
            if o==1:
                for k,v in val.items():
                    if k=='count':
                        sold=sold+int(v)
        print("The total copies of books sold by author", name, "is", sold)
    elif choice == 7:
        w=dict()
        for key,val in top_books.items():
            for k,v in val.items():
                if k == 'type':
                    w[v]=w.get(v,0)+1
        print("The different types of books are:")
        for key,val in w.items():
            print(key)
        h=str(input("The type is:"))
        for book in top_books:
            if top_books[book]['type']==h:
                print(book)
    elif choice == 8:
        list_keys=list(types.keys())
        list_values=list(types.values())
        types_inverse=dict(zip(list_values, list_keys))
        dictionary_items=types_inverse.items()
        sorted_items=sorted(dictionary_items)
        print(sorted_items)
        top8types=[]
        top8sold=[]
        count=0
        for k in sorted(sorted_items,reverse=True):
            top8sold.append(k)
            top8types.append(sorted_items[k])
            count+=1
            if count==8:
                break
        print("The top 8 types are:", top8types, "They sold", top8sold)
    elif choice == 9:
        import numpy as np
        import matplotlib.pyplot as plt

        x = ("Fantasy","Satire","Mystery","Historical Fiction","Family Saga","Adventure","Romance","Children's Fiction") #type of book
        markings = np.arange(len(x))
        y = [1357000000,600000000,290000000,256500000,133000000,117094805,115000000,100000000] #number of copies of this type book sold
        plt.bar(markings,y, align='center',alpha=0.5) #barchart
        plt.xticks(markings,x) #draw x-axis markings
        plt.title("Distribution of books among the top 8 types of books")
        plt.xlabel("Type of book")
        plt.ylabel("Number of copies of this type of books sold")
        plt.show()
    else: #option 10
        print("You exit the program.")
        exit
    #Program menu
    print("1- How many different languages are there?")
    print("2- What language has the most books?")
    print("3- Display all books in a given language.")
    print("4- What are the different types of books? Which type has sold most copies?")
    print("5- List all authors who have more than 1 book on the list.")
    print("6- For a given author, what is the total number of books sold?")
    print("7- List all books of a given type.")
    print("8- What are the top 8 types of books?")
    print("9- Display a plot to show the distribution of books among the top 8 types of books.")
    print("10- Exit.")
    choice=int(input("Select an option by entering its number or 10 to exit:"))
