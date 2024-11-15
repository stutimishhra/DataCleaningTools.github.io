'''import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font as tkFont

# Global DataFrame to hold the loaded data
df = pd.DataFrame()

# Function to load CSV file
def load_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        display_dataframe(df, "Loaded DataFrame:")

# Display DataFrame in text area
def display_dataframe(dataframe, title=""):
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, title + "\n")
    text_area.insert(tk.END, dataframe.to_string(index=False) + "\n\n")

# Data Cleaning Functions
def handle_missing_values():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for column in df.select_dtypes(include=[float, int]).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    for column in df.select_dtypes(include=[object]).columns:
        df[column].fillna("Unknown", inplace=True)
    display_dataframe(df, "DataFrame after handling missing values:")

def remove_duplicates():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    df.drop_duplicates(inplace=True)
    display_dataframe(df, "DataFrame after removing duplicates:")

def fix_data_types():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for column in df.select_dtypes(include=[float]).columns:
        df[column] = df[column].astype(int)
    display_dataframe(df, "DataFrame after fixing data types:")

def standardize_text_data():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for column in df.select_dtypes(include=[object]).columns:
        df[column] = df[column].str.strip().str.lower().str.title()
    display_dataframe(df, "DataFrame after standardizing text data:")

def handle_outliers():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for column in df.select_dtypes(include=[float, int]).columns:
        mean = df[column].mean()
        std_dev = df[column].std()
        df = df[(df[column] >= mean - 3 * std_dev) & (df[column] <= mean + 3 * std_dev)]
    display_dataframe(df, "DataFrame after handling outliers:")

# Set up the Tkinter root window
root = tk.Tk()
root.title("Enhanced Data Cleaning Application")
root.geometry("950x700")
root.configure(bg="#2f3b52")

# Styles
header_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
text_font = tkFont.Font(family="Courier", size=11)

# Frame for Buttons
button_frame = tk.Frame(root, bg="#2f3b52")
button_frame.pack(pady=20)

# Buttons
load_button = tk.Button(button_frame, text="Load CSV File", command=load_file, bg="#76c7c0", fg="white", font=button_font, width=20)
load_button.grid(row=0, column=0, padx=10, pady=10)

missing_values_button = tk.Button(button_frame, text="Handle Missing Values", command=handle_missing_values, bg="#f3a683", fg="white", font=button_font, width=20)
missing_values_button.grid(row=1, column=0, padx=10, pady=10)

remove_duplicates_button = tk.Button(button_frame, text="Remove Duplicates", command=remove_duplicates, bg="#3dc1d3", fg="white", font=button_font, width=20)
remove_duplicates_button.grid(row=1, column=1, padx=10, pady=10)

fix_data_types_button = tk.Button(button_frame, text="Fix Data Types", command=fix_data_types, bg="#ffb8b8", fg="white", font=button_font, width=20)
fix_data_types_button.grid(row=2, column=0, padx=10, pady=10)

standardize_text_button = tk.Button(button_frame, text="Standardize Text Data", command=standardize_text_data, bg="#e77f67", fg="white", font=button_font, width=20)
standardize_text_button.grid(row=2, column=1, padx=10, pady=10)

handle_outliers_button = tk.Button(button_frame, text="Handle Outliers", command=handle_outliers, bg="#63cdda", fg="white", font=button_font, width=20)
handle_outliers_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Text area for displaying DataFrame content
text_area = scrolledtext.ScrolledText(root, height=20, font=text_font, bg="#f0f4f8", fg="#34495e", wrap="none")
text_area.pack(padx=15, pady=10, fill="both", expand=True)

# Run the Tkinter event loop
root.mainloop()'''

