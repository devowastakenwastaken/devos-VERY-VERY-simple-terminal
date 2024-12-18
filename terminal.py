import sys, os, shutil, random, platform, time
from random import randint
import tkinter
import os
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *



# Add source code to any extensions here, if you would like to remove them all then delete everything from extensions and replace it with the 'pass' function.

extensionlist = ['base.hello-world', 'base.calculator', 'base.notepad', 'base.echo', 'base.platform', 'base.diskspace', 'base.help']

# Hello-world example extension, called in the terminal by using the 'hello-world' command
def helloworld():
    print('Hello World!')

# Basic calculator function, called by running 'calc'
def calculator():
    calcnum1 = int(input('Value 1: '))
    calcnum2 = int(input('Value 2: '))
    func = input('Operation (*, /, + or -): ')
    if func == '*':
        print(calcnum1 * calcnum2)
    if func == '/':
        print(calcnum1 / calcnum2)
    if func == '+':
        print(calcnum1 + calcnum2)
    if func == '-':
        print(calcnum1 - calcnum2)
    if calcnum1 == '0':
        if func == '/':
            print('Error: division by zero')
    if calcnum2 == '0':
        if func == '/':
            print('Error: division by zero')

# Notepad function
def notepad():
    class Notepad:

        __root = Tk()
        # default window width and height
        __thisWidth = 300
        __thisHeight = 300
        __thisTextArea = Text(__root)
        __thisMenuBar = Menu(__root)
        __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
        __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
        # To add scrollbar
        __thisScrollBar = Scrollbar(__thisTextArea)
        __file = None

        def __init__(self, **kwargs):
            # Set icon
            try:
                self.__root.wm_iconbitmap("Notepad.ico")
            except:
                pass
            # Set window size (the default is 300x300)
            try:
                self.__thisWidth = kwargs['width']
            except KeyError:
                pass

            try:
                self.__thisHeight = kwargs['height']
            except KeyError:
                pass

            # Set the window text
            self.__root.title("Untitled - Notepad")
            # Center the window
            screenWidth = self.__root.winfo_screenwidth()
            screenHeight = self.__root.winfo_screenheight()
            # For left-alling
            left = (screenWidth / 2) - (self.__thisWidth / 2)
            # For right-allign
            top = (screenHeight / 2) - (self.__thisHeight / 2)
            # For top and bottom

            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                                  self.__thisHeight,
                                                  left, top))
            # To make the textarea auto resizable
            self.__root.grid_rowconfigure(0, weight=3)
            self.__root.grid_columnconfigure(0, weight=3)

            # Add controls (widget)
            self.__thisTextArea.grid(sticky=N + E + S + W)
            # To open new file
            self.__thisFileMenu.add_command(label="New",
                                            command=self.__newFile)
            # To open a already existing file
            self.__thisFileMenu.add_command(label="Open",
                                            command=self.__openFile)
            # To save current file
            self.__thisFileMenu.add_command(label="Save",
                                            command=self.__saveFile)
            # To create a line in the dialog
            self.__thisFileMenu.add_separator()
            self.__thisFileMenu.add_command(label="Exit",
                                            command=self.__quitApplication)
            self.__thisMenuBar.add_cascade(label="File",
                                           menu=self.__thisFileMenu)
            # To give a feature of cut
            self.__thisEditMenu.add_command(label="Cut",
                                            command=self.__cut)
            # to give a feature of copy
            self.__thisEditMenu.add_command(label="Copy",
                                            command=self.__copy)
            # To give a feature of paste
            self.__thisEditMenu.add_command(label="Paste",
                                            command=self.__paste)
            # To give a feature of editing
            self.__thisMenuBar.add_cascade(label="Edit",
                                           menu=self.__thisEditMenu)
            # To create a feature of description of the notepad
            self.__thisHelpMenu.add_command(label="View Help",
                                            command=self.__showAbout)
            self.__thisMenuBar.add_cascade(label="Help",
                                           menu=self.__thisHelpMenu)
            self.__root.config(menu=self.__thisMenuBar)
            self.__thisScrollBar.pack(side=RIGHT, fill=Y)
            # Scrollbar will adjust automatically according to the content
            self.__thisScrollBar.config(command=self.__thisTextArea.yview)
            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        def __quitApplication(self):
            self.__root.destroy()

        # exit()
        def __showAbout(self):
            showinfo("Notepad", view=webbrowser.open(
                "https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA"))

        def __openFile(self):
            self.__file = askopenfilename(defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"),
                                                     ("Text Documents", "*.txt")])
            if self.__file == "":
                # no file to open
                self.__file = None
            else:
                # Try to open the file
                # set the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                self.__thisTextArea.delete(1.0, END)
                file = open(self.__file, "r")
                self.__thisTextArea.insert(1.0, file.read())
                file.close()

        def __newFile(self):
            self.__root.title("Untitled - Notepad")
            self.__file = None
            self.__thisTextArea.delete(1.0, END)

        def __saveFile(self):

            if self.__file == None:
                # Save as new file
                self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                defaultextension=".txt",
                                                filetypes=[("All Files", "*.*"),
                                                           ("Text Documents", "*.txt")])

                if self.__file == "":
                    self.__file = None
                else:
                    # Try to save the file
                    file = open(self.__file, "Untitled")
                    file.write(self.__thisTextArea.get(1.0, END))
                    file.close()

                    # Change the window title
                    self.__root.title(os.path.basename(self.__file) + " - Notepad")

            else:
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

        def __cut(self):
            self.__thisTextArea.event_generate("<<Cut>>")

        def __copy(self):
            self.__thisTextArea.event_generate("<<Copy>>")

        def __paste(self):
            self.__thisTextArea.event_generate("<<Paste>>")

        def run(self):
            # Run main application
            self.__root.mainloop()

    # Run main application
    notepad = Notepad(width=600, height=400)
    notepad.run()

