#!/usr/bin/env python3

from book import Book

import io
import sys

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_page_count(self):
        print("Retrieving page count.")
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == int:
            print(f"Setting page count to {page_count}")
            self._page_count = page_count

        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)


    def get_title(self):
        print("Retrieving title.")
        return self._title
    
    def set_title(self, title):
        if type(title) == str and ( 1<= len(title) <= 45):
            print(f"Setting title to {title}")
            self._title = title = title

        else:
            print("title must be a string")

    title = property(get_title, set_title)




    
        