from tkinter import Text, Tk, Label, Frame, Entry, TOP, LEFT, RIGHT, BOTTOM, PhotoImage, X, Y, BOTH, Button, W, Toplevel, READABLE, StringVar, END
from tkinter.ttk import Combobox, Scrollbar, Treeview
from bl.contact_bl import save_contact
from tkinter.messagebox import showerror, showinfo
import tkinter.messagebox as msg



def show_contact(contact_grid):
    for item in contact_grid.get_children():
        contact_grid.delete(item)

    with open('file/contact.txt', 'r') as file:
        data = file.readlines()
        for idx, line in enumerate(data, 1):
            values = line.strip().split(' - ')
            name = values[0].split(': ')[1]
            family = values[1].split(': ')[1]
            phone = values[3].split(': ')[1]
            gender = values[2].split(': ')[1]
            desc = values[4].split(': ')[1]

            contact_grid.insert('', 'end', values=(name, family, phone, gender, desc))


def show_error_message(errors):
    err_list = []

    for field, msg in errors.items():
        err_list.append(f"Error({field})!, {msg}")

    showerror("Error", "\n".join(err_list))


def show_success_message(errors):
    succ_list = []
    

    for field, msg in errors.items():
        succ_list.append(f"Success({field})!, {msg}")

    showinfo("Success", "\n".join(succ_list))


