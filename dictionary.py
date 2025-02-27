books = [{
'title': "Phantasma",
'genre': "Fantasy Romance",
'author': "Kaylie Smith"
},  {
'title': "Reckless",
'genre': "Fantasy Fiction",
'author': "Lauren Roberts"
}, {
'title': "A Liars Twisted Tongue",
'genre': "Fantasy Fiction",
'author': " Caroline Cusanelli"
}]

songs = [{
'title': "Cry For Me",
'genre': "R&B/Soul",
'author': "The Weeknd"
},  {
'title': "Are You Even Real",
'genre': "Pop",
'author': "Giveon and Teddy Swims"
}, {
'title': "Timeless",
'genre': "R&B/Soul",
'author': "The Weeknd"
}]

x = input("which dictionary do you want to see? books or songs?")
if x == "books":
    print("Titles from books:")
    for book in books:
        print(book['title'])

    print("\nGenres from books:")
    for book in books:
        print(book['genre'])

    print("\nAuthors from books:")
    for book in books:
        print(book['author'])

elif x == "songs":
    print("Titles from songs:")
    for song in songs:
        print(song['title'])

    print("\nGenres from songs:")
    for song in songs:
        print(song['genre'])

    print("\nAuthors from songs:")
    for song in songs:
        print(song['author'])