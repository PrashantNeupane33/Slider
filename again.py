import multiprocessing
import tkinter as tk
from codede import SliderApp
import cv2

# Function to start the Tkinter application
def run_tkinter():
    root = tk.Tk()
    app = SliderApp(root)
    def get_values():
        a, b, c = app.need_values()
        print(f"Retrieved Values: a={a}, b={b}, c={c}")

    # Add a separate button to retrieve the values programmatically
    tk.Button(root, text="Get Slider Values", command=get_values).pack(pady=10)

    root.mainloop()
    # root.mainloop()

# Function to run OpenCV operations
def run_opencv():
    # Open a blank OpenCV window
    cap = cv2.VideoCapture(0)  # Use the webcam
    if not cap.isOpened():
        print("Unable to access the camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the video feed
        cv2.imshow("OpenCV Window", frame)

        # Exit the OpenCV window on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create separate processes for Tkinter and OpenCV
    tkinter_process = multiprocessing.Process(target=run_tkinter)
    opencv_process = multiprocessing.Process(target=run_opencv)

    # Start both processes
    tkinter_process.start()
    opencv_process.start()

    # Wait for both processes to finish
    tkinter_process.join()
    opencv_process.join()
