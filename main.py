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
