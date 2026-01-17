import tkinter as tk
from math import radians, sin, cos, asin, degrees

window = tk.Tk()
window.geometry("800x500")
window.title('Aviate')
window.configure(bg='grey')


class WCA:
    def __init__(self):
        # Title
        tk.Label(window, text="Wind Correction Angle Calculator",
                 font=("Arial", 20), bg="grey").pack(pady=20)

        # --- True Course ---
        tk.Label(window, text="True Course (°)", font=("Arial", 16), bg="grey").pack()
        self.course_entry = tk.Entry(window, font=("Arial", 16))
        self.course_entry.pack(pady=5)

        # --- Wind Direction ---
        tk.Label(window, text="Wind Direction (°)", font=("Arial", 16), bg="grey").pack()
        self.wind_dir_entry = tk.Entry(window, font=("Arial", 16))
        self.wind_dir_entry.pack(pady=5)

        # --- Wind Speed ---
        tk.Label(window, text="Wind Speed (kts)", font=("Arial", 16), bg="grey").pack()
        self.wind_speed_entry = tk.Entry(window, font=("Arial", 16))
        self.wind_speed_entry.pack(pady=5)

        # --- True Airspeed ---
        tk.Label(window, text="True Airspeed (kts)", font=("Arial", 16), bg="grey").pack()
        self.tas_entry = tk.Entry(window, font=("Arial", 16))
        self.tas_entry.pack(pady=5)

        # --- Calculate Button ---
        tk.Button(window, text="Calculate WCA", font=("Arial", 18),
                  command=self.calculate).pack(pady=20)

        # --- Output ---
        self.output = tk.Label(window, text="", font=("Arial", 18), bg="grey")
        self.output.pack(pady=10)

    def calculate(self):
        # Get values
        tc = float(self.course_entry.get())
        wd = float(self.wind_dir_entry.get())
        ws = float(self.wind_speed_entry.get())
        tas = float(self.tas_entry.get())

        # Convert to radians
        wind_angle = radians(wd - tc)

        # WCA formula
        wca = degrees(asin((ws / tas) * sin(wind_angle)))

        # Groundspeed formula
        gs = tas * cos(radians(wca)) + ws * cos(wind_angle)

        # Display result
        self.output.config(
            text=f"WCA: {wca:.1f}°   |   Groundspeed: {gs:.1f} kts"
        )


WCA()
window.mainloop()
