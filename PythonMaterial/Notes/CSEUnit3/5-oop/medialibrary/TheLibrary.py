#imports
from Song import Song

#global variables

#create a Song
#myfav = Song("Wheels on the Bus - Wild n Out")

#print(myfav)
#print(myfav.title)
menu = '''

A to Add
E to Edit
D to Delete
V for View
Q for Quit

'''

library = []
ui = input(menu)
while(ui!="q"):
    if ui=="a":
        name = input("Name of your song")
        artist = input("Name of your artist")
        library.append(song(name))
    elif ui=="e":
        print("e")
    elif ui=="d":
        print("d")
    elif ui=="v":
        print(library)
        for eachItem in library:
            print(eachItem)#.title + " " + eachItem.artist)
    ui = input(menu)
print("Program Shut Down")