import os
import sys
from tkinter import filedialog as fdialog
from tkinter import Tk


def auto_format_rtf(file_path):
    """Takes in complete filepath as input and replaces all
        line breaks with paragraph breaks and writes to
        file with filename + "MODIFIED"
    returns the new file path
    """
    # Gets file name and extension for creation of new file name and path
    # It's here because the next if statement checks if this file is an ".rtf"
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))

    # Verifies that file exists and is .rtf before starting
    if os.path.exists(file_path) and file_ext == ".rtf":
        print("Checks passed on \"{file_path}\", beginning process.".format(file_path=file_path))
        print("Modifiying \"{file_name}{file_ext}\".".format(file_name=file_name,
                                                             file_ext=file_ext))

        # Opens file and copies data to text_data.
        with open(file_path, "r") as file:
            text_data = file.read()
        print("Opened file and read data to text_data.")

        # Formats data and adds it to list for appending.
        new_text_data = text_data.replace("\line", "\par")
        print("Formatted data")

        # Creates new file name and path from original file data.
        file_location = os.path.dirname(file_path)
        new_file_name = file_name + " MODIFIED" + file_ext
        new_file = os.path.join(file_location, new_file_name)
        print("Created new file name, new file at \"{new_file}\"".format(new_file=new_file))

        # Writes data to new file
        with open(new_file, "w+") as file:
            file.write(new_text_data)
        print("Wrote data to \"{new_file_name}\".\n".format(new_file_name=new_file_name))

    return new_file


if __name__ == '__main__':

    # If script is passed to commandline w/ arguments
    # interates through the list of arguments and applies function as it goes.
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                print("Modifiying file \"{filename}\".\n".format(filename=arg))
                new_file_path = auto_format_rtf(arg)

                if os.path.exists(new_file_path):
                    print("New file created @ \"{file_path}\".\n".format(
                        file_path=new_file_path))
                else:
                    print("Error creating new file.\n")

            else:
                print(
                    "\"{file_path}\" does not exist, file not created.".format(file_path=arg))

    # Starts the CLI Environment - will rework with Argparse library
    else:

        print("\nProPresenter RTF Autoformatter © Midlight25 2019\n")
        acceptable_exit_answers = ["quit", "q"]
        acceptable_input_answers = ["input", "i"]
        acceptable_cancel_answers = ["cancel", "c"]
        currently_running = True

        # Processing loop
        while currently_running == True:
            print("Type (I)nput to select your file or (Q)uit to exit the program:")
            selection = input("")

            if selection.lower() in acceptable_exit_answers:
                sys.exit("Program exited by user")

            elif selection.lower() in acceptable_input_answers:
                # Removes an extra window that appears when the file dialog activates
                root = Tk()
                root.withdraw()

                # Opens Documents Directory on Windows
                if sys.platform.startswith('win32'):
                    default_directory = os.path.join(os.getenv('USERPROFILE'),
                                                     "Documents")
                    current_selected_file = fdialog.askopenfilename(
                        initialdir=default_directory,
                        title="Select file",
                        filetypes=[("Rich Text Format files", "*.rtf")])

                # Opens Desktop Directory on Mac OS X
                elif sys.platform.startswith('darwin'):
                    default_directory = os.path.join(os.getenv("HOME"), "Desktop")
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
                    print("User canceled file operation, returning to main menu.\n")
                    continue

                # Initiates confirmation session
                end_session = False
                while end_session == False:
                    user_warning = input("\nYou selected \"{file}\" for formating, is this (OK)? Or type (C)ancel to cancel:\n".format(
                        file=os.path.basename(current_selected_file)))

                    if user_warning.lower() == "ok":
                        try:
                            auto_format_rtf(current_selected_file)
                            end_session = True
                        except:
                            print("Program was unable to create new file, \
                                please try again.\n")
                            end_session = True

                    elif user_warning.lower() in acceptable_cancel_answers:
                        print("User canceled operation.")
                        end_session = True

                    else:
                        print("Unable to understand user input, please try again.")

            else:
                print("Did not understand user input. Please try again\n")

        sys.exit("System crashed.")
