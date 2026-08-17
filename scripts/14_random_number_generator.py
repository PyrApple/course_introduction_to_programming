# %% 

# import 
import tkinter
import random

# create window
root = tkinter.Tk()
root.title("random generator")
root.geometry("200x100")

# init locals
number_var = tkinter.StringVar()
number_var.set("-1")

# callbacks
def generate_random():
    
    # generate random
    n = random.randint(0, 100)
    
    # update locals
    number_var.set(str(n))

# create ui elements
button_generate = tkinter.Button(root, text="Generate Number", command=generate_random)
button_generate.pack()
label_number = tkinter.Label(root, textvariable=number_var)
label_number.pack()

# start ui
root.mainloop()