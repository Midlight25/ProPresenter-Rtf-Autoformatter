# ProPresenter-Rtf-Autoformatter
Python script, takes in input of rtf file you need to format and outputs formatted rtf file for ProPresenter import with line break delimiters.

## Background:
My church uses ProPresenter 5 to display the lyrics to hymns for the congregation. Every Saturday, we receive the lyrics in an email, which we then copy to an .rtf file using Word. Sometimes, the copying does not go through correctly and we have many "line breaks" instead of "paragraph breaks" in our file. ProPresenter separates the slides based on the "paragraph breaks," which means in order for the lyrics to display correctly on the slide, all of the "line breaks" have to be changed to "paragraph breaks." Until now, that had to be done manually. The task is tedious and time consuming; so in a fit of rage, I sat down and wrote a function that would take care of doing that task for me. This is what you see here.

This python script is written in such a way that if you wanted to, you could also import the function that I wrote to use in your code. If the script is run natively, it will perform the function on its own, so it's both a program and a module. Currently, I only have the command-line interface programed, and it's simple. Just write the full path of each file after the program line. It can accept an unlimited number of files by calling the program name from the command line and calling files after the program. There is also a simple stand alone CLI that can be accessed by running the file or running it from the command line without any arguments.

## Disclaimer:
The function will only convert line-breaks to paragraph breaks so that the file will work correctly in ProPresenter, so I apologize if you were searching for something else.

For any questions, just contact me through the channels that GitHub provides. *At this point, I an inexperienced programmer and this was my first project so please be kind. Thank you!
