# import 
import tkinter
import random
import customtkinter

# define participant list
# participant_names = ["A", "B", "C", "D", "E", "F", "G"]
participant_names = ["Herman Von Hessiflag", "B", "C"]

# sanity check 
if( len(participant_names) < 2 ): raise Exception("list too short, while loop will infinite")

# create window
root = tkinter.Tk()
root.title("random student picker")
root.geometry("1400x550")

# init locals
number_var = tkinter.StringVar()
random_ids = []
last_id = -1

# local function
def get_list_random_ids(length):
    ids = [x for x in range(length)]
    random.shuffle(ids)
    return ids

# callbacks
def generate_random():

    # define global to enable writing in variable
    global random_ids, last_id
    
    # reset list if required
    if( len(random_ids) == 0 ):
        random_ids = get_list_random_ids(len(participant_names))

        # re-run if next first is same as last
        while( random_ids[-1] == last_id ):
            random_ids = get_list_random_ids(len(participant_names))
    
    # get next participant
    id = random_ids.pop()

    # remember las id
    if( len(random_ids) == 0): last_id = id
    
    # update locals
    number_var.set(participant_names[id])

# create ui elements
button_generate = customtkinter.CTkButton(root, text="Pick Next", width=500, font=("Roboto", 100, "normal"), command=generate_random, fg_color="gray99", text_color="gray20", hover_color="gray90", border_width=2, border_color="gray20")
button_generate.pack(padx=20, pady=30)
customtkinter.CTkLabel(root, textvariable=number_var, font=("Roboto", 100, "normal"), text_color="gray20").pack(padx=20, pady=50)

# # set ui scale
# customtkinter.set_widget_scaling(1)

# start ui
root.mainloop()