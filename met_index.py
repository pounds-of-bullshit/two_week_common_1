import meto_password as mp
import tkinter as tk
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5


# updated so that it now also destroys the main index menu
def task1_selection():
    t1.task1(client_ID)
    task_selection.destroy()


def task2_selection():
    t2.task2(client_ID)
    task_selection.destroy()


def task3_selection():
    t3.task3(client_ID)
    task_selection.destroy()


def task4_selection():
    t4.task4(client_ID)
    task_selection.destroy()


def task5_selection():
    t5.task5(client_ID)
    task_selection.destroy()


hey1 = mp.meto_login()

# use these to as clientID and potentially client secret
client_ID = hey1[0]
client_secret = hey1[1]

task_selection = tk.Tk()

task_selection.geometry("350x200")
task_selection.title("Task Selection")

task1_btn = tk.Button(task_selection, text="Task 1", command=task1_selection)  # input client_ID like this
task2_btn = tk.Button(task_selection, text="Task 2", command=task2_selection)
task3_btn = tk.Button(task_selection, text="Task 3", command=task3_selection)
task4_btn = tk.Button(task_selection, text="Task 4", command=task4_selection)
task5_btn = tk.Button(task_selection, text="Task 5", command=task5_selection)

task1_btn.grid(row=1)
task2_btn.grid(row=2)
task3_btn.grid(row=3)
task4_btn.grid(row=4)
task5_btn.grid(row=5)

task_selection.mainloop()
