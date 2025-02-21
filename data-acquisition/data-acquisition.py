import customtkinter as Ctk
import tkinterDnD
from ximea import xiapi
import cv2
import time

# GUI Setup
window_height=480
window_width=620
Ctk.set_ctk_parent_class(tkinterDnD.Tk)

Ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
Ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = Ctk.CTk()
app.geometry(f"{window_width}x{window_height}")
app.title("APP")

print(type(app), isinstance(app, tkinterDnD.Tk))

# Create instance for first connected camera 
cam = xiapi.Camera()

# Set variables
timer = Ctk.BooleanVar()
fps = Ctk.BooleanVar()

def zoom_point(img, zoom=1, coord=None):
    h, w = img.shape[:2]
    if coord is None:
        cx, cy = int(w/2), int(h/2)
    else:
        cx, cy = coord
    
    crop_size = int(min(h, w) / zoom)
    half_crop = crop_size // 2
    
    roi = img[max(0, cy-half_crop):min(h, cy+half_crop), 
              max(0, cx-half_crop):min(w, cx+half_crop)]
    
    zoomed = cv2.resize(roi, (w, h), interpolation=cv2.INTER_LINEAR)
    return zoomed

def miniscope_event():
    # Start communication
    print('Opening first camera...')
    cam.open_device()

    # Camera Settings
    # Set downsampling rate based on option
    global value
    value = ds_button_var.get()
    if value == 1:
        ds_value = 'XI_DWN_1x1'
    elif value == 2:
        ds_value = 'XI_DWN_2x2'
    elif value == 3:
        ds_value = 'XI_DWN_4x4'
    elif value == 4:
        ds_value = 'XI_DWN_8x8'
        
    cam.set_downsampling(ds_value)

    # Set exposure based on option
    exposure_value = expose_entry.get()
    if not exposure_value:
        exposure_value = 80000
    else:
        exposure_value = int(exposure_value)

    cam.set_exposure(exposure_value)

    # Define camera width and height
    width = cam.get_width()
    height = cam.get_height()
    
    # Create instance of Image to store image data and metadata
    global  img
    img = xiapi.Image()

    # Check recording name
    global  recording_name
    recording_name = rec_name_entry.get()
    if not recording_name:
        recording_name = 'recording'  # Use a default name if the entry is empty

    # Define Videowriter
    # output = cv2.VideoWriter(f'{recording_name}.mp4v', cv2.VideoWriter_fourcc('P', 'I', 'M', '1'), 4.6, (width, height))
    # output = cv2.VideoWriter(f'{recording_name}.avi', cv2.VideoWriter_fourcc(*'XVID'), 4.6, (width, height))
    output = cv2.VideoWriter(f'{recording_name}.avi', cv2.VideoWriter_fourcc(*'MJPG'), 4.6, (width, height))
    print('Starting data acquisition...')
    
    cam.start_acquisition()
    print('Starting video. Press CTRL+C to exit.')
    t0 = time.time()

    global endscope
    endscope = False

    def check_endscope():
        if endscope:
            # Stop data acquisition
            print('Stopping acquisition...')
            cam.stop_acquisition()

            cam.close_device()

            print('Done.')
            cv2.destroyAllWindows()

            # Close app window
            app.quit() 
        else:
            # Continue data acquisition
            cam.get_image(img)
            data = img.get_image_data_numpy()
            
            # Convert frames to BGR format
            data = cv2.cvtColor(data, cv2.COLOR_GRAY2BGR)

            # Apply zoom
            zoom_factor = z_button_var.get() - 4  # Convert button values to zoom factors
            if zoom_factor > 1:
                data = zoom_point(data, zoom=zoom_factor)

            # Get FPS
            fps_counter = cam.get_framerate()

            # Show acquired image with time since the beginning of acquisition
            font = cv2.FONT_HERSHEY_SIMPLEX
            timer_text = '{:5.2f}'.format(time.time()-t0)
            fps_text = '{:5.2f}'.format(fps_counter)
            
            if timer.get():
                cv2.putText(
                    data, timer_text, (width-378, 100), font, 4, (255, 255, 255), 2
                )

            if fps.get():
                cv2.putText(
                    data, fps_text, (width-378, 240), font, 4, (255, 255, 255), 2
                )

            # Resize live recording
            cv2.namedWindow("XiCAM live", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("XiCAM live", 1296, 972)
                
            # Displaying live recording
            cv2.imshow('XiCAM live', data)

            # Record the frames
            output.write(data)

            cv2.waitKey(1)

            # Schedule the next check
            app.after(100, check_endscope)  # Check every 100 ms

    # Start checking
    check_endscope()

# Stop Miniscope button
def endscope_event():
    global endscope
    endscope = True

# Take Photo button
def take_photo_event():
    # Capture and save the current frame
    cam.get_image(img)
    photo_data = img.get_image_data_numpy()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    cv2.imwrite(f'{recording_name}_{timestamp}.png', photo_data)
    print(f"Photo saved as {recording_name}_{timestamp}.png")

frame_1 = Ctk.CTkFrame(master=app)
frame_1.grid(row=0,column=0, columnspan=6, ipady=20, ipadx=60)

# Placeholder space 1
empty_label_1 = Ctk.CTkLabel(master=frame_1, text="  ", justify=Ctk.LEFT)
empty_label_1.grid(row=1,column=0,pady=0, padx=10)

# Recording name
rec_name_entry = Ctk.CTkEntry(master=frame_1, placeholder_text="Recording Name")
rec_name_entry.grid(row=2,pady=8)

# Expsosure
expose_entry = Ctk.CTkEntry(master=frame_1, placeholder_text="Exposure")
expose_entry.grid(row=3,column=0,pady=8)


# Downsampling
label_2 = Ctk.CTkLabel(master=frame_1, text="Downsampling Options", font=("Inter", 14), justify=Ctk.LEFT)
label_2.grid(row=5,column=0, pady=14)

ds_button_var = Ctk.IntVar(value=1)

ds_button_1 = Ctk.CTkRadioButton(master=frame_1, text="None", variable=ds_button_var, value=1)
ds_button_1.grid(row=6,column=0)

ds_button_2 = Ctk.CTkRadioButton(master=frame_1, text="1/2", variable=ds_button_var, value=2)
ds_button_2.grid(row=6,column=1)

ds_button_3 = Ctk.CTkRadioButton(master=frame_1, text="1/4", variable=ds_button_var, value=3)
ds_button_3.grid(row=6,column=2)

ds_button_4 = Ctk.CTkRadioButton(master=frame_1, text="1/8", variable=ds_button_var, value=4)
ds_button_4.grid(row=6,column=3,pady=10)

# Zoom
label_3 = Ctk.CTkLabel(master=frame_1, text="Zoom Options", font=("Inter", 14), justify=Ctk.LEFT)
label_3.grid(row=7,column=0, pady=1)

z_button_var = Ctk.IntVar(value=5)

z_button_1 = Ctk.CTkRadioButton(master=frame_1, text="None", variable=z_button_var, value=5)
z_button_1.grid(row=8,column=0)

z_button_2 = Ctk.CTkRadioButton(master=frame_1, text="2x", variable=z_button_var, value=6)
z_button_2.grid(row=8,column=1)

z_button_3 = Ctk.CTkRadioButton(master=frame_1, text="3x", variable=z_button_var, value=7)
z_button_3.grid(row=8,column=2)

z_button_4 = Ctk.CTkRadioButton(master=frame_1, text="7x", variable=z_button_var, value=8)
z_button_4.grid(row=8,column=3)

z_button_5 = Ctk.CTkRadioButton(master=frame_1, text='10x', variable=z_button_var, value=10)
z_button_5.grid(row=8,column=4, pady=10)

# Timer
timer_checkbox = Ctk.CTkCheckBox(master=frame_1, text="Show Timer", variable=timer, onvalue="True", offvalue="False")
timer_checkbox.grid(row=10,column=0,pady=15)

# Show FPS
fps_checkbox = Ctk.CTkCheckBox(master=frame_1, text="Show FPS", variable=fps, onvalue="True", offvalue="False")
fps_checkbox.grid(row=11,column=0,pady=10)

# Placeholder space 4
empty_label_5 = Ctk.CTkLabel(master=frame_1, text="  ", justify=Ctk.LEFT)
empty_label_5.grid(row=12,column=0,pady=0, padx=10)

# Start Miniscope
button_1 = Ctk.CTkButton(master=frame_1, text="Start", command=miniscope_event)
button_1.grid(row=13,column=0,pady=10, padx=10)

# Stop Miniscope
button_2 = Ctk.CTkButton(master=frame_1, text="Stop", command=endscope_event)
button_2.grid(row=13,column=3,pady=10, padx=10)

# Take Photo
button_3 = Ctk.CTkButton(master=frame_1, text="Take Photo", command=take_photo_event)
button_3.grid(row=2,column=3,pady=5, padx=5)

app.mainloop()