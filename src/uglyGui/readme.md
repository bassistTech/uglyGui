# PDF_Chunker_Upper

Francis Deck, 3-4-2025

PDF_Chunker_Upper is a utility to break up a large PDF file into a bunch of smaller ones. My main use is PDF copies of sheet music books. For instance a book might contain a whole bunch of etudes or songs. Breaking it up into files named after the songs allows me to use the regular file manager of the OS platform to find and organize material. Files from multiple books can be combined, and the file manager will keep them in alphabetical order, or allow for searching.

**It's a Python program** and is shared as source code. This means it's likely to be difficult for beginners to install, but I hope to provide some instructions. For now, if you know someone who's into Python programming, ask them to help you. Python is the #1 most popular programming language, and *it's not all that hard*, but could be forbidding for a non-techie.

## How it works
To chunk up a PDF, you need an index, so the program knows which pages go where. The main function of the program is a GUI that helps you build that index. The index is kept as a separate file.

Once you're satisfied that the index is accurate, you tell it to break up the PDF, and it takes a while. I've been careful to make sure that my program never modifies or damages your original PDF file.