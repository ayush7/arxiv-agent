import os
from PyPDF2 import PdfReader
from typing import List, Dict

def parse_pdf(pdf_path: str) -> Dict:
    """
    Parses a PDF file, extracts text content, chunks it, and returns it with metadata.

    Args:
        pdf_path: The path to the PDF file.

    Returns:
        A dictionary containing the extracted text chunks and metadata.  Returns None if there's an error.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PdfReader(pdf_file)
            num_pages = len(reader.pages)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

        # Metadata
        pdf_name = os.path.basename(pdf_path)
        metadata = {
            "pdf_name": pdf_name,
            "num_pages": num_pages,
            "total_characters": len(text)
        }

        # Mega chunk
        mega_chunk = text

        # Chunking
        chunk_size = 4000
        overlap = 500
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunks.append(text[start:end])
            start += chunk_size - overlap

        return {
            "metadata": metadata,
            "mega_chunk": mega_chunk,
            "chunks": chunks
        }

    except FileNotFoundError:
        print(f"Error: PDF file not found at {pdf_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


    
# Access Metadata with result['metadata']
# Access individual chunks using result['chunks'][i]
# Access mega chunk using result['mega_chunk']
