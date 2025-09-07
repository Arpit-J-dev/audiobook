import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2

def select_and_read_pdf():
    # Open file dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select a PDF file"
    )
    if not file_path:
        print("No file selected.")
        return

    # Read PDF
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

    if not text.strip():
        print("No readable text found in this PDF.")
        return

    # Setup TTS
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)   # Speed
    engine.setProperty("volume", 1.0) # Volume

    # Speak the text
    engine.say(text)
    engine.runAndWait()


# GUI for selecting PDF
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

select_and_read_pdf()
