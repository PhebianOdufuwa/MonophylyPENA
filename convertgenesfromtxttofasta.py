import os
import glob

def convert_to_fasta(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Extract the header and sequence
    header = lines[0].strip()
    sequence = ''.join(line.strip() for line in lines[1:])

    # Write to FASTA file
    with open(output_file, 'w') as fasta_file:
        fasta_file.write(f"{header}\n")
        fasta_file.write(sequence + '\n')

def process_directory(directory):
    # Find all .txt files in the directory
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    
    for file_path in txt_files:
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join(directory, f"{base_name}_intronerated_consensus.fasta")
        convert_to_fasta(file_path, output_file)

# Usage
directory = './path/to/directory'  # Specify your directory path here
process_directory(directory)
