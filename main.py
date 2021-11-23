# project by @shreyamalogi
# date: 23/11/21

# in the given grid design.png when we break it down we can see that 
# the window has 4 label widgets, 1 button widget, 1 input widget


#import all classes from tkinter
from tkinter import *

#create window from Tk class
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

#define the functionality for converting miles input to kilometer output
def miles_to_km():
    miles = float(miles_input.get())                                     #as the value is in decimal make sure to change the data type to float
    km    = miles * 1.609
    kilometer_result_label.config(text=f"{km}")                         #wrap the km into f string and then convert into srting to put into my label                      #get hold of the kilometer result label and change the text by using config
                                                                        #THEN WE NEED TO TRIGGER THE DEF AND ADD IT AS COMMAND IN THE END

#the miles input widget will be created from the                        Entry class
miles_input = Entry(width = 10)
miles_input.grid(column=1, row=0)                                       #grid of rows and columns for each widget

#the miles text label widget will be created from the                   Label class which holds the text miles
miles_label = Label(text = "Miles")
miles_label.grid(column=2, row=0)

#the is equal to label widget will be created from the                  Label class which holds the text is equal to
is_equal_to_label = Label(text = " Is Equal To" )  
is_equal_to_label.grid(column=0, row=1)

#the kilometer result label widget will be created from the            Label class which holds the text a 0    ( big fat 0)
kilometer_result_label = Label(text = "0")
kilometer_result_label.grid(column=1, row=1)

#the kilometer text label widget will be created from the               Label class which holds the text km
kilometer_label = Label(text = "km")
kilometer_label.grid(column=2, row=1)

#the calculate button widget will be created from the                   Button class which holds the text calculate
calculate_button = Button (text = "Calculate", command= miles_to_km)
calculate_button.grid(column=1, row=2)


#to display our window and start running in the main loop
window.mainloop()