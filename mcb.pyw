# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usages: py.exe mcb.pyw save <keyword> Saves clipboard to keybword
#        py.exe mcb.pyw <keyword> - leads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open ("mcb")
#TODO save slipboard content

if len(sys.argv)== 3 and sys.argv[1].lower()=="save":
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
#TODO list keyswords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys)))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.cloce()
