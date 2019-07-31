import os

this_folder = os.path.dirname(os.path.abspath(__file__))
the_file = os.path.join(this_folder, "test.rtf")


with open(the_file) as file:
    text_data = file.readlines()

new_file_lines = []

for line in text_data:
    new_file_lines.append(line.replace("\line", "\par"))

new_file = os.path.join(this_folder, "new_test.rtf")

with open(new_file, "w") as file:
    for line in new_file_lines:
        file.write(line)
