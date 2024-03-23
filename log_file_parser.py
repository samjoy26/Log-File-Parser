import tkinter as tk
from tkinter import filedialog

def parse_log_file(log_file_paths, specific_string):
    found_lines = []

    for log_file_path in log_file_paths:
        with open(log_file_path, 'r') as file:
            lines_with_string = []
            for line in file:
                if specific_string.lower() in line.lower():
                    lines_with_string.append(line.strip())
            if lines_with_string:
                found_lines.append((log_file_path, lines_with_string))

    return found_lines

def main():
    # Hide the root window
    root = tk.Tk()
    root.withdraw()

    # Get specific string from user
    specific_string = input("Enter the specific string: ").strip().lower()
    if not specific_string:
        print("No specific string provided. Exiting.")
        return

    # Prompt user to select multiple log files
    log_file_paths = filedialog.askopenfilenames(title="Select Log Files", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not log_file_paths:
        print("No log files selected. Exiting.")
        return

    # Parse log files
    found_lines = parse_log_file(log_file_paths, specific_string)
    if found_lines:
        print("Lines containing the specific string:")
        for file_name, lines in found_lines:
            print(f"File: {file_name}")
            for line in lines:
                print(line)
    else:
        print("No lines containing the specific string found in the selected log files.")

if __name__ == "__main__":
    main()
