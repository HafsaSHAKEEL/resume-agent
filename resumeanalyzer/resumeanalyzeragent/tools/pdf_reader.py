import PyPDF2


def read_pdf(pdf_path: str) -> str:
    """
    Reads text from a PDF file and returns it as a string.

    Args:
        pdf_path (str): The file path to the PDF document.

    Returns:
        str: The extracted text from the PDF.
    """
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text
