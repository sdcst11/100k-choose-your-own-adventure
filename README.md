  # 100k-choose-your-own-adventure
##Create a choose your own adventure program

Choose your own adventure (CYAC) was a popular series of books that was published in the mid 1980's.  Instead of reading the book from cover to cover, you would read the contents of a page.  It would have a few options about what you wanted to do next in the story, and the options would direct you to an appropriate page to continue your adventure. Some options would allow you to keep going, while others could lead to death or a happy ending.  

The key to the CYAC books was that a single part of the story (1 page) was kind of a contained section.

We can create our own CYAC using multiple print statements.  First thing you want to do is flesh out your story with a web diagram.  This is best planned on paper.  The distinct pathways of your story will likely begin to branch out like a tree, with each combination of choices resulting in a different outcome at the end. To do this, you may need to make use of nested if statements. This means putting a second if-else structure inside of the first one.

![Choose your own adventure map](cyoa.png)
[Choose your own adventure map](https://rudolfkerkhoven.com/wp-content/uploads/2011/01/sturls-map.jpg)

Once you have a plan, you can start filling in contents for your pages.

### Advanced Options

We can include color in our print output!

This requires that you make use of a Python Library that is not normally included in your Python installation.  We will have retrieve and install it from the Python Package Repository (pypi).

Type the following command into your terminal:
```
pip install rich
```
If that one doesn't work, you can also try:
```
python3 -m pip install rich
```
The difference is that the first one installs it for everyone on the computer (which might not work due to the way Delta controls permissions on the computers) whereas the second one is only for you when you use the computer.

Once you are done, you can just start using their new print command if you do the following:
```
from rich import print
```
This tells Python to start using the print command that is in the *rich* package instead of it's regular one.  We can add colours or text formatting by adding a markup code to the beginning of a block of text:
```
print("This is not colored, but [bold blue]this is blue[/bold blue]")
```
Note that when you want to end the formatting, you need to put a closing to your markup that begins with a / symbol.  If you end a line, the formatting is reset. (see page 9.py). 

Experiment or google to find some of the options available to you!
You can also check out the documentation at https://rich.readthedocs.io/en/latest/index.html
