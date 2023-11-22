library_books = [
    {"title": "Python crash course", "author": "Eric Matthes", "genre": "programming"},
    {"title": "To kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
 ] #Liste de livres disponibles dans la bibliothèque

checked_out_books = set() #Ensemble de livres vérifiés

library_branches = ("Main Branch", "Downtown Branch", "East Branch") #Branches de la bibliothèque

library_hours = {
    "Main Branch": "9:00 AM - 6:00 PM",
    "Downtown Branch": "10:00 AM - 7:00 PM",
    "East Branch": "8:30 AM - 5:30 PM",
} #Heures d'ouverture de la bibliothèque

while True:
    print("\n Welcome to our library")
    print("Options: ")
    print("1. View Books in the Library")
    print("2. Check out a Book")
    print("3. View checked Out Books")
    print("4. View Library Branchs")
    print("5. View Labrary hours")
    print("6. Exit")
    choice = input("\nEnter your choice (1-6):")   #Boucle principale du programme

    if choice == "1": 
      print("\nBooks in the Library:")  #Afficher la liste des livres dans la bibliothèque
      for book in library_books:
        print("{book['title']) by {book['author']} ({book[ 'genre']})")

    elif choice == "2":

      book_to_checkout = input("\nEnter the title of the book you want to check out: ") #Emprunter un livre

      if book_to_checkout.lower() in [book.lower() for book in checked_out_books]:
          print("\nSorry, this book has already been checked out. Please choose another book.") 
      else:
        for book in library_books:
          if book["title"].lower() == book_to_checkout.lower():   
                 checked_out_books.add(book["title"])
                 print (f"\nYou have checked out '{book['title']}'. Enjoy your reading!")

    elif choice == "3":
        print("\nChecked Out Books: ") #Afficher les livres empruntés

        for book in checked_out_books:
             print (book)

    elif choice == "4":

        print("\nLibrary Branches: ")  #Afficher les branches de la bibliothèque
        for branch in library_branches:

           print(branch)

           for branch in library_branches: 
              print(branch)

    elif choice == "5":

        print("\nLibrary Hours:")  #Afficher les heures d'ouverture de la bibliothèque

        for branch, hours in library_hours.items():

          print("{branch): (hours)")

    elif choice == "6":

       print("\nExiting the Library Program. Goodbye!") #Quitter le programme

       break

    else:

        print("\nInvalid choice. Please enter a number between 1 and 6.") #Message d'erreur pour une option invalide