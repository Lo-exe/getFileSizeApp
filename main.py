import os
import tkinter as tk
from tkinter import filedialog
import tkinter.font as TkFont
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, FONT_FAMILY, FONT_SIZE, LABEL_PADX, LABEL_PADY

class FileSizeApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Get File Size') 
        self.master.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}') # Window Size
        self.font = TkFont.Font(family=f'{FONT_FAMILY}', size=FONT_SIZE)

        self.upload_button = tk.Button(self.master, text='Open', width=25, command=self.upload_file, font=self.font)
        self.upload_button.pack(pady=20)

        self.file_label = self.create_label('')
        self.file_size_label = self.create_label('')
    
    def create_label(self, text: str):
        self.label = tk.Label(self.master, text=text, anchor='w')
        self.label.pack(fill='both', padx=LABEL_PADX, pady=LABEL_PADY) 
        return self.label

    def get_file_size(self, file: str):
        return os.path.getsize(file)

    def upload_file(self):
        filename = filedialog.askopenfilename()

        if filename:  
            file_size = self.get_file_size(filename)
            file_name = os.path.basename(filename)

            self.file_label.config(text=f'File: {file_name}', background='lightgreen', fg='white', font=self.font)
            self.file_size_label.config(text=f'Size: {file_size}bytes', background='lightgreen', fg='white', font=self.font)

def main():
    root = tk.Tk()
    app = FileSizeApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
