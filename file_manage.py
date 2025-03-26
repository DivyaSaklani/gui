import os
import tkinter as tk
from tkinter import messagebox ,filedialog


def home_screen():
    #Buttons to perform the operation
    home_frame.pack(pady=20)
    create_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()
    dir_frame.pack_forget()


def show_create():
    create_frame.pack(pady = 20)
    home_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()
    dir_frame.pack_forget()

def show_update():
    update_frame.pack(pady=20)
    home_frame.pack_forget()
    create_frame.pack_forget()
    delete_frame.pack_forget()
    dir_frame.pack_forget()


def show_delete():
    delete_frame.pack(pady=20)
    home_frame.pack_forget()
    create_frame.pack_forget()
    update_frame.pack_forget()
    dir_frame.pack_forget()
    
def show_directory():
    dir_frame.pack(pady=20)
    home_frame.pack_forget()
    create_frame.pack_forget()
    update_frame.pack_forget()
    delete_frame.pack_forget()
    
        

def create_file():
    filename  = file_entry.get()
    if filename:
        with open(filename, 'x') as f :#we use with so that the .close no need to be written
           
            messagebox.showinfo("success",f"file name {filename}-created successfully!")
    
    #same file name
    elif FileExistsError:
        messagebox.showwarning("warning",f"file name {filename} exist already change the name")
    
    #any other exception
    else:
        messagebox.showerror("error",f'An error occured ')


def view_all_files():
    directory = filedialog.askdirectory() #we here ask for the list of the directory in which the file exist
    if directory:
        file_list.delete(0,tk.END)
        files =os.listdir(directory)
        for f in files:
            file_list.insert(tk.END,f)
        
    else:
        messagebox.showerror("No directroy")
       

def delete_file():
    filename = file_entry.get()
    if filename and os.path.exists(filename):
        os.remove(filename)
        file_entry.delete(0,tk.END)
        """ text_area.delete("1.0" ,tk.END) """
        messagebox.showinfo("Success",f"{filename} has been removed")

    else:
        messagebox.showerror("Error",f"{filename} not found")
    


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"content of file {filename} is :\n{content}")
    
    except FileNotFoundError:
        print("file not found")
    
    except Exception as E:
        print(f"Error occured {E}")

def write_file(filename):
    try:
        file = open(filename, 'w')
        file.write("this is code to perform various file operation")

    except FileNotFoundError:
        print("no file found with this name")
    
    
    except Exception as E:
        print(f"Error occured {E}")
    

def edit_file():
    filename = file_entry.get().strip()

    if not filename:
        messagebox.showerror("Error","Enter the file name")
        return
    content = text_update.get(1.0 , tk.END).strip()
    if not content:
        messagebox.showerror("Error","Enter the content to be appended to the file")
        return 

    try:
        with open(filename,'a',encoding = "utf-8") as f:
            
            f.write(content)
            messagebox.showinfo("success",f'content added to {filename} successfully')
    except FileNotFoundError:
        messagebox.showerror("error","no file found with this name")
    
    except Exception as E:
        messagebox.showerror("Error",f"Error occured {E}")

""" def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: To Create a file')
        print('2: To view all file')
        print('3: To Delete a file')
        print('4: To Read a file')
        print('5: To Edit a file')
        print('6: Exit')

        choice =input('Enter your choice (1-6): ')
        
        if choice == '1':
            filename = input("Enter the file name : ")
            create_file(filename)
        
        elif choice =='2':
            view_all_files()
        
        elif choice =='3':
            filename=input("Enter the file name to be deleted :")
            delete_file(filename)
            
        
        elif choice =='4':
            filename = input("Enter the file name :")
            read_file(filename)
        
        elif choice =='5':
            filename = input("enter the file name to be edited")
            edit_file(filename)

        elif choice =='6':
            print("closing the app")
            break

        else:
            print("invalid option")

if __name__ =="__main__":
    main() """

#initialize Tkinter
root =tk.Tk()
root.title("File Operation")
root.geometry("500x500")
root.configure(bg="#0A192F")

