```markdown
# Resume Analyzer

This project is a Resume Analyzer that evaluates a resume (in PDF format) against a job description and returns a match percentage. The tool leverages AI to assess the alignment between the candidate's resume and the job requirements.

## Project Structure

```
resumeanalyzer/
│
├── resumeanalyzeragent/
│   ├── __init__.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── confidence_tool.py
│   │   ├── pdf_reader.py
│   ├── files/
│   │   ├── pdf.pdf  # Example PDF file to be analyzed
│   ├── resume_agent.py
│
├── agency.py  # Main script to run the agency
├── .env  # Environment variables including API keys and file paths
├── requirements.txt  # List of dependencies
├── README.md  # This readme file
```

## Features

- **Confidence Level Calculation**: Uses AI to evaluate the resume against the job description and calculate a match percentage.
- **Flexible Evaluation Criteria**: The tool evaluates various aspects of the resume, such as programming languages, role-specific expertise, and problem-solving abilities.

## Prerequisites

- Python 3.7+
- API keys and credentials (e.g., OpenAI API Key) stored in the `.env` file.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/resumeanalyzer.git
    cd resumeanalyzer
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory with the following content:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    RESUME_PDF_PATH=/home/hafsa/PycharmProjects/pythonProject14/resumeanalyzer/resumeanalyzeragent/files/pdf.pdf
    ```

## Usage

1. **Running the Agency:**

    To evaluate a resume against a job description, run the `agency.py` script:

    ```bash
    python agency.py
    ```

    This will process the PDF file located at the `RESUME_PDF_PATH` and evaluate it against the job description provided in the script.

2. **Modifying the Job Description:**

    You can modify the job description text within the `agency.py` file to evaluate different job roles.

## Example Output

When you run the script, it will output the confidence level, including detailed criteria evaluations and the overall match percentage.

```plaintext
Starting the resume evaluation process...
Confidence Level: The provided resume for John Doe showcases strong skills in Python, Django, and JavaScript. However, more experience in cloud platforms like AWS is required for this role.
Match Percentage: 85%
```

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is open-source and available under the [MIT License](LICENSE).

```

### Key Points:
- **Project Structure:** Clearly lays out the directory structure and purpose of each file.
- **Setup Instructions:** Guides the user on how to install dependencies, set up environment variables, and run the project.
- **Usage Section:** Provides clear instructions on how to run the script and what output to expect.
- **Example Output:** Helps users understand what they will see when they run the script.
- **Contributing:** Encourages others to contribute to the project.
- **License:** You can add a license of your choice to the project if it’s open-source.

