import datetime
import sys
from collections import OrderedDict
import os

from peewee import *

db = SqliteDatabase("diary.db")


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the datebase and the table if they do not exist"""
    db.connect()
    db.create_tables([Entry], safe=True)

def clear():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """Show the menu."""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))

        choice = input("Action: ").lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    """Add and entry."""
    print("Enter your entry. Press enter when finished.")
    data = sys.stdin.readline().strip()

    if data:
        if input("Save entry? [Y/N]\n").lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")

def view_entries(search_query=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d %Y %I:%M%p')
        clear()
        line = len(timestamp)
        print('='* line)
        print(timestamp)
        print('='* line)
        print(entry.content)
        print("\n\n")
        print('_ ' * line)
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')

        next_action = input("Action: [Ndq] ").lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

def search_entries():
    """Search entries for a word"""
    view_entries(input("Search: "))

def delete_entry(entry):
    """Delete an entry."""
    if input("Are you sure? [yN]").lower().strip() == 'y':
        entry.delete_instance()
        print("Entry was successfully deleted!")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == "__main__":
    initialize()
    menu_loop()