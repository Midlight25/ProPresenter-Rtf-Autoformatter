import os
# import sys
import argparse
# from tkinter import filedialog as fdialog
import tkinter as tk


def auto_format_rtf(file_path, debug=False):
    r""" Input complete filepath to .rtf file
        replaces all instances of "\line" to "\par".
        writes new data to new file with "MODFIED" appended.
        Prints debug messages to console if debug=True.
    """
    # Separates file name and extension for processing later.
    file_name, file_ext = os.path.splitext(
        os.path.basename(file_path))

    # Verifies that file exists and is .rtf before starting
    if os.path.exists(file_path) and file_ext == ".rtf":
        if debug:
            print("File Operation Confirmed")
            print(f"\tModifiying \"{file_name}.{file_ext}\".")

        # Opens file and copies data to text_data object.
        with open(file_path, "r") as file:
            text_data = file.read()
        if debug:
            print("\tSuccessfully read data")

        # Replaces the unwanted "\\line" with "\\par"
        # Operation performed on the entire data set instead of line
        # by line.
        new_text_data = text_data.replace(r"\line", r"\par")
        if debug:
            print("\tData format operation successful")

        # Gets location of file
        file_location = os.path.dirname(file_path)

        # Creates new file name from original name.
        new_file_name = file_name + " MODIFIED" + file_ext

        # Creates new complete file path from new name and original
        # path.
        new_file = os.path.join(file_location, new_file_name)

        # Creates new file @ new path and writes data to new file.
        with open(new_file, "w+") as file:
            file.write(new_text_data)
            if debug:
                print(f"\tCreated new file at \"{new_file}\".")
                print(f"\tWrote data to \"{new_file_name}\".\n")

    return new_file


class font:
    def __init__(self, font_name):
        self.med = (str(font_name), 12)
        self.large = (str(font_name), 14)


class prog_GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ProPresenter Auto Formatter")
        frame_width = 475
        helv = font("Helvetica")

        # Variables

        self.preview_var = tk.StringVar()
        self.preview_var.set("No File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File SelectedNo File Selected")

        # Frames
        self.title_frame = tk.Frame(
            self.master, bg="pink", width=frame_width, height=30, )
        self.title_frame.place(relx=0.5, rely=0.05, anchor="center")

        self.selection_frame = tk.Frame(
            self.master, bg="red", width=frame_width, height=50)
        self.selection_frame.place(
            relx=0.5, rely=0.15, anchor="center")

        self.preview_frame = tk.Frame(
            self.master, bg="blue", width=frame_width, height=290)
        self.preview_frame.place(relx=0.5, rely=0.54, anchor="center")

        self.sub_preview_frame = tk.Frame(
            self.preview_frame, bg="green")
        self.sub_preview_frame.place(
            relx=0, rely=0.25, relwidth=1, relheight=0.75)

        self.confirm_frame = tk.Frame(
            self.master, bg="green", width=frame_width, height=50)
        self.confirm_frame.place(relx=0.5, rely=0.93, anchor="center")

        # Labels
        self.title_label = tk.Label(
            self.title_frame,
            text="ProPresenter Auto Formatter",
            anchor="center",
            font=helv.large,
            width=50,)
        self.title_label.pack()

        self.preview_label = tk.Label(
            self.preview_frame,
            text="File Preview:",
            font=helv.large,
            anchor="w",
            justify="left")
        self.preview_label.place(relx=0.15, rely=0.1, anchor="center")

        self.preview_window = tk.Label(
            self.sub_preview_frame, textvariable=self.preview_var)
        self.preview_window.configure(
            anchor="nw",
            justify="left",
            font=helv.large,
            wraplength=425)
        self.preview_window.pack(fill="both")


if __name__ == '__main__':

    # Initializes parser for commandline call and sets flags.
    parser = argparse.ArgumentParser(
        description="Formats .rtf files for use "
        "with ProPresenter6 import function. "
        "Or optionally, you can run without "
        "arguments and you will be brought to an "
        "interactive commandline interface.")

    parser.add_argument(
        "-c",
        "--confirm",
        action="store_true",
        help="Skips having to confirm processing on every "
        "file")
    parser.add_argument("-f", "--files", nargs="*",
                        help="Full file paths of all files "
                        "that you want to process")

    args = parser.parse_args()

    # If script is called from the commandline and supplied arguments.
    # Iterates through arguments, applying processing as it goes.
    if args.files is not None:
        for file in args.files:

            # Checks to see if the file exists.
            if os.path.exists(file):
                print(f"Modifiying file \"{file}\".")
                # If the "confirm all" flag is not raised, will ask for user
                # confirmation for each file before processing is
                # applied.
                if not args.confirm:

                    # Starts decision loop
                    # User must give valid answer for loop to exit.
                    confirmation = None
                    while confirmation is None:
                        print(
                            "\nAre you sure you would like to modify "
                            f"\"{file}\"? Please confirm. \n(y/n)?")
                        selection = input(">")

                        if selection == "n":
                            print(
                                f"\nUser canceled processing on \"{file}\"."
                                "\n")
                            confirmation = False

                        elif selection == "y":
                            print(
                                f"\nRecieved go-ahead for \"{file}\".")
                            confirmation = True

                        else:
                            print(
                                "\nInvalid Selection, please try again. \n")

                    # If user selects no for this file,
                    # the program will continue on to the next file.
                    if not confirmation:
                        continue

                # Performs formatting on file with debugging enabled.
                new_file_path = auto_format_rtf(file, debug=True)

                # Checks if file was really created.
                if os.path.exists(new_file_path):
                    print(
                        f"New file created @ \"{new_file_path}\".\n")
                else:
                    print("Error creating new file.\n")

            # If file was not valid for program.
            else:
                print(f"\"{file}\" does not exist.")

        # End of program.
        print("Instance terminated without any issues.")

    # Starts the interactive CLI when script
    # is called from the commandline with no arguments
    else:
        root = tk.Tk()
        root.geometry("500x450")
        root.resizable(0, 0)
        gui = prog_GUI(root)
        root.mainloop()
"""
                # Opens Documents Directory on Windows
                if sys.platform.startswith('win32'):
                    default_directory = os.path.join(
                        os.getenv('USERPROFILE'), "Documents")
                    current_selected_file = fdialog.askopenfilename(
                        initialdir=default_directory,
                        title="Select file",
                        filetypes=[("Rich Text Format files", "*.rtf")])

                # Opens Desktop Directory on Mac OS X
                elif sys.platform.startswith('darwin'):
                    default_directory = os.path.join(
                        os.getenv("HOME"), "Desktop")
                    current_selected_file = fdialog.askopenfilename(
                        initialdir=default_directory,
                        title="Select file",
                        filetypes=[("Rich Text Format files", "*.rtf")])
"""
