#!/bin/bash

# Define the directories
folder_a="./path/to/folder/containing/Angelica_archangelica_onekp"
folder_b="./path/to/folder/containing/all/other/files4"
output_folder="./path/to/output_folder"

# Create the output folder if it does not exist
mkdir -p "$output_folder"

# Loop through all _intronerated.fasta files in folder_a
for file_a in "$folder_a"/*_intronerated_consensus.fasta; do
    # Get the base filename (e.g., 4471_intronerated_consensus.fasta)
    base_filename=$(basename "$file_a")
    
    # Define the corresponding file in folder_b
    file_b="$folder_b/$base_filename"
    
    # Check if the corresponding file exists in folder_b
    if [[ -f "$file_b" ]]; then
        # Concatenate the files and write to the output folder
        cat "$file_a" "$file_b" > "$output_folder/$base_filename"
        echo "Concatenated $base_filename from folder_a and folder_b into $output_folder/$base_filename"
    else
        echo "File $file_b does not exist, skipping..."
    fi
done

