# audiobook
# Project Report: Audiobook Converter in Python

## Introduction
Reading long documents or books in digital format can sometimes be tiring and time-consuming. Audiobooks provide a convenient way to consume content hands-free. This project, "Audiobook Converter in Python," is developed to automatically convert a PDF file into spoken audio using Python libraries.

## Objectives
- To build a Python-based tool that converts PDF files into audiobooks.
- To provide an offline text-to-speech solution.
- To make reading accessible and convenient for users.

## Methodology
1. **Extracting Text from PDF**  
   The project uses the PyPDF2 library to read and extract text from PDF files.
   
2. **Text-to-Speech Conversion**  
   The extracted text is converted into speech using the pyttsx3 library, which works offline and supports different voices and speech rates.
   
3. **Integration**  
   The program combines PDF reading and text-to-speech functionalities into a single script, providing a smooth audiobook experience.

## Tools & Technologies
- **Programming Language:** Python 3.x
- **Libraries Used:**
  - PyPDF2 (for PDF text extraction)
  - pyttsx3 (for text-to-speech conversion)

## Features
- Converts PDF documents into spoken audio.
- Works offline without requiring internet access.
- Cross-platform compatibility (Windows, macOS, Linux).
- Adjustable voice and speed settings.

## Results
The program successfully converts PDF text into speech and reads it aloud to the user. It simplifies the process of consuming digital content and makes reading accessible to people who prefer listening over reading.

## Limitations
- The program currently only works with text-based PDFs (not scanned images).
- The voice output is limited to system-installed voices.
- No built-in feature to save audio as MP3/WAV.

## Future Enhancements
- Add functionality to save audiobooks in MP3 format.
- Provide support for more file formats like DOCX and EPUB.
- Develop a GUI-based interface for better user experience.
- Integrate Optical Character Recognition (OCR) to support scanned PDFs.

## Conclusion
The Audiobook Converter in Python demonstrates the potential of combining simple libraries to build a useful and accessible tool. It serves as an excellent beginner-friendly project to explore file handling, text processing, and text-to-speech technologies in Python.

## Author
Developed as part of a learning project to improve skills in Python programming and automation.

