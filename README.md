# Document Converter

A simple GUI application to convert PDF and Word documents to text files.

## Features

- User-friendly graphical interface
- Supports PDF and DOCX files (DOC files need to be saved as DOCX)
- Organized input and output folders
- Batch conversion support
- Timestamp-based output file naming
- Proper text extraction using specialized libraries

## Requirements

- Python 3.x
- python-docx
- PyPDF2

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Use

1. Run the application:
   ```
   python converter.py
   ```

2. Use the "Upload Files" button to select documents for conversion
   - Supported formats: PDF, DOCX
   - Files will be copied to the `input` folder

3. Click "Convert Files" to process all uploaded documents
   - Converted files will be saved in the `output` folder
   - Each output file includes a timestamp in its name

## Project Structure

```
project/
├── converter.py      # Main application file
├── requirements.txt  # Python dependencies
├── uploads/           # Directory for input files
└── output/          # Directory for converted files
```

## Notes

- The application automatically creates `uploads` and `output` directories if they don't exist
- Output files are named with the format: `originalname_YYYYMMDD_HHMMSS.txt`
- The interface shows the status of operations and any errors that occur
- Old .doc files are not supported - please save them as .docx before converting
