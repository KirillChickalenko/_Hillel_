from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, author_or_director, year):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"


class Book(LibraryItem):
    def __init__(self, title, author, year, number_of_pages):
        super().__init__(title, author, year)
        self.number_of_pages = number_of_pages

    def description(self):
        return super().description() + f", Number of pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def description(self):
        return super().description() + f", Issue number: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)
        self.duration = duration

    def description(self):
        return super().description() + f", Duration: {self.duration} minutes"


book = Book("Вій", "Микола Гоголь", 1835, 320)
magazine = Magazine("Forbes", "Randall Lane", 2024, 5)
dvd = DVD("Interstellar", "Christopher Nolan", 2014, 169)

print(book.description())
print(magazine.description())
print(dvd.description())
