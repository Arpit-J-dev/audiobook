# audiobook
# Audiobook Converter in Python

## Project Overview
This project is a simple Audiobook Converter built in Python. It allows you to select a PDF file and convert its text content into an audiobook by reading it aloud using a text-to-speech (TTS) engine.

## Features
- Convert PDF files into spoken audio.
- Uses pyttsx3 (offline TTS engine) for narration.
- Easy-to-use file selection system.
- Works on multiple platforms (Windows, macOS, Linux).

## Tools & Libraries
- Python 3.x
- pyttsx3 – Text-to-Speech conversion
- PyPDF2 (or fitz/PyMuPDF) – For extracting text from PDFs

## Project Structure
audiobook_converter/
│-- audiobook_converter.py   # Main script
│-- requirements.txt         # Dependencies
│-- README.txt               # Project Documentation

## Installation & Setup
1. Clone or download the project.
2. Install dependencies:
   pip install pyttsx3 PyPDF2
3. Run the script:
   python audiobook_converter.py

## Usage
1. When prompted, select the PDF file you want to convert.
2. The program will extract text and start reading it aloud.
3. You can pause, stop, or adjust the voice and speed.

## Future Improvements
- Option to save the audiobook as an MP3 file.
- Support for multiple file formats (EPUB, DOCX).
- Add a GUI for easier interaction.

## Author
Developed as a beginner-friendly project to explore Python automation and audiobook creation.
