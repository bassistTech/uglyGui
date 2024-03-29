# uglyGui

Francis Deck

Minimalist GUI library for supporting my own projects.

**Purpose**: Create ugly but readable GUI's quickly, with minimal boilerplate. All layout is automatic. Aesthetics are by default. Widgets are arranged vertically in the order that they're created. Options: None.

I'll be using it in some of the other programs that I share, so it belongs in its own repo.

**History**: In the mid 80's, I wrote a graphing program in Turbo Pascal. The program quickly ballooned into screen after screen of options, as I added stuff to meet my own needs. I quickly got sick of "hard coding" menus, so I wrote a library that generated my menus automatically, in MS-DOS text mode.

Then I forgot about it, got into HyperCard, and then Visual Basic. Being able to draw GUIs was certainly intuitive and convenient, but making nice ones becomes physically laborious, unless you automate styling and layout. But if you do that, you're getting close to automating everything.

uglyGui is the same concept as my old Pascal program, brought up to date in Python, using the **tkinter** library, plus **matplotlib** for graphing.

**How to get it**: Navigate to a convenient folder for storing this repo, and execute:

	git clone https://github.com/bassistTech/uglyGui.git
	cd uglyGui
	pip install -e .
	
Note that I chose the "editable" mode, which leaves the code in the location where you placed it, and lets you make changes. You can also install without that option, which puts it in your site-packages folder.

**Usage**

You can build a dialog in just one line of Python per widget, plus a tiny amount of boilerplate. Stuff is arranged automatically, and Tkinter uses the standard widgets of your OS platform if you don't customize them. You'll need to import the library of course:

	import uglyGui
	
You need to create at least one dialog:

	mainDialog = uglyGui.MainDialog('My first dialog')
	
You can add some widgets:

	button1 = uglyGui.Button(mainDialog, 'Press me',
		action = lambda: print('You pressed me'))
		
	intEntry1 = uglyGui.IntEntry('Number of things', 20)
	
Finally you can show the dialog

	mainDialog.show()
	
Invoking show() is blocking, i.e., your program won't go any further until you close the main window.

You always need a MainDialog, but can add SubDialog objects, which behave the same with one difference. Closing a SubDialog just closes it. Closing the MainDialog terminates the show() method, which is typically equivalent to your dear user quitting your program. You can have lines of code after show(), for instance to clean up open ports.

**Learning more**

For more elaborate examples, check out some of my other repo's! I'm going to be using uglyGui for some the Python programs that I write and share here.