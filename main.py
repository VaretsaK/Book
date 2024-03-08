class Book:
    """
        A Book class that stores information about a book and provides comparison methods.

        Attributes:
            title (str): The title of the book.
            author (str): The author of the book.

        Methods:
            __init__: Constructs a Book instance with a title and an author.
            __eq__: Compares this Book instance with another for equality based on title and author.
            __ne__: Compares this Book instance with another for inequality based on title and author.
            __repr__: Returns a string representation of the book.
        """
    def __init__(self, title: str, author: str) -> None:
        """
        Initialize a Book instance with the given title and author.
        """
        self.title = title
        self.author = author

    def __eq__(self, other: object) -> bool:
        """
        Check the equality of this Book instance with another Book instance.
        """
        if isinstance(other, Book):
            return self.author == other.author and self.title == other.title
        raise TypeError("Unsupported operand type for ==")

    def __ne__(self, other: object) -> bool:
        """
        Check the inequality of this Book instance with another Book instance.
        """
        if isinstance(other, Book):
            return self.author != other.author and self.title != other.title
        raise TypeError("Unsupported operand type for !=")

    def __repr__(self):
        """
        Returns a string representation of the Book instance.
        :return:
        """
        return f"Book('{self.title}';'{self.author}')"


class Library:
    """
    A Library class to manage a collection of books.

    Attributes:
        list_of_books (list[Book]): A list of Book instances.

    Methods:
        __init__: Initializes a new Library instance with a list of books.
        __len__: Returns the number of books in the library.
        __repr__: Returns a string representation of the library.
        __getitem__: Allows indexed access to the library's books.
    """
    def __init__(self, list_of_books: list['Book']) -> None:
        """
        Initializes a new Library instance.
        :param list_of_books:
        """
        self.list_of_books = list_of_books

    def __len__(self) -> int:
        """
        Returns the number of books in the library.
        :return:
        """
        return len(self.list_of_books)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Library instance.
        :return:
        """
        return f"Library('{self.list_of_books}')"

    def __getitem__(self, item) -> object:
        """
        Allows indexed access to the books in the library.
        :param item:
        :return:
        """
        return self.list_of_books[item]
