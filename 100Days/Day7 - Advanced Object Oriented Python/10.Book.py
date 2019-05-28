class Book():

    def __init__(self,name,copies):
        self._name = name
        self._copies = copies
    
    """
        toString equivalent of java
    """
    def __repr__(self):
        return repr((self._name,self.copies))

    """
        getter equivalent - 
        book.copies 
    """
    @property
    def copies(self):
        return self._copies

    """
        setter
        -use the @property to define setter
    """
    @copies.setter
    def copies(self,copies):
        self._copies = copies

if __name__ == "__main__":
    book = Book('microservice',1)
    print(book)
    print(book.copies)
    book.copies = 100
    print(book)