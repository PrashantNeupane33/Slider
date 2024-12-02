import slider_gui

# Open the GUI (adjust slider values here)
slider_gui.create_window()

while(1):
    s1=slider_gui.slider1_value.get()
    s2=slider_gui.slider2_value.get()
    s3 = slider_gui.slider3_value.get()

    print(s1)
    print(s2)
    print(s3)
