import os
import sys
import argparse
from tkinter import filedialog as fdialog
from tkinter import Tk


def auto_format_rtf(file_path, debug=False):
    """ Input complete filepath to .rtf file
        replaces all instances of "\\line" to "\\par".
        writes new data to new file with "MODFIED" appended.
        Prints debug messages to console if debug=True.
    """
    # Separates file name and extension for processing later.
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))

    # Verifies that file exists and is .rtf before starting
    if os.path.exists(file_path) and file_ext == ".rtf":
        if debug:
            print("\nFile Operation Confirmed".format(
                file_path=file_path))
            print("    Modifiying \"{filename}\".".format(
                filename=os.path.basename(file_path)))

        # Opens file and copies data to text_data object.
        with open(file_path, "r") as file:
            text_data = file.read()
        if debug:
            print("    Successfully read data")

        # Replaces the unwanted "\\line" with "\\par"
        # Operation performed on the entire data set instead of line by line.
        new_text_data = text_data.replace("\\line", "\\par")
        if debug:
            print("    Data format operation successful")

        # Gets location of file
        file_location = os.path.dirname(file_path)

        # Creates new file name from original name.
        new_file_name = file_name + " MODIFIED" + file_ext

        # Creates new complete file path from new name and original path.
        new_file = os.path.join(file_location, new_file_name)

        # Creates new file @ new path and writes data to new file.
        with open(new_file, "w+") as file:
            file.write(new_text_data)
            if debug:
                print("    Created new file at \"{new_file}\"."
                      .format(new_file=new_file))
                print("    Wrote data to \"{new_file_name}\".\n"
                      .format(new_file_name=new_file_name))

    return new_file


if __name__ == '__main__':

    # Initializes parser for commandline call and sets flags.
    parser = argparse.ArgumentParser(description="Formats .rtf files for use "
                                     "with ProPresenter6 import function. "
                                     "Or optionally, you can run without "
                                     "arguments and you will be brought to an "
                                     "interactive commandline interface.")

    parser.add_argument("-c", "--confirm", action="store_true",
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
                print("Modifiying file \"{filename}\"."
                      .format(filename=file))
                # If the "confirm all" flag is not raised, will ask for user
                # confirmation for each file before processing is applied.
                if not args.confirm:

                    # Starts decision loop
                    # User must give valid answer for loop to exit.
                    confirmation = None
                    while confirmation is None:
                        print("\nAre you sure you would like to modify "
                              "\"{filename}\"? Please confirm. \n"
                              "(y/n)?".format(filename=file))
                        selection = input(">")

                        if selection == "n":
                            print("\nUser canceled processing on "
                                  "\"{filename}\".\n"
                                  .format(filename=file))
                            confirmation = False

                        elif selection == "y":
                            print("\nRecieved go-ahead for \"{filename}\"."
                                  .format(filename=file))
                            confirmation = True

                        else:
                            print("\nInvalid Selection, please try again. \n")

                    # If user selects no for this file,
                    # the program will continue on to the next file.
                    if not confirmation:
                        continue

                # Performs formatting on file with debugging enabled.
                new_file_path = auto_format_rtf(file, debug=True)

                # Checks if file was really created.
                if os.path.exists(new_file_path):
                    print("New file created @ \"{file_path}\".\n"
                          .format(file_path=new_file_path))
                else:
                    print("Error creating new file.\n")

            # If file was not valid for program.
            else:
                print("\"{file_path}\" does not exist."
                      .format(file_path=file))

        # End of program.
        print("Instance terminated without any issues.")

    # Starts the interactive CLI when script
    # is called from the commandline with no arguments
    else:
        print("\nProPresenter RTF Autoformatter ©Midlight25 2019\n")

        # Defining choices for use in CLI.
        acceptable_exit_answers = ["quit", "q"]
        acceptable_input_answers = ["input", "i"]
        acceptable_cancel_answers = ["cancel", "c"]
        currently_running = True

        # Starts program loop with currently_running.
        while currently_running:
            print("Type (I)nput to select a file "
                  "or (Q)uit to exit the program:")
            selection = input(">")

            # Exit program if quit is passed to the CLI
            if selection.lower() in acceptable_exit_answers:
                sys.exit("Program exited by user")

            # Starts file input dialog
            elif selection.lower() in acceptable_input_answers:

                # Removes an extra window that appears
                # when the file dialog activates
                root = Tk()
                root.withdraw()

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

                # Any Unrecognized OS - Need to add Linux support
                else:
                    current_selected_file = fdialog.askopenfilename(
                        initialdir="/",
                        title="Select file",
                        filetypes=[("Rich Text Format files", "*.rtf")])

                # When user cancels file selection, tk returns empty string.
                if current_selected_file == "":
                    print("User canceled file operation, "
                          "returning to main menu.\n")
                    continue

                # Initiates confirmation session
                confirm = None
                while confirm is None:
                    print("\nYou selected \"{file}\" for formating, "
                          "is this (OK)? Or type (C)ancel to cancel."
                          .format(file=os.path.basename
                                  (current_selected_file)))
                    user_warning = input(">")

                    if user_warning.lower() == "ok":
                        try:
                            auto_format_rtf(current_selected_file, debug=True)

                        except:
                            print("\nProgram was unable to create new file,"
                                  " please try again.\n")
                        confirm = True

                    elif user_warning.lower() in acceptable_cancel_answers:
                        print("\nUser canceled operation.")
                        confirm = False

                    else:
                        print("\nInvalid Input, please try again.")

            else:
                print("Invalid Input,  please try again\n")

        sys.exit("\nSystem crashed.")
