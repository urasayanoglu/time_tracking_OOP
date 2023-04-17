import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import simpledialog
#from PIL import Image, ImageTk
from pathlib import Path
from time import strftime



#import time_tracking_calendar 
import work_day
import day_stats

class TimeTracker(tk.Tk):
    """Time tracker main window"""

    def __init__(self):
        super().__init__()

        # root window
        self.title("Work Time Tracker ver 0.1.0")

        # window size and position
        self.geometry("%dx%d" % (self.winfo_screenwidth() * 1//3, self.winfo_screenheight() * 1//3))
    
        # bind close window event
        self.protocol("WM_DELETE_WINDOW", self.__close)
        
        # Show the the day information
        self.day = work_day.WorkDay()
        
        # Show the the day information
        self.work_day_label = ttk.Label(self, text=f"{self.day}")
        self.work_day_label.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

        # Show actual time
        self.time_label = ttk.Label(self, text="Time")
        self.time_label.grid(row=0, column=4, sticky=tk.NE)

        # Display Informaton about the current work day
        day_info_frame = ttk.Frame(self)
        self.work_status_label = ttk.Label(day_info_frame, text=f"{self.day.work_status}")
        self.work_status_label.pack(side=tk.TOP)
        day_info_frame.grid(row=2, column=0, rowspan=3 ,columnspan=4, sticky=tk.NSEW)

        
        # Create buttons
        work_start_button = ttk.Button(self, text="Day Start", command=lambda: self.__start_work_day())
        work_start_button.grid(row=5, column=0, padx=2, pady=2, sticky=tk.NSEW)

        work_end_button = ttk.Button(self, text="Day End", command=lambda: self.__end_work_day())
        work_end_button.grid(row=5, column=3, padx=2, pady=2, sticky=tk.NSEW)

        break_button = ttk.Button(self, text="Give Break", command=lambda: self.__give_break())
        break_button.grid(row=5, column=1, padx=2, pady=2, sticky=tk.NSEW)

        return_button = ttk.Button(self, text="End Break", command=lambda: self.__end_break())
        return_button.grid(row=5, column=2, padx=2, pady=2, sticky=tk.NSEW)

        report_button = ttk.Button(self, text="Report Day", command=self.day.report_work_day)
        report_button.grid(row=6, column=0, columnspan=2, padx=2, pady=2, sticky=tk.NSEW)

        day_stats_button = ttk.Button(self, text="Day Stats", command=self.display_day_stats)
        day_stats_button.grid(row=6, column=2, columnspan=2, padx=2, pady=2, sticky=tk.NSEW)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
    
    def show_time(self):
        time_string = strftime('%H:%M:%S') # time format 
        self.time_label.config(text=time_string)
        self.time_label.after(1000,app.show_time) # time delay of 1000 milliseconds 


    def __start_work_day(self):
        """Start the work day."""
        self.day.start_work_day()
        self.display_work_status()


    def __give_break(self):
        """Give a break."""
        self.day.give_break()
        self.display_work_status()


    def __end_break(self):
        """End the break."""
        self.day.return_from_break()
        self.display_work_status()
    

    def __end_work_day(self):
        """End the work day."""
        self.day.end_work_day()
        self.display_work_status()


    # Display work status e.g: Working! or On Break!
    def display_work_status(self):
        """Display the current work status."""
        self.update()
        self.work_status_label.configure(text=f"{self.day.work_status}")
        self.work_status_label.grid()
        self.update()

    
    def display_day_stats(self):
        """Open day stats window and display stats for the work day."""
        window = tk.Toplevel(self)
        window.title("Day Stats")
        window.geometry("%dx%d" % (self.winfo_screenwidth() * 4//5, self.winfo_screenheight() * 4//5))
        window.update()
        home = day_stats.DayStats(window)
        home.pack(expand=True)
        home.grab_set()
        


    def __close(self):
        """Close window event"""
        if messagebox.askyesno("Quit", "Do you want to close the program?"):
            self.destroy()

if __name__ == "__main__":
    app = TimeTracker()
    app.show_time()
    app.mainloop()