# %% 

# import 
import tkinter
import time

# create window
root = tkinter.Tk()
root.title("nearest to zero")
root.geometry("200x100")

# init tkinter variables
timer_var = tkinter.StringVar()
score_var = tkinter.StringVar()

# init locals
time_left = 0
time_step = 10 # in ms
game_running = False
time_start = 3000 # in ms
best_score = time_start

# start timer callback
def start_timer():

    # declare globals
    global time_left, game_running

    # update locals
    time_left = time_start
    game_running = True

    # update button text and callback
    button.configure(command = stop_timer, text = "Stop")

    # trigger first update
    update()

# stop timer callback
def stop_timer(register_score = True):

    # declare globals
    global game_running, best_score

    # flag game stop
    game_running = False

    # update button text and callback
    button.configure(command = start_timer, text = "Start")

    # discard remainder if no register score required
    if( not register_score ): return
    
    # register score
    if( time_left < best_score ):

        # update locals/ui 
        best_score = time_left
        score_var.set(f"best score: {best_score}")
    
# ui update
def update():

    # exit if game over
    if( not game_running ): return 

    # declare globals
    global time_left

    # decrement time
    time_left -= time_step

    # exit 
    if( time_left < 0 ):
        stop_timer(False)
        return 

    # update ui 
    timer_var.set(str(time_left))

    # restart callback
    timer = root.after(time_step, update)

# create ui elements
button = tkinter.Button(root, text="Start", command=start_timer)
button.pack()
label_number = tkinter.Label(root, textvariable=timer_var)
label_number.pack()
label_score = tkinter.Label(root, textvariable=score_var)
label_score.pack()

# start ui
root.mainloop()