'''import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# DataFrame to hold the loaded data
df = pd.DataFrame()

# Function to load CSV file
def load_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        display_dataframe(df, "Loaded DataFrame:")

# Display DataFrame in text area
def display_dataframe(dataframe, title=""):
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, title + "\n")
    text_area.insert(tk.END, dataframe.to_string(index=False) + "\n\n")

# Data Cleaning Functions
def handle_missing_values():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    # Handle missing values for numeric and text columns
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna('Unknown', inplace=True)
    display_dataframe(df, "DataFrame after handling missing values:")

def remove_duplicates():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    df.drop_duplicates(inplace=True)
    display_dataframe(df, "DataFrame after removing duplicates:")

def fix_data_types():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for col in df.columns:
        if df[col].dtype == 'float64':
            df[col] = df[col].astype(int)
    display_dataframe(df, "DataFrame after fixing data types:")

def standardize_text_data():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().str.title()
    display_dataframe(df, "DataFrame after standardizing text data:")

def handle_outliers():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        col_mean = df[col].mean()
        col_std = df[col].std()
        threshold_upper = col_mean + 3 * col_std
        threshold_lower = col_mean - 3 * col_std
        df = df[(df[col] >= threshold_lower) & (df[col] <= threshold_upper)]
    display_dataframe(df, "DataFrame after handling outliers:")

# Set up the Tkinter root window
root = tk.Tk()
root.title("Data Cleaning Application")
root.geometry("950x600")
root.configure(bg="#34495e")

# Create a frame for buttons
button_frame = tk.Frame(root, bg="#34495e")
button_frame.pack(pady=10)

# Button Styling and Layout
button_font = ("Courier New", 10, "bold")
button_bg_1 = "#1abc9c"
button_bg_2 = "#e67e22"

load_button = tk.Button(button_frame, text="Load CSV File", command=load_file, bg=button_bg_1, fg="white", font=button_font, width=20)
load_button.grid(row=0, column=0, padx=10, pady=10)

missing_values_button = tk.Button(button_frame, text="Handle Missing Values", command=handle_missing_values, bg=button_bg_1, fg="white", font=button_font, width=20)
missing_values_button.grid(row=0, column=1, padx=10, pady=10)

remove_duplicates_button = tk.Button(button_frame, text="Remove Duplicates", command=remove_duplicates, bg=button_bg_1, fg="white", font=button_font, width=20)
remove_duplicates_button.grid(row=1, column=0, padx=10, pady=10)

fix_data_types_button = tk.Button(button_frame, text="Fix Data Types", command=fix_data_types, bg=button_bg_1, fg="white", font=button_font, width=20)
fix_data_types_button.grid(row=1, column=1, padx=10, pady=10)

standardize_text_button = tk.Button(button_frame, text="Standardize Text Data", command=standardize_text_data, bg=button_bg_1, fg="white", font=button_font, width=20)
standardize_text_button.grid(row=2, column=0, padx=10, pady=10)

handle_outliers_button = tk.Button(button_frame, text="Handle Outliers", command=handle_outliers, bg=button_bg_1, fg="white", font=button_font, width=20)
handle_outliers_button.grid(row=2, column=1, padx=10, pady=10)

# Create a scrolled text area for displaying DataFrame contents
text_area = scrolledtext.ScrolledText(root, height=20, font=("Courier New", 10), bg="#ecf0f1", fg="#34495e")
text_area.pack(padx=10, pady=10, fill="both", expand=True)

# Run the Tkinter event loop
root.mainloop()'''

import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Global DataFrame to hold the loaded data
df = pd.DataFrame()

# Function to load CSV file
def load_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            display_dataframe(df, "Loaded DataFrame:")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

# Function to display DataFrame in the text area
def display_dataframe(dataframe, title=""):
    text_area.delete("1.0", tk.END)
    if dataframe.empty:
        text_area.insert(tk.END, "No data available.\n")
    else:
        text_area.insert(tk.END, title + "\n")
        text_area.insert(tk.END, dataframe.to_string(index=False) + "\n\n")

# Data Cleaning Functions
def handle_missing_values():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    try:
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna('Unknown', inplace=True)
        display_dataframe(df, "DataFrame after handling missing values:")
    except Exception as e:
        messagebox.showerror("Error", f"Error handling missing values: {str(e)}")

