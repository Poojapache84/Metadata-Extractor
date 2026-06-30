# Metadata Extractor

Intern ID: CITS4853

## Description

The Metadata Extractor is a Python application that extracts metadata from image files. It reads image information such as file name, image format, dimensions, color mode, file size, and EXIF metadata (if available). This project demonstrates file handling, image processing, and metadata extraction using Python.

## Technologies Used

- Python
- Pillow (PIL) Library
- OS Module

## Features

- Extracts image filename
- Displays image format
- Shows image dimensions (width × height)
- Displays image color mode
- Shows file size
- Extracts EXIF metadata (if available)
- Handles unsupported or invalid files gracefully

## Project Structure

```
Metadata-Extractor/
│
├── metadata_extractor.py
├── requirements.txt
└── README.md
```

## Installation

1. Install Python.
2. Install the required library:

```
pip install pillow
```

Or install using:

```
pip install -r requirements.txt
```

## How to Run

Open a terminal in the project folder and run:

```
python metadata_extractor.py
```

## Example Output

```
Enter image path: sample.jpg

File Name : sample.jpg
Image Format : JPEG
Dimensions : 1920 x 1080
Color Mode : RGB
File Size : 542 KB

EXIF Metadata:
Camera : Canon EOS 200D
Date Taken : 2024:07:15 10:30:20
```

## Learning Outcomes

- Python file handling
- Working with images
- Reading metadata
- Exception handling
- Using external Python libraries
- Building command-line applications

## Author

Pooja