#home Screen
home_frame = tk.Frame(root)
home_frame.pack(pady=30)
home_frame.configure(bg="#0A192F")
tk.Label(home_frame,text="File Operations",font=("Arial",16,"bold"),fg="White",bg="#0A192F").pack(pady=20)
tk.Button(home_frame, text="Create File", command=show_create).pack(pady=10)
tk.Button(home_frame, text="Update File", command=show_update).pack(pady=10)
tk.Button(home_frame, text="View Directory", command=show_directory).pack(pady=10)
tk.Button(home_frame, text="Delete File", command=show_delete).pack(pady=10)




#Create File frame
create_frame  = tk.Frame(root)
create1_frame=tk.Frame(create_frame)
create1_frame.pack(pady=10)
create_frame.configure(bg="#0A192F")
create1_frame.configure(bg="#0A192F")

tk.Label(create1_frame, text="Create A File",font=("Arial",15,"bold"),fg="White",bg="#0A192F").pack(pady =50)
label1=tk.Label(create1_frame,text="File Name : ",font=("Arial",12,"bold"),fg="White",bg="#0A192F")
label1.pack(side="left",padx=5)

file_entry  = tk.Entry(create1_frame, width=30)
file_entry.pack( side="right",padx=5)
tk.Button(create_frame, text="Create File", command=create_file).pack(pady=20)
tk.Button(create_frame, text="Back", command=home_screen).pack(pady=10)


#update file frame
update_frame = tk.Frame(root)
update_frame.configure(bg="#0A192F")
tk.Label(update_frame,text="Update A file",font=("Arial",15,"bold"),fg="White",bg="#0A192F").pack(pady =10,padx =20)
tk.Label(update_frame,text="File Name",font=("Arial",12,"bold"),fg="White",bg="#0A192F").pack(pady=10)
file_entry = tk.Entry(update_frame, width =30)
file_entry.pack(padx = 15)

tk.Label(update_frame,text="Write the content",font=("Arial",12,"bold"),fg="White",bg="#0A192F").pack(pady=10)
text_update = tk.Text(update_frame, width =50 , height =10)
text_update.pack(padx=15)

tk.Button(update_frame, text="Update", command=edit_file).pack(pady=10)
tk.Button(update_frame, text="Back", command=home_screen).pack(pady=5)



#delete file frame
delete_frame = tk.Frame(root)
delete1_frame = tk.Frame(delete_frame)
delete1_frame.pack(pady=20)
delete_frame.configure(bg="#0A192F")
delete1_frame.configure(bg="#0A192F")
tk.Label(delete1_frame,text="Delete A file",font=("Arial",15,"bold"),fg="White",bg="#0A192F").pack(pady =10,padx =20)
tk.Label(delete1_frame,text="File Name",font=("Arial",12,"bold"),fg="White",bg="#0A192F").pack(pady=10, side="left")
file_entry = tk.Entry(delete1_frame, width = 30)
file_entry.pack(padx = 15, side="right")


tk.Button(delete_frame, text="delete", command=delete_file).pack(pady=10)
tk.Button(delete_frame, text="Back", command=home_screen).pack(pady=5)


#show dir frame
dir_frame = tk.Frame(root)

dir_frame.configure(bg="#0A192F")

tk.Label(dir_frame,text="Veiw Directory",font=("Arial",15,"bold"),fg="White",bg="#0A192F").pack(pady =10,padx =20)
""" tk.Label(dir_frame,text="File Name",font=("Arial",12,"bold"),fg="White",bg="#0A192F").pack(pady=10, side="left")
file_entry = tk.Entry(dir_frame, width = 30) """
file_entry.pack(padx = 15, side="right")

file_list =tk.Listbox(dir_frame,width=30,height= 10)
file_list.pack(pady =12)


tk.Button(dir_frame, text="Select Directory", command=view_all_files).pack(pady=10)
tk.Button(dir_frame, text="Back", command=home_screen).pack(pady=5)



#Text area for file content 
""" text_area = tk.Text(create_frame, height =10, width = 50)
text_area.pack(pady=5)
 """

""" 
file_list =tk.Listbox(root,width=100 ,height= 150)
file_list.pack(pady =12) """

home_screen()

root.mainloop()