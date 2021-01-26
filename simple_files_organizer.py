# A Simple Files Organizer

# This project is used to arrange and separate/organize different types of millions of files having different extentions present in a single folder into new folders with respect to the file types.


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import shutil
import time



# GUI
main_app = tk.Tk()
main_app.geometry("550x180+550+180")
main_app.title("Simple Files Organizer")
main_app.resizable(0,0)

label_frame = ttk.LabelFrame(main_app, text = 'A simple files organizer/separator')
label_frame.pack(pady = 25)

path_label = ttk.Label(label_frame, text = 'Enter the path of the folder in "" to organize its files : ')
path_label.grid(row = 0, column = 0, padx = 5, pady = 10)

path_entry_var = tk.StringVar()                                                                           # User inputs the desired path get stored
path_entry = ttk.Entry(label_frame, width = 40, textvariable = path_entry_var)
path_entry.grid(row = 0, column = 1, padx = 5, pady = 10)

time_label = ttk.Label(main_app, text = f"Time Taken : ")
time_label.pack(side = tk.BOTTOM)



def organize() :

    global time_label

    try :                                                                                                 # For Exception Handling
        mixed_files_folder_path = path_entry_var.get()                                                    # Get path from user entry box

        t1 = time.time()                                                                                  # Initial time for program


        all_files_extentions_dict = {                                                                     # All extensions of files with file type
            "Audio" : ('.mp3','.m3u','.wav','.flac','.vorbis','.pls','.qcp','.aes3','.rf64','.adx','.vgm'),                                            # Can add more extensions if needed
            "Video" : ('.webm','.mpg','.mp2','.mpeg','.mpe','.mkv','.ogg','.mp4','.m4p','.mav','.avi','.wmv','.mov','.qt','.flv','.swf','.avchd'),
            "Document" : ('.txt','.docx','.xlsx','.py','.pdf','.doc','.html','.htm','.odt','.xls','.ods','.ppt','.pptx')
        }


        def files_of_same_format(folder_path, file_extensions) :                                          # This function returns a list containing files with same format for ex : audio only, video only
            return (file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension))                             # A Generator which can return millions of files in less time, memory, performance


            
        # This code will create a new folders with new path and move files into it which are separated with same format
        for file_format_dict, file_extensions_dict in all_files_extentions_dict.items() :                 # A loop on files extension dict       
            separated_folder_name = file_format_dict + " Files"                                           # Create new folder name
            separated_folder_path = os.path.join(mixed_files_folder_path,separated_folder_name)           # Create new folder path
            while True :                                                                                  # A infinite loop for more feature
                if os.path.exists(separated_folder_path) :                                                # If folder already exist then code to move file in that folder
                    for item in files_of_same_format(mixed_files_folder_path, file_extensions_dict) :           
                        item_old_path = os.path.join(mixed_files_folder_path,item)                                 
                        item_new_path = os.path.join(separated_folder_path,item)
                        shutil.move(item_old_path,item_new_path)                                          # Move file from old folder to new organised folder
                else :
                    os.mkdir(separated_folder_path)                                                       # Create a new folder if not exists already
                    continue
                break
        

        # This code is used to remove the empty folders, if created or present after the files get separated
        for folder in os.listdir(mixed_files_folder_path) :
            folderpath = os.path.join(mixed_files_folder_path,folder)
            directory = os.listdir(folderpath)
            if len(directory) == 0:
                os.rmdir(folderpath) 


        t2 = time.time()                                                                                   # Final time for program
        t = t2 - t1                                                                                        # Time required

        time_label.config(text = f"Time Taken   :   {round(t, 2)}")                                        # Config time label with time


        messagebox.showinfo("Completed","All of your files have been Successfully Organized !")    

    except :
        return    



organize_button = ttk.Button(label_frame, text = 'ORGANIZE', command = organize)
organize_button.grid(row = 1, columnspan = 2 , padx = 50, pady = 10)



main_app.mainloop()