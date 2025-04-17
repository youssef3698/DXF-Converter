# Standard Library Imports
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import configparser
import time
from pathlib import Path

# Local Application Imports
from business_logic import ConverterOperations

class Converter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DXF Converter")

        # Initialize configuration
        self.config_path = Path(__file__).parents[1] / "config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

        # Debugging
        print(f"Config variables: {self.config}")
        print(f"Ouput variables: {self.config["OUTPUT"]}")
        print(f"default_extension: {self.config["OUTPUT"]["default_extension"]}")

        # Load configuration
        self.default_extension = self.config["OUTPUT"]["default_extension"]

        # Add copyright notice at the bottom
        copyright_label = tk.Label(
            self.root,
            text="© 2025 Youssef Boueri. All rights reserved.",
            font=("Arial", 8),
        )
        copyright_label.pack(side=tk.BOTTOM, pady=5)

        # Create a frame for the file selection
        file_frame = tk.Frame(self.root)
        file_frame.pack(pady=10)

        # Add a label for the file path
        file_label = tk.Label(file_frame, text="Select DXF File:")
        file_label.pack(side=tk.LEFT, padx=5)

        # Add a text box to display the selected file path
        self.file_path = tk.StringVar()
        file_entry = tk.Entry(file_frame, textvariable=self.file_path, width=50)
        file_entry.pack(side=tk.LEFT, padx=5)

        # Add a browse button to select the file
        browse_button = tk.Button(file_frame, text="Browse", command=self.browse_file)
        browse_button.pack(side=tk.LEFT, padx=5)

        # Create a frame for the conversion options
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=10)

        # Add a label for the conversion options
        options_label = tk.Label(options_frame, text="Convert to:")
        options_label.pack(side=tk.LEFT, padx=5)

        # Add radio buttons for TXT and CSV options
        self.convert_option = tk.StringVar(value=self.default_extension)
        txt_radio = tk.Radiobutton(
            options_frame, text="TXT", variable=self.convert_option, value="txt"
        )
        txt_radio.pack(side=tk.LEFT, padx=5)
        csv_radio = tk.Radiobutton(
            options_frame, text="CSV", variable=self.convert_option, value="csv"
        )
        csv_radio.pack(side=tk.LEFT, padx=5)

        # Create a frame for the save file location
        save_frame = tk.Frame(self.root)
        save_frame.pack(pady=10)

        # Add a label for the save file path
        save_label = tk.Label(save_frame, text="Save As:")
        save_label.pack(side=tk.LEFT, padx=5)

        # Add a text box to display the save file path
        self.save_path = tk.StringVar()

        def update_save_path(*args):
            if self.file_path.get():
                # Get the directory and filename from the input path
                input_path = self.file_path.get()
                ext = ".txt" if self.convert_option.get() == "txt" else ".csv"
                # Set new file name:
                filename = Path(input_path).stem + ext
                # Set output directory (relative to input file):
                output_dir = Path(input_path).parents[1] / "output"
                # Create the output directory if it doesn't exist
                output_dir.mkdir(exist_ok=True)
                # Set the save path to the new file name in the output directory
                self.save_path.set(str(output_dir / filename))


        # Track changes to file_path and convert_option
        self.file_path.trace_add("write", update_save_path)
        self.convert_option.trace_add("write", update_save_path)

        save_entry = tk.Entry(save_frame, textvariable=self.save_path, width=50)
        save_entry.pack(side=tk.LEFT, padx=5)

        # Add a browse button to select the save file location
        save_browse_button = tk.Button(
            save_frame, text="Browse", command=self.browse_save_location
        )
        save_browse_button.pack(side=tk.LEFT, padx=5)

        # Add a convert button to start the conversion process
        convert_button = tk.Button(self.root, text="Convert", command=self.convert_file)
        convert_button.pack(pady=10)


    def auto_close(self):
        """Auto close the application after 2 seconds"""
        self.root.after(2000, self.root.destroy)

    def convert_file(self):
        if not self.file_path.get():
            messagebox.showerror("Error", "Please select a DXF file to convert.")
            return

        if not self.save_path.get():
            messagebox.showerror("Error", "Please select a save location.")
            return

        try:
            operations = ConverterOperations(
                self.file_path.get(),
                self.save_path.get(),
                self.convert_option.get()
            )

            skipped_entities = operations.convert_file()
            if skipped_entities != []:
                messagebox.askokcancel(
                    "Skipped Entities", f"Skipped entities: {skipped_entities}"
                )
            messagebox.showinfo(
                "Success",
                "File converted successfully!\nApplication will close in 2 seconds.",
            )
            self.auto_close()  # Add auto-close after success
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred: {e}",
                detail="Please try again or contact support.",
            )

    def browse_save_location(self):
        save_path = filedialog.asksaveasfilename(
            defaultextension=self.convert_option.get(),
            filetypes=[
                ("TXT files", "*.txt"),
                ("CSV files", "*.csv"),
                # ("All files", "*.*"),
            ],
        )
        if save_path:
            self.save_path.set(save_path)

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("DXF files", "*.dxf"),
                # ("All files", "*.*"),
            ]
        )
        if file_path:
            self.file_path.set(file_path)


if __name__ == "__main__":
    start_time = time.time()
    converter = Converter()
    converter.root.mainloop()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")
