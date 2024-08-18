import os

def merge_txt_files(folder_path, output_folder, max_lines_per_file):
    file_count = 1
    lines_count = 0
    output_file = os.path.join(output_folder, f'output_{file_count}.txt')
    
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith('.txt'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as infile:
                        for line in infile:
                            outfile.write(line)
                            lines_count += 1
                            if lines_count >= max_lines_per_file:
                                file_count += 1
                                lines_count = 0
                                output_file = os.path.join(output_folder, f'output_{file_count}.txt')
                                outfile.close()
                                outfile = open(output_file, 'w')

def main():
    # Input prompts
    folder_path = input('Enter the path to the folder containing .txt files (Masukkan path folder yang berisi file .txt): ')
    output_folder = input('Enter the name of the folder to save the merged files (Masukkan nama folder untuk menyimpan file hasil): ')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    max_lines_per_file = int(input('Enter the maximum number of lines per file (Masukkan jumlah maksimal baris per file): '))
    
    # Call the function to merge files
    merge_txt_files(folder_path, output_folder, max_lines_per_file)
    
    # Output message
    print(f'Merged files are saved in: {output_folder} (File hasil penggabungan tersimpan di: {output_folder})')

if __name__ == '__main__':
    main()
