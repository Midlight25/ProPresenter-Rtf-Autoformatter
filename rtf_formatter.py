import os
import sys


def auto_format_rtf(file_path):
    # Takes in complete filepath as input and replaces all
    # line breaks with paragraph breaks and writes to
    # file with filename + "MODIFIED"
    # returns the new file path

    # Gets file name and extension for creation of new file name and path
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))

    # Verifies that file exists and is .rtf before starting
    if os.path.exists(file_path) and file_ext == ".rtf":
        #print("Checks passed, beginning process.")
        #print("Modifiying {file_name}{file_ext}.".format(file_name=file_name, file_ext=file_ext))

        # Finds file directory from file path and changes to it.
        file_location = os.path.dirname(file_path)
        os.chdir(file_location)
        #print("Active directory changed to {file_location}.".format(file_location=file_location))

        # Opens file and copies data to text_data.
        with open(file_path) as file:
            text_data = file.readlines()
        #print("Opened file and read data to text_data.")

        # Formats data and adds it to list for appending.
        new_file_lines = []
        for line in text_data:
            new_file_lines.append(line.replace("\line", "\par"))
        #print("Formatted data and appended to new_file_lines")

        # Creates new file name and path from original file data.
        new_file_name = file_name + " MODIFIED" + file_ext
        new_file = os.path.join(file_location, new_file_name)
        #print("Created new file name, new file at {new_file}".format(new_file=new_file))

        # Writes data to new file
        with open(new_file, "w+") as file:
            for line in new_file_lines:
                file.write(line)
        print("Wrote data to \"{new_file_name}\".".format(new_file_name=new_file_name))
    return new_file


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if os.path.exists(arg):
                sys.stdout.write("Modifiying file {filename}.\n".format(filename=arg))
                new_file_path = auto_format_rtf(arg)
                if os.path.exists(new_file_path):
                    sys.stdout.write("New file created @ {file_path}.\n".format(
                        file_path=new_file_path))
            else:
                sys.stdout.write(
                    "{file_path} does not exist, file not created.".format(file_path=arg))
