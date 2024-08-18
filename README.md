Text File Merger and Splitter
Overview
This repository contains a Python script that automates the process of merging multiple .txt files from a specified directory into a single file, and then splits the output into multiple files based on a user-defined maximum number of lines per file.

Features
Merge .txt Files: Combines all .txt files from a specified folder into one cohesive output.
Split Output: The combined output is split into multiple files, each containing a maximum number of lines as specified by the user.
Automatic Folder Creation: If the specified output folder doesn't exist, the script will automatically create it.
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/repo-name.git
cd repo-name
Run the Script:

Ensure you have Python installed.
Execute the script:
bash
Copy code
python merge_txt_files.py
You will be prompted to:
Enter the path to the folder containing the .txt files.
Specify the output folder where the merged files will be saved.
Set the maximum number of lines per output file.
Example:

If your input folder contains several .txt files and you set a limit of 1000 lines per output file, the script will generate multiple files (output_1.txt, output_2.txt, etc.) in the specified output folder.
Requirements
Python 3.x
Access to the folder containing .txt files you wish to merge.
File Structure
merge_txt_files.py: The main script that handles the merging and splitting of text files.
README.md: Documentation and instructions on how to use the script.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Thanks to the open-source community for their continuous support and contributions.

