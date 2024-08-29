from agency_swarm.tools import BaseTool
from pydantic import Field
from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from g4f import models
from langchain_g4f import G4FLLM


class ConfidenceLevelTool(BaseTool):
    resume_pdf_path: str = Field(..., description="The file path to the resume PDF.")
    job_description: str = Field(..., description="The job description text content.")

    def run(self):
        # Read the resume from the provided PDF file
        with open(self.resume_pdf_path, "rb") as file:
            reader = PdfReader(file)
            resume_text = ""
            for page in reader.pages:
                resume_text += page.extract_text()


        llm = G4FLLM(
            model=models.gpt_35_turbo,
        )


        prompt = PromptTemplate(
            input_variables=["resume", "job_description"],
            template="""
                You are an expert in evaluating resumes for various developer roles. Your task is to analyze the provided resume against the job description and determine how well they match, focusing on the skills, experience, and qualifications necessary for the specific role.

                **Evaluation Criteria:**

                1. **Programming Languages and Frameworks**:
                   - Match the programming languages and frameworks listed in the resume with those required in the job description (e.g., Python, Java, JavaScript, React, Django, TensorFlow).
                   - Evaluate the depth of experience in these technologies across different roles.

                2. **Role-Specific Expertise**:
                   - Assess the candidate's expertise based on the role (e.g., AI Engineer, UI/UX Developer, Full Stack Developer).
                   - Match their experience with the specific responsibilities and technologies mentioned in the job description.

                3. **Software Development Experience**:
                   - Analyze the candidate's overall software development experience, including roles, responsibilities, and project types.
                   - Consider the relevance of their past projects to the job description.

                4. **System Design and Architecture**:
                   - Evaluate the candidate's ability to design and implement systems, with a focus on scalability, maintainability, and efficiency.

                5. **Tools and Technologies**:
                   - Match the tools and technologies the candidate is familiar with to those required for the role (e.g., CI/CD tools, cloud platforms, data processing frameworks).

                6. **Problem-Solving and Innovation**:
                   - Assess the candidate's ability to solve complex problems and innovate within their field.
                   - Consider examples from the resume where they demonstrated problem-solving or innovative thinking.

                7. **Collaboration and Communication**:
                   - Evaluate the candidate's experience working in teams, including collaboration with other developers, designers, and stakeholders.
                   - Consider any leadership or mentoring roles mentioned in the resume.

                Based on these criteria, calculate a match percentage (between 0% to 100%) that represents how well the candidate fits the specific developer role described.

                **Resume**: {resume}
                **Job Description**: {job_description}

                **Match Percentage**: ...
            """,
        )

        llm_chain = LLMChain(llm=llm, prompt=prompt)


        response = llm_chain.run(
            {"resume": resume_text, "job_description": self.job_description}
        )
        return response