def remove_duplicates():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    try:
        initial_rows = len(df)
        df.drop_duplicates(inplace=True)
        final_rows = len(df)
        display_dataframe(df, f"Removed {initial_rows - final_rows} duplicate rows. Updated DataFrame:")
    except Exception as e:
        messagebox.showerror("Error", f"Error removing duplicates: {str(e)}")

def fix_data_types():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    try:
        for col in df.columns:
            if pd.api.types.is_float_dtype(df[col]):
                df[col] = df[col].fillna(0).astype(int)  # Safely convert to integers
            elif pd.api.types.is_object_dtype(df[col]):
                df[col] = df[col].astype(str)
        display_dataframe(df, "DataFrame after fixing data types:")
    except Exception as e:
        messagebox.showerror("Error", f"Error fixing data types: {str(e)}")

def standardize_text_data():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    try:
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip().str.title().fillna('Unknown')
        display_dataframe(df, "DataFrame after standardizing text data:")
    except Exception as e:
        messagebox.showerror("Error", f"Error standardizing text data: {str(e)}")

def handle_outliers():
    global df
    if df.empty:
        messagebox.showwarning("Warning", "Please load a CSV file first!")
        return
    try:
        for col in df.select_dtypes(include=['float64', 'int64']).columns:
            col_mean = df[col].mean()
            col_std = df[col].std()
            threshold_upper = col_mean + 3 * col_std
            threshold_lower = col_mean - 3 * col_std
            df = df[(df[col] >= threshold_lower) & (df[col] <= threshold_upper)]
        display_dataframe(df, "DataFrame after handling outliers:")
    except Exception as e:
        messagebox.showerror("Error", f"Error handling outliers: {str(e)}")

# Tkinter UI Setup
root = tk.Tk()
root.title("Data Cleaning Application")
root.geometry("950x600")
root.configure(bg="#34495e")

# Create button frame
button_frame = tk.Frame(root, bg="#34495e")
button_frame.pack(pady=10)

# Button Styling and Layout
button_font = ("Courier New", 10, "bold")
button_bg_1 = "#1abc9c"

load_button = tk.Button(button_frame, text="Load CSV File", command=load_file, bg=button_bg_1, fg="white", font=button_font, width=20)
load_button.grid(row=0, column=0, padx=10, pady=10)

missing_values_button = tk.Button(button_frame, text="Handle Missing Values", command=handle_missing_values, bg=button_bg_1, fg="white", font=button_font, width=20)
missing_values_button.grid(row=0, column=1, padx=10, pady=10)

remove_duplicates_button = tk.Button(button_frame, text="Remove Duplicates", command=remove_duplicates, bg=button_bg_1, fg="white", font=button_font, width=20)
remove_duplicates_button.grid(row=1, column=0, padx=10, pady=10)

fix_data_types_button = tk.Button(button_frame, text="Fix Data Types", command=fix_data_types, bg=button_bg_1, fg="white", font=button_font, width=20)
fix_data_types_button.grid(row=1, column=1, padx=10, pady=10)

standardize_text_button = tk.Button(button_frame, text="Standardize Text Data", command=standardize_text_data, bg=button_bg_1, fg="white", font=button_font, width=20)
standardize_text_button.grid(row=2, column=0, padx=10, pady=10)

handle_outliers_button = tk.Button(button_frame, text="Handle Outliers", command=handle_outliers, bg=button_bg_1, fg="white", font=button_font, width=20)
handle_outliers_button.grid(row=2, column=1, padx=10, pady=10)

# Scrolled text area for displaying DataFrame contents
text_area = scrolledtext.ScrolledText(root, height=20, font=("Courier New", 10), bg="#ecf0f1", fg="#34495e")
text_area.pack(padx=10, pady=10, fill="both", expand=True)

# Run the Tkinter application
root.mainloop()