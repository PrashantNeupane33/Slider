import tkinter as tk
from tkinter import ttk

def create_window():
    """Create the main window with three sliders."""
    # Create the main window
    root = tk.Tk()
    root.title("Slider GUI")

    # Create a frame for sliders
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Slider 1
    ttk.Label(frame, text="Slider 1").grid(row=0, column=0, pady=5, sticky=tk.W)
    slider1 = ttk.Scale(frame, from_=0, to=100, orient='horizontal')
    slider1.grid(row=0, column=1, pady=5)

    # Slider 2
    ttk.Label(frame, text="Slider 2").grid(row=1, column=0, pady=5, sticky=tk.W)
    slider2 = ttk.Scale(frame, from_=0, to=100, orient='horizontal')
    slider2.grid(row=1, column=1, pady=5)

    # Slider 3
    ttk.Label(frame, text="Slider 3").grid(row=2, column=0, pady=5, sticky=tk.W)
    slider3 = ttk.Scale(frame, from_=0, to=100, orient='horizontal')
    slider3.grid(row=2, column=1, pady=5)

    # Button to close the window
    close_button = ttk.Button(frame, text="Close", command=root.destroy)
    close_button.grid(row=3, column=0, columnspan=2, pady=10)

    def print_values():
        """Print the slider values continuously."""
        print("Slider 1 value:", slider1.get())
        print("Slider 2 value:", slider2.get())
        print("Slider 3 value:", slider3.get())
        print("-" * 30)  # Separator for clarity
        root.after(500, print_values)  # Call this function again after 500ms

    # Start printing slider values
    print_values()

    # Start the Tkinter event loop
    root.mainloop()

# If the script is run directly, open the window
if __name__ == "__main__":
    create_window()
