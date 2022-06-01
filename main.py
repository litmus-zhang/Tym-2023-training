from tkinter import *



def add_item(entry : Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open("tasks.txt", "a") as tasks_list_file:
        tasks_list_file.write(f"\n{new_task}")
        # tasks_list.close()


def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open("tasks.txt", "r+") as tasks_list_file:
        lines = tasks_list_file.readlines()
        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            
            tasks_list_file.write(line)
        tasks_list_file.close()

# GUI of the application

root = Tk()
root.title("Team Contechs To-Do List")

root.geometry('300x400')

root.resizable(0, 0)

root.configure(bg='#00bfff')

#Heading label
Label(root, text="Contechs To Do List", bg='palevioletred', font=("Arial", 15), wraplength=300).place(x=35, y=0)



# List of tasks
tasks = Listbox(root, selectbackground="Gold", bg='Silver', font=('Arial', 12), height=12, width=25)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=232)


tasks.config(yscrollcommand=scroller.set)

tasks.place(x=35, y=50)


# Adding items to list box
with open("tasks.txt", "r+") as tasks_list:
    for line in tasks_list:
        tasks.insert(END, line)
    tasks_list.close()


# Creating the entry widget to enter a new task
new_item_entry = Entry(root, width=37)
new_item_entry.place(x=35, y=310)


# Creating the button to add a new task

add_btn = Button(root, text="Add Item", bg="Azure", width=10, font=('Arial', 12), command=lambda: add_item(new_item_entry, tasks))


add_btn.place(x=35, y=350)


delete_btn = Button(root, text="Delete Item", bg="Azure", width=10, font=('Arial', 12), command=lambda: delete_item(tasks))

delete_btn.place(x=150, y=350)

# Finanlizing the window
root.update()
root.mainloop()




# The functions  to add and delete items

