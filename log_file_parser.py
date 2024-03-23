import tkinter as tk
from tkinter import filedialog

def parse_log_file(log_file_path, specific_string):
    found_lines = []

    with open(log_file_path, 'r') as file:
        for line in file:
            if specific_string.lower() in line.lower():
                found_lines.append(line.strip())

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

    # Prompt user to select the log file
    log_file_path = filedialog.askopenfilename(title="Select Log File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not log_file_path:
        print("No log file selected. Exiting.")
        return

    # Parse log file
    found_lines = parse_log_file(log_file_path, specific_string)
    if found_lines:
        print("Lines containing the specific string:")
        for line in found_lines:
            print(line)
    else:
        print("No lines containing the specific string found in the log file.")

if __name__ == "__main__":
    main()