def contact_data_entry_form():

    def add_btn_onclick():

        contact = (name_var.get(),family_var.get(),phone_var.get(),gender_var.get(),desc_entry.get(1.0,'end-1c'))          

        result = save_contact(contact=contact)
        

        if not result["SUCCESS"]:


            if "name" in result["ERR_MSG"]:
                name_var.set("")

            if "family" in result["ERR_MSG"]:
                family_var.set("")

            if "phone" in result["ERR_MSG"]:
                phone_var.set("")

            if "gender" in result["ERR_MSG"]:
                gender_var.set("")

            show_error_message(result["ERR_MSG"])
        else:
            name_var.set("")
            family_var.set("")
            phone_var.set("")
            gender_var.set("")
            desc_entry.delete(1.0, 'end-1c')
            confirm = msg.askyesno(title='Confirmation', message='Do you want to add another contact?')
            if not confirm:
                back_btn_onclick()

    def back_btn_onclick():
        form.quit()
        form.destroy()

    form = Toplevel()


    # region variable
    name_var = StringVar()
    family_var = StringVar()
    phone_var = StringVar()
    gender_var = StringVar()
    # endregion

    # region config
    form.title("SepidehS3")

    form_width = 600
    form_height = 600
    left_pad = (form.winfo_screenwidth()//2) - (form_width//2)
    top_pad = (form.winfo_screenheight()//2) - (form_height//2)
    form.geometry(f"{form_width}x{form_height}+{left_pad}+{top_pad}")
    form.configure(bg="white")
    app_icon = PhotoImage(file=r"ui/images/icon_main.png")
    form.wm_iconphoto(False, app_icon)
    form.overrideredirect(False)
    # endregion

    # region frame
    header = Frame(
        master=form,
        height=80,
        bg="#665A48",
        highlightthickness=1,
        highlightbackground="#665A48"
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(
        master=form,
        height=80,
        bg="#665A48",
        highlightthickness=1,
        highlightbackground="#665A48"
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = Frame(
        master=form,
        height=80,
        bg="white"
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)

    name_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    name_frame.pack(side=TOP, fill=X, pady=(10, 10), padx=10)
    name_frame.propagate(False)

    family_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    family_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    family_frame.propagate(False)

    phone_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    phone_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    phone_frame.propagate(False)

    gender_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    gender_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    gender_frame.propagate(False)

    description_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    description_frame.pack(fill=BOTH, expand=True, pady=(0, 10), padx=10)
    description_frame.propagate(False)

    # endregion

    # region title app
    title_icon = PhotoImage(file=r"ui/images/entry_icon.png")

    Label(
        master=header,
        text="  Contact data entry form",
        font=("PAPYRUS", 20, 'bold'),
        bg="#665A48",
        image=title_icon,
        compound=LEFT,
        fg="white"
    ).pack(side=TOP, pady=(10, 0))
    # endregion

    # region Button
    back_icon = PhotoImage(file=r"ui/images/back_icon.png")
    Button(
        master=footer,
        text="Back",
        padx=5,
        pady=7,
        font=("PAPYRUS", 10, "bold"),
        image=back_icon,
        compound=LEFT,
        bg="#A9A9A9",
        fg="black",
        activebackground="#A9A9A9",
        activeforeground="black",
        command=back_btn_onclick
    ).pack(side=LEFT, padx=10)

    add_icon = PhotoImage(file=r"ui/images/add_icon.png")
    Button(
        master=footer,
        text="Add",
        padx=6,
        pady=10,
        font=("PAPYRUS", 10, "bold"),
        image=add_icon,
        compound=LEFT,
        bg="#C8DBBE",
        fg="black",
        activebackground="#C8DBBE",
        activeforeground="white",
        command=add_btn_onclick
    ).pack(side=RIGHT, padx=(0, 10))

    # endregion

    # region name
    Label(
        master=name_frame,
        text="First name : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_name=Entry(
        master=name_frame,
        bg="#e7e7e7",
        bd=1,
        textvariable=name_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region family
    Label(
        master=family_frame,
        text="Last name : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_family=Entry(
        master=family_frame,
        bg="#e7e7e7",
        bd=1,
        textvariable=family_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region phone
    Label(
        master=phone_frame,
        text="Phone number : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_phone=Entry(
        master=phone_frame,
        bg="#e7e7e7",
        bd=1,
        textvariable=phone_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region gender
    Label(
        master=gender_frame,
        text="Gender : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_gender=Combobox(
        master=gender_frame,
        values=["male", "female", "other"],
        background="#e7e7e7",
        state='readonly',
        textvariable=gender_var
    ).pack(fill=BOTH, expand=True)

    
    # endregion

    # region textbox
    Label(
        master=description_frame,
        text="Description : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    desc_entry = Text(
        master=description_frame,
        bg="#e7e7e7",
        bd=1
    )
    desc_entry.pack(fill=BOTH, expand=True)

    # endregion


    desc_entry.insert('end','__')

    name_val= name_var.get()
    family_val= family_var.get()
    phone_val= phone_var.get()
    gender_val= gender_var.get()
    des_val= desc_entry.get(1.0,'end-1c')



    
    form.mainloop()
    contact = (name_val,family_val,phone_val,gender_val,des_val)
    return contact


def edit_form(values):

    phone = values[2]
    with open('file/contact.txt', 'r') as file:
        lines = file.readlines()
    with open('file/contact.txt', 'w') as file:
        for line in lines:
            if phone not in line:
                file.write(line)

    def add_btn_onclick():
        
        contact = (name_var.get(),family_var.get(),phone_var.get(),gender_var.get(),desc_entry.get(1.0,'end-1c'))
        
        phone = values[2]
        with open('file/contact.txt', 'r') as file:
            lines = file.readlines()
        with open('file/contact.txt', 'w') as file:
            for line in lines:
                if phone not in line:
                    file.write(line)
        result = save_contact(contact=contact)


        if not result["SUCCESS"]:
            if "name" in result["ERR_MSG"]:
                name_var.set("")

            if "family" in result["ERR_MSG"]:
                family_var.set("")

            if "phone" in result["ERR_MSG"]:
                phone_var.set("")

            if "gender" in result["ERR_MSG"]:
                gender_var.set("")

            show_error_message(result["ERR_MSG"])
            
        else:
            
            name_var.set("")
            family_var.set("")
            phone_var.set("")
            gender_var.set("")
            desc_entry.delete(1.0, 'end-1c')
            show_success_message(result["SUCC_MSG"])
            back_btn_onclick()

    def back_btn_onclick():
        form.quit()
        form.destroy()

    form = Toplevel()

    # region variable
    name_var = StringVar()
    family_var = StringVar()
    phone_var = StringVar()
    gender_var = StringVar()
    # endregion

    # region config
    form.title("SepidehS3")

    form_width = 800
    form_height = 600
    left_pad = (form.winfo_screenwidth()//2) - (form_width//2)
    top_pad = (form.winfo_screenheight()//2) - (form_height//2)
    form.geometry(f"{form_width}x{form_height}+{left_pad}+{top_pad}")
    form.configure(bg="white")
    # form.resizable(width=False, height=False)
    form.overrideredirect(True)

    # endregion

    # region frame
    header = Frame(
        master=form,
        height=80,
        bg="#665A48",
        highlightthickness=1,
        highlightbackground="#665A48"
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(
        master=form,
        height=80,
        bg="#665A48",
        highlightthickness=1,
        highlightbackground="#665A48"
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = Frame(
        master=form,
        height=80,
        bg="white"
    )
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)

    edit_frame = Frame(
        master=body,
        height=50,
        bg="white"
    )
    edit_frame.pack(side=TOP, fill=X, pady=(10, 10), padx=10)
    edit_frame.propagate(False)

    name_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    name_frame.pack(side=TOP, fill=X, pady=(10, 10), padx=10)
    name_frame.propagate(False)

    family_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    family_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    family_frame.propagate(False)

    phone_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    phone_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    phone_frame.propagate(False)

    gender_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    gender_frame.pack(side=TOP, fill=X, pady=(0, 10), padx=10)
    gender_frame.propagate(False)

    description_frame = Frame(
        master=body,
        height=40,
        bg="white"
    )
    description_frame.pack(fill=BOTH, expand=True, pady=(0, 10), padx=10)
    description_frame.propagate(False)

    # endregion

    # region title app
    title_icon = PhotoImage(file=r"ui/images/entry_edit_icon.png")

    Label(
        master=header,
        text="  Edit form",
        font=("PAPYRUS", 20, 'bold'),
        bg="#665A48",
        image=title_icon,
        compound=LEFT,
        fg="white"
    ).pack(side=TOP, pady=(10, 0))
    # endregion

    # region Button
    

    add_icon = PhotoImage(file=r"ui/images/edit_icon.png")
    Button(
        master=footer,
        text="Edit",
        padx=15,
        pady=10,
        font=("PAPYRUS", 10, "bold"),
        image=add_icon,
        compound=LEFT,
        bg="#FFE6BC",
        fg="black",
        activebackground="#FFE6BC",
        activeforeground="white",
        command=add_btn_onclick
    ).pack(side=TOP, padx=(0, 10), pady=(10, 0))

    # endregion

    # region name
    Label(
        master=name_frame,
        text="New First name : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_name=Entry(
        master=name_frame,
        bg="#e7e7e7",
        bd=1,
        textvariable=name_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region family
    Label(
        master=family_frame,
        text="New Last name : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_family=Entry(
        master=family_frame,
        bg="#e7e7e7",
        bd=1,
        textvariable=family_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region phone
    Label(
        master=phone_frame,
        text="New Phone number : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_phone=Entry(
        master=phone_frame,
        bg="#e7e7e7",
        bd=1,
        textvariable=phone_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region gender
    Label(
        master=gender_frame,
        text="New Gender : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    entry_gender=Combobox(
        master=gender_frame,
        values=["male", "female", "other"],
        background="#e7e7e7",
        state='readonly',
        textvariable=gender_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region textbox
    Label(
        master=description_frame,
        text="New Description : ",
        font=("PAPYRUS", 10, "bold"),
        bg="white",
        fg="black",
        anchor=W,
        width=15
    ).pack(side=LEFT)

    desc_entry = Text(
        master=description_frame,
        bg="#e7e7e7",
        bd=1
    )
    desc_entry.pack(fill=BOTH, expand=True)

    # endregion

    # region grid
    contact_grid_edit = Treeview(
        master=edit_frame,
        columns=("name", "family", "phone", "gender", "description"),
        selectmode="extended",
        show="headings"
    )

    contact_grid_edit.heading(column="name", text="Firstname", anchor="center")
    contact_grid_edit.heading(column="family", text="Lastname", anchor="center")
    contact_grid_edit.heading(column="gender", text="Gender", anchor="center")
    contact_grid_edit.heading(column="phone", text="Phone number", anchor="center")
    contact_grid_edit.heading(column="description",
                         text="Description", anchor="center")

    contact_grid_edit.column(column="name",  anchor="center", width=5)
    contact_grid_edit.column(column="family",  anchor="center", width=5)
    contact_grid_edit.column(column="phone",  anchor="center", width=5)
    contact_grid_edit.column(column="gender",  anchor="center", width=5)
    contact_grid_edit.column(column="description",  anchor="center", width=5)

    
    contact_grid_edit.pack(fill=BOTH, expand=True)
    contact_grid_edit.insert('', 'end', values=values)


    #endregion

    name_var.set(values[0])
    family_var.set(values[1])
    phone_var.set(values[2])
    gender_var.set(values[3])
    desc_entry.insert('end',values[4])



    name_val= name_var.get()
    family_val= family_var.get()
    phone_val= phone_var.get()
    gender_val= gender_var.get()
    des_val= desc_entry.get(1.0,'end-1c')



    
    form.mainloop()
    contact = (name_val,family_val,phone_val,gender_val,des_val)
    return contact


def contact_main_form():


    def remove_contact():

        selected_item = contact_grid.selection()
        
        if selected_item:  
            for item in selected_item:
                values = contact_grid.item(item, 'values')
                name = values[0]
                family= values[1]
                phone = values[2]

            message = (f'Fullname: {name} {family}\nPhone: {phone}\nAre you sure you want to delete this contact?')
            confirm = msg.askyesno(title='Confirmation', message=message)
            if confirm:
                for item in selected_item:
                    values = contact_grid.item(item, 'values')
                    phone = values[2]
                    with open('file/contact.txt', 'r') as file:
                        lines = file.readlines()
                    with open('file/contact.txt', 'w') as file:
                        for line in lines:
                            if phone not in line:
                                file.write(line)
                show_contact(contact_grid)  
        else:
            msg.showerror("Error", "Please select a user to delete.")
 
    def exit_btn_onclick():
        form.quit()
        form.destroy()

    def add_btn_onclick():
        form.withdraw()
        contact_data_entry_form()
        form.deiconify()
        show_contact(contact_grid)

    def edit_btn_onclick():
        selected_item = contact_grid.selection()
        if selected_item:
            
            for item in selected_item:
                values = contact_grid.item(item, 'values')
            form.withdraw()
            

            edit_form(values)
            form.deiconify()
            show_contact(contact_grid)
        else:
            msg.showerror("Error", "Please select a user to edit.")

    def show_search(line, contact_grid_search):
        values = line.strip().split(' - ')
        name = values[0].split(': ')[1]
        family = values[1].split(': ')[1]
        phone = values[2].split(': ')[1]
        gender = values[3].split(': ')[1]
        desc = values[4].split(': ')[1]


        contact_grid.insert('', 'end', values=(name, family, gender, phone, desc))

    def showall_btn_onclick():
        show_contact(contact_grid)

    def searchbar_btn_onclick():
        flag = False
        value = value_var.get()
        select = select_var.get()

        if not value:
            showerror("Error", 'Section is empty!')
            flag=True


        for item in contact_grid.get_children():
            contact_grid.delete(item)

        if select == 'Name':
            with open('file/contact.txt', 'r') as file:
                data = file.readlines()
                for idx, line in enumerate(data, 1):
                    values = line.strip().split(' - ')
                    name = values[0].split(': ')[1]
                    if name == value.strip():
                        show_search(line, contact_grid)
                        flag=True
                
        elif select =='Last name':
            with open('file/contact.txt', 'r') as file:
                data = file.readlines()
                for idx, line in enumerate(data, 1):
                    values = line.strip().split(' - ')
                    family = values[1].split(': ')[1]
                    if family == value.strip():
                        show_search(line, contact_grid)
                        flag=True
        elif select == 'Gender':
            with open('file/contact.txt', 'r') as file:
                data = file.readlines()
                for idx, line in enumerate(data, 1):
                    values = line.strip().split(' - ')
                    gender = values[2].split(': ')[1]
                    if gender == value.strip():
                        show_search(line, contact_grid)
                        flag=True
        else:
            with open('file/contact.txt', 'r') as file:
                data = file.readlines()
                for idx, line in enumerate(data, 1):
                    values = line.strip().split(' - ')
                    phone = values[3].split(': ')[1]
                    if phone == value.strip():
                        show_search(line, contact_grid)
                        flag=True

        if not flag:
            showinfo(':(', 'No matching value')

    form = Tk()

    # region config
    form.title("SepidehS3")

    form_width = 800
    form_height = 600
    left_pad = (form.winfo_screenwidth()//2) - (form_width//2)
    top_pad = (form.winfo_screenheight()//2) - (form_height//2)
    form.geometry(f"{form_width}x{form_height}+{left_pad}+{top_pad}")
    form.configure(bg="white")
    app_icon = PhotoImage(file=r"ui/images/icon_main.png")
    form.wm_iconphoto(False, app_icon)
    form.overrideredirect(False)
    
    # endregion

    # region frame
    header = Frame(
        master=form,
        height=80,
        bg="#665A48",
        highlightthickness=1,
        highlightbackground="#665A48"
    )
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    searchbar = Frame(
        master=header,
        height=35,
        width=250,
        bg="#1A5F7A",
        highlightthickness=1,
        highlightbackground="#1A5F7A"

    )
    searchbar.pack(side=RIGHT, padx=(0, 50))
    searchbar.propagate(False)
    

    footer = Frame(
        master=form,
        height=80,
        bg="#665A48",
        highlightthickness=1,
        highlightbackground="#665A48"
    )
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = Frame(
        master=form,
        height=80,
        bg="white"
    )
    body.pack(fill=BOTH, expand=True, padx=10, pady=10)
    body.propagate(False)

    # endregion

    # region title app
    title_icon = PhotoImage(file=r"ui/images/title_icon.png")

    Label(
        master=header,
        text="  Contact main form",
        font=("PAPYRUS", 20, 'bold'),
        bg="#665A48",
        image=title_icon,
        compound=LEFT,
        fg="white"
    ).pack(side=TOP, pady=(10, 0), padx=(100, 0))
    # endregion

    # region Button
    back_icon = PhotoImage(file=r"ui/images/exit_icon.png")
    Button(
        master=footer,
        text='Exit',
        padx=5,
        pady=7,
        font=("PAPYRUS", 10, "bold"),
        compound=LEFT,
        bg="#FF7878",
        fg="black",
        activebackground="#FF7878",
        activeforeground="black",
        command=exit_btn_onclick
    ).pack(side=LEFT, padx=6, pady=1)

    add_icon = PhotoImage(file=r"ui/images/add_icon.png")
    Button(
        master=footer,
        text="Add",
        padx=6,
        pady=10,
        font=("PAPYRUS", 10, "bold"),
        image=add_icon,
        compound=LEFT,
        bg="#C8DBBE",
        fg="black",
        activebackground="#C8DBBE",
        activeforeground="black",
        command=add_btn_onclick
    ).pack(side=RIGHT, padx=(0, 10))

    edit_icon = PhotoImage(file=r"ui/images/edit_icon.png")
    Button(
        master=footer,
        text="Edit",
        padx=6,
        pady=10,
        font=("PAPYRUS", 10, "bold"),
        image=edit_icon,
        compound=LEFT,
        bg="#FFE6BC",
        fg="black",
        activebackground="#FFE6BC",
        activeforeground="black", 
        command=edit_btn_onclick
    ).pack(side=RIGHT, padx=(0, 10))

    remove_icon = PhotoImage(file=r"ui/images/remove_icon.png")
    Button(
        master=footer,
        text="Remove",
        padx=6,
        pady=10,
        font=("PAPYRUS", 10, "bold"),
        image=remove_icon,
        compound=LEFT,
        bg="#FFE3E1",
        fg="black",
        activebackground="#FFE3E1",
        activeforeground="black",
        command= remove_contact
    ).pack(side=RIGHT, padx=(0, 10))


    Button(
        master=footer,
        text="Show All",
        padx=6,
        pady=10,
        font=("PAPYRUS", 10, "bold"),
        compound=LEFT,
        bg="#DEB6AB",
        fg="black",
        activebackground="#DEB6AB",
        activeforeground="black",
        command= showall_btn_onclick
    ).pack(side=RIGHT, padx=(0, 10))

    search_icon_bar = PhotoImage(file=r"ui/images/search_icon.png")
    Button(
        master=searchbar,
        padx=10,
        pady=10,
        width=40,
        font=("PAPYRUS", 10, "bold"),
        compound=LEFT,
        bg="#DAEAF1",
        fg="black",
        activebackground="#DAEAF1",
        activeforeground="black",
        command= searchbar_btn_onclick,
        image=search_icon_bar
    ).pack(side=RIGHT, fill=BOTH)


    # endregion

    # region grid & scrollbar
    scrollbar_x = Scrollbar(master=body, orient="horizontal")
    scrollbar_x.pack(side=BOTTOM, fill=X)

    scrollbar_y = Scrollbar(master=body, orient="vertical")
    scrollbar_y.pack(side=RIGHT, fill=Y)

    contact_grid = Treeview(
        master=body,
        columns=("name", "family", "phone", "gender", "description"),
        selectmode="extended",
        show="headings"
    )

    contact_grid.heading(column="name", text="Firstname", anchor="center")
    contact_grid.heading(column="family", text="Lastname", anchor="center")
    contact_grid.heading(column="gender", text="Gender", anchor="center")
    contact_grid.heading(column="phone", text="Phone number", anchor="center")
    contact_grid.heading(column="description",
                         text="Description", anchor="center")

    contact_grid.column(column="name",  anchor="center", width=5)
    contact_grid.column(column="family",  anchor="center", width=5)
    contact_grid.column(column="phone",  anchor="center", width=5)
    contact_grid.column(column="gender",  anchor="center", width=5)
    contact_grid.column(column="description",  anchor="center", width=70)

    contact_grid.configure(yscrollcommand=scrollbar_y.set,
                           xscrollcommand=scrollbar_x.set)
    
    contact_grid.pack(fill=BOTH, expand=True)
    show_contact(contact_grid)

    scrollbar_y["command"] = contact_grid.yview
    scrollbar_x["command"] = contact_grid.xview


    # endregion

    # region variable
    value_var = StringVar()
    select_var = StringVar(value='search by...')
    # endregion

    #region searchbar

    entry_value=Entry(
        master=searchbar,
        bg="#e7e7e7",
        bd=1,
        textvariable=value_var
    ).pack(fill='both', expand=True, side=RIGHT)

    entry_select=Combobox(
        master=searchbar,
        width=60,
        values=["Name", "Last name", "Phone", 'Gender'],
        background="#e7e7e7",
        state='readonly',
        textvariable=select_var
    ).pack(fill=BOTH, expand=True, side=LEFT)


    #endregion
    
    form.mainloop()
    