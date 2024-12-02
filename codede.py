import tkinter as tk

class SliderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Sliders")

        # Create IntVar variables to store slider values
        self.slider1_value = tk.IntVar()
        self.slider2_value = tk.IntVar()
        self.slider3_value = tk.IntVar()

        # Create sliders
        tk.Label(root, text="Slider 1").pack(pady=5)
        self.slider1 = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=self.slider1_value)
        self.slider1.pack(pady=5)

        tk.Label(root, text="Slider 2").pack(pady=5)
        self.slider2 = tk.Scale(root, from_=0, to=200, orient="horizontal", variable=self.slider2_value)
        self.slider2.pack(pady=5)

        tk.Label(root, text="Slider 3").pack(pady=5)
        self.slider3 = tk.Scale(root, from_=0, to=300, orient="horizontal", variable=self.slider3_value)
        self.slider3.pack(pady=5)

        # Button to display slider values
        tk.Button(root, text="Show Values", command=self.display_values).pack(pady=10)

    def need_values(self):
        return (self.slider1_value.get(), self.slider2_value.get(), self.slider3_value.get())

    def display_values(self):
        values = self.need_values()
        print(f"Slider 1 Value: {values[0]}")
        print(f"Slider 2 Value: {values[1]}")
        print(f"Slider 3 Value: {values[2]}")
