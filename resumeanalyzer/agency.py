import os
from dotenv import load_dotenv
from agency_swarm import set_openai_key, Agency
from resumeanalyzer.resumeanalyzeragent.resume_agent import (
    ResumeMatchAgent,
    evaluate_resume,
)


load_dotenv()


set_openai_key("YOUR_API_KEY")


resume_agent = ResumeMatchAgent()


agency = Agency(
    agency_chart=[  # agency chart
        resume_agent,
    ],
    shared_instructions="agency_manifesto.md",
    temperature=0.5,
    max_prompt_tokens=25000,
)

if __name__ == "__main__":

    resume_pdf_path = os.getenv("RESUME_PDF_PATH")

    if not resume_pdf_path:
        print("Error: The RESUME_PDF_PATH environment variable is not set.")
    else:

        job_description_text = """
            We are looking for a highly skilled **python developer** to join our team. The ideal candidate will have expertise in both front-end and back-end development, with a strong understanding of modern web technologies.
        """

        confidence_level = evaluate_resume(resume_pdf_path, job_description_text)

        if confidence_level:
            print(f"Match Percentage: {confidence_level}")
        else:
            print("No match percentage returned.")
