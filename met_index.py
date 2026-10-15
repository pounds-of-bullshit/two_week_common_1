import meto_password as mp
import tkinter as tk
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5


hey1 = mp.meto_login()

# use these to as clientID and potentially client secret
client_ID = hey1[0]
client_secret = hey1[1]

task_selection = tk.Tk()

task_selection.geometry("350x200")
task_selection.title("Task Selection")

task1_btn = tk.Button(task_selection, text="Task 1", command=t1.task1(client_ID))  # input client_ID like this
task2_btn = tk.Button(task_selection, text="Task 2", command=t2.task2())
task3_btn = tk.Button(task_selection, text="Task 3", command=t3.task3())
task4_btn = tk.Button(task_selection, text="Task 4", command=t4.task4())
task5_btn = tk.Button(task_selection, text="Task 5", command=t5.task5())

task1_btn.grid(row=1)
task2_btn.grid(row=2)
task3_btn.grid(row=3)
task4_btn.grid(row=4)
task5_btn.grid(row=5)

task_selection.mainloop()
