from tkinter import *
from tkinter import filedialog, colorchooser, messagebox


class MyNotepad:

    current_file = "no-file"

    def exit_file(self, event=""):
        s = self.txt_area.get(1.0, END)
        if not s.strip():
            quit()
        else:
            result = messagebox.askyesnocancel("Save Dialog Box", "Do you want to save  this file")
            if result == True:
                self.saveas_file()
                quit()
            elif result == False:
                quit()

    def clear(self):
        self.txt_area.delete(1.0, END)

    def new_file(self, event=""):
        s = self.txt_area.get(1.0, END)
        if not s.strip():
            pass
        else:
            result = messagebox.askyesnocancel("Save Dialog Box", "Do you want to save  this file")
            if result == True:
                self.saveas_file()
                self.clear()
            elif result == False:
                self.clear()

    def open_file(self, event=""):
        result = filedialog.askopenfile(initialdir='/', title="Open File", filetype=(("Text File", "*.txt"), ("All Files", "*.*")))
        #print(result)

        # fetching the file data in the text area
        for data in result:
            self.txt_area.insert(INSERT, data)

        self.current_file = result.name

    def saveas_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        data = self.txt_area.get(1.0, END)
        f.write(data)
        self.current_file = f.name
        f.close()

    def save_file(self, event=""):
        if self.current_file == "no-file":
            self.saveas_file()
        else:
            f = open(self.current_file, mode="w")
            f.write(self.txt_area.get(1.0, END))
            f.close()

    def copy_file(self):
        self.txt_area.clipboard_clear()
        self.txt_area.clipboard_append(self.txt_area.selection_get())

    def paste_file(self):
        self.txt_area.insert(INSERT, self.txt_area.clipboard_get())

    def cut_file(self):
        self.copy_file()
        self.txt_area.delete('sel.first', 'sel.last')

    def del_file(self):
        self.txt_area.delete('sel.first', 'sel.last')

    def change_back_color(self):
        c = colorchooser.askcolor()
        self.txt_area.configure(background=c[1])

    def change_fore_color(self):
        c = colorchooser.askcolor()
        self.txt_area.configure(foreground=c[1])


    def __init__(self, master):
        self.master = master
        master.title("MasS Notepad")
        master.wm_iconbitmap("texteditoricon.ico")

        ''' binding the shortcut keys with the functions '''
        master.bind("<Control-o>", self.open_file)  # to execute the open_file function by the shortcut key
        master.bind("<Control-O>", self.open_file)
        master.bind("<Control-s>", self.save_file)  # to execute the save_file function by the shortcut key
        master.bind("<Control-S>", self.save_file)
        master.bind("<Control-n>", self.new_file)  # to execute the new_file function by the shortcut key
        master.bind("<Control-N>", self.new_file)
        master.bind("<Alt-x>", self.exit_file)  # to execute the exit_file function by the shortcut key
        master.bind("<Alt-X>", self.exit_file)


        # creating a text area using text()
        self.txt_area = Text(master,padx=5, pady=5, wrap=WORD,insertwidth=3, bd=5, undo=True)
        self.txt_area.pack(fill=BOTH, expand=1)

        # creating the menu bar
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)  # associating the manu bar with the master

        ''' the file menu'''
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="FILE", menu=self.file_menu)  # adding the file option to the main menu
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)  # adding the new in the file menu
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)  # adding the open in the file menu
        self.file_menu.add_separator()  # adding the separator
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)  # adding the save in the file menu
        self.file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.saveas_file)  # adding the save as in the file menu
        self.file_menu.add_separator()  # adding the separator
        self.file_menu.add_command(label="Exit", accelerator="Alt+X", command=self.exit_file)  # adding the Exit in the file menu

        ############################################################################################################
        ''' the edit menu'''
        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="EDIT", menu=self.edit_menu)  # adding the edit option to the main menu
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.txt_area.edit_undo)# adding the undo in the edit menu

        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.txt_area.edit_redo)
                                     # adding the redo in the edit menu
        self.edit_menu.add_separator()  # adding the separator
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut_file)
                                     # adding the cut in the edit menu
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy_file)
                                     # adding the copy as in the edit menu
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste_file)
                                     # adding the paste in the edit menu
        self.edit_menu.add_separator()  # adding the separator
        self.edit_menu.add_command(label="Delete", command = self.del_file)
                                     # adding the delete in the edit menu

        ###################################################################################################################

        ''' the format menu'''
        self.format_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="FORMAT", menu=self.format_menu)  # adding the edit option to the main menu
        self.format_menu.add_command(label="Background Color",command=self.change_back_color) # adding the background color in the format menu

        self.format_menu.add_command(label="Font Color", command=self.change_fore_color)  # # adding the foreground color in the format menu



root = Tk()


b = MyNotepad(root)

root.geometry('800x600+500+10')
root.mainloop()