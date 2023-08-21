import tkinter as tk
import serial


arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) 

# Create the main window
window = tk.Tk()
window.title("Stepper Motor")
window.configure(bg="red")

# Create the Current Angle label and text box
current_angle_frame = tk.Frame(window).pack()
current_angle_label = tk.Label(current_angle_frame, text="Angle Buttons", bg="blue")
current_angle_label.pack(side="right")

current_angle_text = tk.StringVar()
current_angle_text.set("0") 

current_angle_entry = tk.Entry(current_angle_frame, textvariable=current_angle_text, state="readonly")
current_angle_entry.pack()

#Input text box
input_frame = tk.Frame(window)
input_frame.pack()

input_label = tk.Label(input_frame, text="Angle Input", bg="blue")
input_label.pack(side="right")

input_text = tk.Entry(input_frame)
input_text.pack(side="left")

# Function to send angle to the stepper motor
# def send_angle(angle, direction):
#     direction = "1" if direction else "0"
#     arduino.write(f"{direction},{angle}".encode())
#     update_current_angle(angle)

# Function to handle button click events
# def button_clicked(angle, direction):
#     direction_value = toggle_clockwise() if direction else toggle_counterclockwise()
#     send_angle(angle, direction_value)
#     update_current_angle(angle)

# Function to toggle the direction buttons
def toggle_clockwise():
    clockwise_button.config(relief="sunken")
    counterclockwise_button.config(relief="raised")
    send_direction(True)  # Send direction as True (clockwise)

def toggle_counterclockwise():
    clockwise_button.config(relief="raised")
    counterclockwise_button.config(relief="sunken")
    send_direction(False)  # Send direction as False (counterclockwise)

# Function to send direction to the stepper motor
def send_direction(direction):
    direction_str = "1" if direction else "0"
    arduino.write(f"d,{direction_str}".encode())

# Function to send angle to the stepper motor
def send_angle(angle):
    arduino.write(f"a,{angle}".encode())
    update_current_angle(angle)

# Function to handle button click events
def button_clicked(angle, direction):
    if direction:
        toggle_clockwise()
    else:
        toggle_counterclockwise()
    send_angle(angle)
    send_direction(direction)
    update_current_angle(angle)

# Function to handle submit button click event
def submit_clicked():
    angle = float(input_text.get())
    closest_angle = round(angle / 1.8) * 1.8
    #clockwise = clockwise_button.config('relief')[-1] == 'sunken'
    # if(toggle_clockwise() == True):
    #     direction = True
    # elif(toggle_counterclockwise() == True):
    #     direction = False

    #send_angle(closest_angle, direction)
    closest_angle = round(angle / 1.8) * 1.8
    # if toggle_clockwise():
    #     direction = True
    # elif toggle_counterclockwise():
    #     direction = False
    send_angle(closest_angle)
    #send_direction(direction)
    # Clear the input box after submission
    input_text.delete(0, tk.END)

# Function to update the current angle display
def update_current_angle(angle):
    current_angle_text.set(str(angle))

# Create the buttons
button_frame = tk.Frame(window)
button_frame.pack()

buttons = [tk.Button(button_frame, text=str(i), command=lambda i=i: button_clicked(i, True)) for i in [0,30,45,60,75, 90,105,120, 135,150,165, 180]]

# Position the buttons in a 3x3 grid
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3, pady=5)

# Create the clockwise and counterclockwise buttons
toggle_frame = tk.Frame(window)
toggle_frame.pack()

clockwise_button = tk.Button(toggle_frame, text="CW", relief="sunken")
clockwise_button.pack(side="left")

counterclockwise_button = tk.Button(toggle_frame, text="CCW", relief="raised")
counterclockwise_button.pack(side="left")

# Function to toggle the direction buttons
# def toggle_clockwise():
#     clockwise_button.config(relief="sunken")
#     counterclockwise_button.config(relief="raised")
#     return True

# def toggle_counterclockwise():
#     clockwise_button.config(relief="raised")
#     counterclockwise_button.config(relief="sunken")
#     return False


clockwise_button.config(command=toggle_clockwise)
counterclockwise_button.config(command=toggle_counterclockwise)

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit_clicked)
submit_button.pack()

# Start the GUI event loop
window.mainloop()
