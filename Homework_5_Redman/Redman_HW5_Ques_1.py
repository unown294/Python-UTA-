import tkinter
import math
import tkinter.messagebox

class TestAvg:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the five frames.
        self.sideA_frame = tkinter.Frame(self.main_window)
        self.sideB_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for test 1.
        self.sideA_label = tkinter.Label(self.sideA_frame,
                                         text='Side A:')
        self.sideA_entry = tkinter.Entry(self.sideA_frame,
                                         width=30)
        self.sideA_label.pack(side='left')
        self.sideA_entry.pack(side='left')

        # Create and pack the widgets for test 2.
        self.sideB_label = tkinter.Label(self.sideB_frame,
                                         text='Side B:')
        self.sideB_entry = tkinter.Entry(self.sideB_frame,
                                         width=30)
        self.sideB_label.pack(side='left')
        self.sideB_entry.pack(side='left')

        # Create and pack the widgets for the average.
        self.result_label = tkinter.Label(self.avg_frame,
                                          text='Side C:')
        self.avg = tkinter.StringVar() # To update avg_label
        self.avg_label = tkinter.Entry(self.avg_frame,
                                       textvariable=self.avg, width = 30)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Calculate',
                                          command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Exit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')

        # Pack the frames.
        self.sideA_frame.pack()
        self.sideB_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The calc_avg method is the callback function for
    # the calc_button widget.

    def calc_avg(self):
        # Get the three test scores and store them
        # in variables.
        self.sideA = float(self.sideA_entry.get())
        self.sideB = float(self.sideB_entry.get())

        # Calculate the average.
        self.average = math.sqrt(self.sideA**2 + self.sideB**2)

        # Update the avg_label widget by storing
        # the value of self.average in the StringVar
        # object referenced by avg.
        self.avg.set('{:.3f}'.format(self.average))

# Create an instance of the TestAvg class.
test_avg = TestAvg()
