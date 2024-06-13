import os

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def split_file_into_folders(input_file):
    folder_name = os.path.splitext(os.path.basename(input_file))[0] + '_folder'
    create_folder_if_not_exists(folder_name)

    with open(input_file, 'r') as file:
        content = file.read()
    
    entries = content.split('>')
    folder_base_name = os.path.splitext(os.path.basename(input_file))[0]
    for entry in entries:
        if entry.strip():  # Skip empty entries
            header = entry.splitlines()[0]
            entry_number = header.split()[0]
            output_file = f"{folder_name}/{entry_number}.txt"
            with open(output_file, 'w') as out_file:
                out_file.write(f">{folder_base_name}\n")
                out_file.write('\n'.join(entry.splitlines()[1:]))

def process_multiple_files(file_list):
    for file in file_list:
        split_file_into_folders(file)

# Usage
# Usage
file_list = ['file_path/*.txt']  # Add your file path(s) here
process_multiple_files(file_list)
