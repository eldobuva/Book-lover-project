# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:44:18 2020

@author: Administrator
"""

class BookLover:
    def __init__(self, name, email, favGenre, numBooks = 0, bookLst = []):
        self.name = name
        self.email = email
        self.favGenre = favGenre
        self.numBooks = numBooks
        self.bookLst = bookLst
        
    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Email: ' + self.email + '\n' + 'Books read: ' + str(self.bookLst)
        
    def addBook(self, bookName='x', rating=0):
        self.bookName=input('Input the book name: ')
        z=0
        while z==0:
            k=0
            for book in self.booBkLst:
                if book[0]==self.bookName:
                    k=1    
            if k==1:
                self.bookName=input('This book already exists in the list! Input another book name: ')
            else:
                z=1
        self.rating = int(input('Rate this book (0:"Did not like the book" to 5:"Loved the book"): '))    
        while self.rating<0 or self.rating>5:
            self.rating= int(input('Rate is not valid! (0:"Did not like the book" to 5:"Loved the book"). Rate again: ')) 
                 
        record = (self.bookName, self.rating)
        self.bookLst.append(record)
        self.numBooks += 1    

#   def addBook(self, bookName, rating):
#        title = bookName
#        rating = int(rating)
#        record = (bookName, rating)
#        self.bookLst.append(record)
#        self.numBooks += 1        
                
        
    def hasRead(self, bookName):
        check_list = []
        for x in self.bookLst:
            if x[0] == bookName:
                check_list.append(True)
            else:
                check_list.append(False)
        if True in check_list:
            return True
        else:
            return False
    
    def numBooksRead(self):
        return self.numBooks
    
    def favBooks(self):
        top_books = []
        for x in self.bookLst:
            if x[1] > 3:
                top_books.append(x[0])
        return top_books

P1=BookLover("Ali", 'am4hb@virginia.edu', 'Fiction')
P1.addBook()