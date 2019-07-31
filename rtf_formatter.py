import os


def auto_format_rtf(file_path):
    # Takes in complete filepath as input and replaces all
    # line breaks with paragraph breaks and writes to
    # file with filename + "MODIFIED"
    # returns None

    file_location = os.path.dirname(file_path)
    os.chdir(file_location)

    if os.path.exists(file_path):
        with open(file_path) as file:
            text_data = file.readlines()

        new_file_lines = []
        for line in text_data:
            new_file_lines.append(line.replace("\line", "\par"))

        file_name, file_ext = os.path.splitext(file_path)

        new_file_name = file_name + " MODIFIED" + file_ext

        new_file = os.path.join(file_location, new_file_name)

        with open(new_file, "w+") as file:
            for line in new_file_lines:
                file.write(line)

    return None
