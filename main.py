import fitz  # PyMuPDF
import pyttsx3


def pdf_to_text(pdf_file):
    try:
        # Open the provided PDF file
        document = fitz.open(pdf_file)

        # Initialize a string to store the text from the PDF
        text = ""

        # Iterate through each page in the PDF and extract text
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

        # Close the document
        document.close()

        return text

    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


def text_to_speech(text):
    try:
        # Initialize the Text-to-Speech engine
        engine = pyttsx3.init()

        # Setting up voice rate and properties
        engine.setProperty('rate', 150)  # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1

        # Convert text to speech
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error converting text to speech: {e}")


if __name__ == "__main__":
    pdf_file = "C:/path/to/your/example.pdf"  # Replace with your PDF file path

    # Extract text from PDF
    extracted_text = pdf_to_text(pdf_file)

    if extracted_text:
        # Convert extracted text to speech
        text_to_speech(extracted_text)
    else:
        print("Failed to extract text from PDF.")