# Echo function
def echo():
    echo = input('echo? >>> ')
    print(echo)

# Shows platform and OS version
def plat():
    print(f'\\terminal.py - platform.platform >>> $ {platform.platform()} \n'
          f'\\terminal.py - platform.system >>> $ {platform.system()} \n'
          f'\\terminal.py - platform.release >>> $ {platform.release()}')

# Extension to show disk space in GB
def diskspace():
    total, used, free = shutil.disk_usage("/")

    print("Total space: %d GB" % (total // (2**30)))
    print("Used space: %d GB" % (used // (2**30)))
    print("Free space: %d GB" % (free // (2**30)))

# Help text
def helptxt():
    print('echo = asks for an input that, when filled, repeats the input in the terminal \n'
          'platform = shows the platform, OS and version that the terminal is running on \n'
          'disk = shows total, used and free diskspace on the drive the terminal is on \n'
          'quit = quits the program \n'
          'notepad = opens a notepad app (source code by Pratyush Jain, https://github.com/pratyushjain122) \n'
          '? = shows this text')

# End extensions area here.

print('Starting terminal...')
time.sleep(0.325)

while True:         
    terminalinput = input('>>> ')
    if terminalinput == 'echo':
        echo()
    elif terminalinput == 'platform':
        plat()
    elif terminalinput == 'disk':
        diskspace()
    elif terminalinput == 'quit':
        print('Goodbye!')
        time.sleep(0.25)
        exit()
    elif terminalinput == 'notepad':
        notepad()
    elif terminalinput == 'gui':
        pass
    elif terminalinput == 'calc':
        calculator()
    elif terminalinput == 'hello-world':
        helloworld()
    elif terminalinput == '?':
        helptxt()
    elif terminalinput == 'extensions':
        print('Extensions:', extensionlist)
    elif terminalinput == 'git':
        print('https://github.com/devowastakenwastaken/devos-simple-terminal')
    else:
        print('Exception in ~terminal.py: unknown command or function entered')



# Objectives:
# Add disk function ✔
# Add echo ✔
# Add install function - Extensions are good anough howay man
# Add YT to MP4 downloader
# Add system-intertwined commands (shutdown, install)
