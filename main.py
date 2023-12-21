"""
This program keeps track of all of our books
version : 1.0.0
Date : 21/12/2023
"""




def main():
    print("welcom sir in our program")
    
    
    try:
        #initialise book list and logic :
        bookList= []
        infile= open("TheBookStore.txt","r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("the <TheBookStore.txt> file is not found")
        print("restarting a new books list")
        bookList=[]

    choice = 0
    while choice != 4:   
        print("*** Book director ***")
        print("1) Add a Book ")
        print("2) Lookup for a Book ")
        print("3) Display Books ")
        print("4) Quit ")

        choice = int(input())
        if choice == 1:
            print("Adding a book...")
            nBook = input("enter the name of the book :")
            nPage= input ("enter the number of the pages :")
            nAuthor= input("enter the name of the author:")
            dPublishing =  input ("enter the year of publishing this book")
            bookList.append([nBook,nAuthor,nPage,dPublishing])
        elif choice == 2: 
            print("loking up for a book **")
            keyword = input ("Entre searsh Term :")
            for book in bookList:
                if keyword in book:
                    print(book)
        elif choice == 3:
            print("displaying all books... ")
            for i in range (len(bookList)):
                print(bookList[i])
        elif choice ==4:
            print("Quiting the programme")
    print("Programme terminated")

# saving to external TXT file
    outfile = open("TheBookStore.txt","w")

    for book in bookList:
        outfile.write(",".join(book) + "\n")
    outfile.close()





if __name__ == "__main__":
    main()

