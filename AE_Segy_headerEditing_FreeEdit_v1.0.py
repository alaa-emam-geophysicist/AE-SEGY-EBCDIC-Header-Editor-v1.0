import tkinter as tk
from tkinter import filedialog, messagebox
import codecs

def read_ebcdic_header(file_path):
    try:
        # Open the SEGY file and read the EBCDIC header
        with open(file_path, 'rb') as f:
            ebcdic_header = f.read(3200)
            ascii_header = codecs.decode(ebcdic_header, 'cp037')
            return ascii_header
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read SEGY header:\n{e}")
        return None

def save_ebcdic_header(file_path, header_text):
    try:
        # Ensure header_text is a string and encode it to EBCDIC
        ascii_header = header_text.encode('ascii', 'ignore').decode('ascii')  # Ensure text is ASCII
        ebcdic_header = codecs.encode(ascii_header, 'cp037')
        # Open file in binary write mode
        with open(file_path, 'r+b') as f:
            f.seek(0)  # Go to the start of the file
            # Write EBCDIC header and pad if necessary
            f.write(ebcdic_header.ljust(3200, b'\x00'))
        messagebox.showinfo("Success", "EBCDIC header updated and saved.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save SEGY header:\n{e}")

def display_and_edit_header():
    file_path = filedialog.askopenfilename(
        title="Select SEGY File",
        filetypes=(("SEGY Files", "*.segy"), ("All Files", "*.*"))
    )
    if file_path:
        header_text = read_ebcdic_header(file_path)
        if header_text:
            # Create a new window for editing
            edit_window = tk.Toplevel(root)
            edit_window.title("EBCDIC Header Editor")
            
            text_area = tk.Text(edit_window, wrap=tk.WORD, width=80, height=20)
            text_area.pack(expand=True, fill=tk.BOTH)
            
            text_area.insert(tk.END, header_text)
            text_area.config(state=tk.NORMAL)  # Make text area editable
            
            def save_and_close():
                edited_text = text_area.get("1.0", tk.END)
                save_ebcdic_header(file_path, edited_text)
                edit_window.destroy()

            save_button = tk.Button(edit_window, text="Save and Close", command=save_and_close)
            save_button.pack(pady=10)

def main():
    global root
    # Initialize the main window
    root = tk.Tk()
    root.title("AE SEGY EBCDIC Header Editor v1.0")

    # Button to edit EBCDIC header
    edit_button = tk.Button(root, text="Edit SEGY File EBCDIC Header", command=display_and_edit_header)
    edit_button.pack(pady=20)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
