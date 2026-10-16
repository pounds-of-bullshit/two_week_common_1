import meto_password as mp
import tkinter as tk
import sys
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5


# updated so that it now also destroys the main index menu
def task1_selection():
    task_selection.destroy()
    t1.task1(client_ID)


def task2_selection():
    task_selection.destroy()
    t2.task2(client_ID)


def task3_selection():
    task_selection.destroy()
    t3.task3(client_ID)


def task4_selection():
    task_selection.destroy()
    t4.task4(client_ID)


def task5_selection():
    task_selection.destroy()
    t5.task5(client_ID)


hey1 = mp.meto_login()

# use these to as clientID and potentially client secret
client_ID = hey1[0]

while True:
    if client_ID != "":

        task_selection = tk.Tk()

        task_selection.geometry("350x200")
        task_selection.title("Task Selection")

        task1_btn = tk.Button(task_selection, text="Task 1", command=task1_selection)  # input client_ID like this
        task2_btn = tk.Button(task_selection, text="Task 2", command=task2_selection)
        task3_btn = tk.Button(task_selection, text="Task 3", command=task3_selection)
        task4_btn = tk.Button(task_selection, text="Task 4", command=task4_selection)
        task5_btn = tk.Button(task_selection, text="Task 5", command=task5_selection)

        close_btn = tk.Button(task_selection, text="Close Script", command=sys.exit)

        task1_btn.grid(row=1)
        task2_btn.grid(row=2)
        task3_btn.grid(row=3)
        task4_btn.grid(row=4)
        task5_btn.grid(row=5)

        close_btn.grid(row=6)

        task_selection.mainloop()
    else:
        sys.exit()
