import requests
import os
from urllib.parse import urlparse

def is_arxiv_pdf(arxiv_link):
    """
    Checks if an arXiv link points to a PDF file.

    Args:
        arxiv_link: The URL of the arXiv link.

    Returns:
        True if the link points to a PDF, False otherwise.  Returns False if there's an error accessing the link.
    """
    try:
        response = requests.head(arxiv_link, allow_redirects=True)
        response.raise_for_status()
        if response.status_code == 302: #check for redirect
            pdf_link = response.headers.get('location')
            if pdf_link:
                response = requests.head(pdf_link, allow_redirects=False)
                response.raise_for_status()
                content_type = response.headers.get('content-type')
                return content_type and 'application/pdf' in content_type
            else:
                return False
        content_type = response.headers.get('content-type')
        return content_type and 'application/pdf' in content_type

    except requests.exceptions.RequestException as e:
        print(f"Error accessing link: {e}")
        return False


def download_arxiv_pdf(arxiv_link, download_dir=".downloaded_content"):
    """Downloads the PDF from the given arXiv link if it's a PDF.

    Args:
        arxiv_link: The URL of the arXiv link.
        download_dir: The directory to save the downloaded PDF. Defaults to ".downloaded_content".
    """
    if arxiv_link[-4:] == ".pdf":
        arxiv_link = arxiv_link
    else:
        arxiv_link = arxiv_link+".pdf"

    file_path = None

    if is_arxiv_pdf(arxiv_link):
        try:
            # Create the download directory if it doesn't exist
            os.makedirs(download_dir, exist_ok=True)

            response = requests.get(arxiv_link, stream=True)
            response.raise_for_status()

            # Extract filename from URL
            parsed_url = urlparse(arxiv_link)
            filename = os.path.basename(parsed_url.path)
            filepath = os.path.join(download_dir, filename)

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"PDF downloaded successfully to: {filepath}")
            file_path = os.path.abspath(filepath)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading PDF: {e}")
        
    else:
        print(f"The link '{arxiv_link}' does not point to a PDF.")
    
    return file_path





# Test usage 
# arxiv_link = "https://arxiv.org/pdf/2311.16386.pdf"
# is_pdf = is_arxiv_pdf(arxiv_link)
# print(f"Is '{arxiv_link}' a PDF? {is_pdf}")


# arxiv_link = "https://arxiv.org/abs/2311.16386"
# is_pdf = is_arxiv_pdf(arxiv_link)
# print(f"Is '{arxiv_link}' a PDF? {is_pdf}")

# arxiv_link = "https://arxiv.org/pdf/2311.16386.pdf"
# download_arxiv_pdf(arxiv_link)

# arxiv_link = "https://arxiv.org/abs/2311.16386"
# download_arxiv_pdf(arxiv_link)