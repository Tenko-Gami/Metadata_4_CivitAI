import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import json
from PIL.PngImagePlugin import PngInfo
import os
import get_functions as getF

def load_and_extract_data():
    global selected_image_path, extracted_data
    file_path = filedialog.askopenfilename(filetypes=[("PNG images", "*.png")])
    if not file_path:
        messagebox.showwarning("No File Selected", "No PNG image was selected.")
        return
    selected_image_path = file_path
    im = Image.open(selected_image_path)
    # try:
    #     data = json.loads(im.info["prompt"])
    #
    #     # You can integrate the data extraction functions here
    #     height, width = im.size
    #     ckpt_name = getF.model_name(data)
    #     seed, steps, cfg, sampler_name, scheduler = getF.ksampler_values(data)
    #     lora_names = getF.lora_names(data)
    #     positive_prompt, negative_prompt = getF.prompts(data)
    #
    #     # Display the extracted data
    #     result_text.delete(1.0, tk.END)
    #     result_text.insert(tk.END, f"Seed: {seed}\n\n")
    #     result_text.insert(tk.END, f"Image size: {width}x{height}\n\n")
    #     result_text.insert(tk.END, f"Steps: {steps}\n\n")
    #     result_text.insert(tk.END, f"CFG: {cfg}\n\n")
    #     result_text.insert(tk.END, f"Sampler Name: {sampler_name}\n\n")
    #     result_text.insert(tk.END, f"Scheduler: {scheduler}\n\n")
    #     result_text.insert(tk.END, f"CKPT Name: {ckpt_name}\n\n")
    #     result_text.insert(tk.END, f"LORA Names: {', '.join(lora_names)}\n\n")
    #     result_text.insert(tk.END, f"Positive Prompt: {positive_prompt}\n\n")
    #     result_text.insert(tk.END, f"Negative Prompt: {negative_prompt}\n\n")
    #
    #     # Store the extracted data in global variables for later use
    #     extracted_data = {
    #         "seed": seed,
    #         "width": width,
    #         "height": height,
    #         "ckpt_name": ckpt_name,
    #         "steps": steps,
    #         "cfg": cfg,
    #         "sampler_name": sampler_name,
    #         "scheduler": scheduler,
    #         "lora_names": lora_names,
    #         "positive_prompt": positive_prompt,
    #         "negative_prompt": negative_prompt
    #     }

    # Update the image preview
    update_image_preview(im)

    # except Exception as e:
    #     messagebox.showerror("Error", f"An error occurred: {e}")

# def select_folder():
#     global selected_folder
#     folder_path = filedialog.askdirectory()
#     if not folder_path:
#         messagebox.showwarning("No Folder Selected", "No folder was selected.")
#         return
#     selected_folder = folder_path
#     folder_label.config(text=f"Selected Folder: {selected_folder}")

def launch_program():
    # if 'extracted_data' not in globals() or not extracted_data:
    #     messagebox.showwarning("No Data Extracted", "Please extract data from an image first.")
    #     return
    # if 'selected_folder' not in globals() or not selected_folder:
    #     messagebox.showwarning("No Folder Selected", "Please select a folder first.")
    #     return


    try:
        global final_str
        metadata = PngInfo()
        im = Image.open(selected_image_path)
        data = json.loads(im.info["prompt"])
        for x, y in im.info.items():
            metadata.add_text(x, y)
            print(x, y)

        # You can integrate the data extraction functions here
        height, width = im.size
        ckpt_name = getF.model_name(data)
        seed, steps, cfg, sampler_name, scheduler = getF.ksampler_values(data)
        lora_names = getF.lora_names(data)
        positive_prompt, negative_prompt = getF.prompts(data)
        root = r"C:\Users\mathi\Documents\Comfy_ui\ComfyUI_windows_portable\ComfyUI\models/"

        lora_hashes = ""
        for lora_name in lora_names:
            hash = getF.hash(root + 'loras/' + lora_name)
            lora_hashes += f"{lora_name.split('.')[0]}: {hash}, "

        Model_hash = getF.hash(root + 'checkpoints/' + ckpt_name)

        final_str = (f"{positive_prompt}\nNegative prompt: {negative_prompt}\nSteps: {steps}, Sampler: {sampler_name}, "
                 f"Schedule type: {scheduler}, CFG scale: {cfg}, Seed: {seed}, Size: {width}x{height}, Model hash: {Model_hash},"
                 f"Model: {ckpt_name.split(".")[0]}, Lora hashes: \"{lora_hashes}\", "
                 f"Version: ComfyUi")

        print(final_str)

        metadata.add_text("parameters", final_str)

        im.save(selected_image_path.split('.')[0]+'_meta.png', pnginfo=metadata)

    # Add your program logic here
    # For example, you can call a function that processes the data and folder
    # process_data(extracted_data, selected_folder)

        messagebox.showinfo("Program Launched", "The program has been launched successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while launching the program: {e}")

def update_image_preview(image):
    # Resize the image to fit the preview area
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("Change Metadata")
root.geometry("1200x800")

# Create a frame for image preview
image_frame = ttk.Frame(root)
image_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Create a label for the image preview
image_label = ttk.Label(image_frame)
image_label.pack()

# Create a frame for folder and text widget
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Create a button to select the PNG image
select_image_button = ttk.Button(control_frame, text="Select PNG Image", command=load_and_extract_data)
select_image_button.pack(pady=10)

# Create a button to select a folder
# select_folder_button = ttk.Button(control_frame, text="Select Folder", command=select_folder)
# select_folder_button.pack(pady=10)

# Create a button to launch the program
launch_program_button = ttk.Button(control_frame, text="Launch Program", command=launch_program)
launch_program_button.pack(pady=10)

# Create a label to display the selected folder
# folder_label = ttk.Label(control_frame, text="Selected Folder: None", wraplength=400)
# folder_label.pack(pady=10)

# Create a text widget to display the results
result_text = tk.Text(control_frame)
result_text.pack(pady=20)

# Initialize global variables
extracted_data = None
selected_folder = None
selected_image_path = None
final_str = None

# Run the application
root.mainloop()