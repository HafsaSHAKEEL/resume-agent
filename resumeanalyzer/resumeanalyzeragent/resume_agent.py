from agency_swarm import Agent

from resumeanalyzer.resumeanalyzeragent.tools.confidence_tool import ConfidenceLevelTool


class ResumeMatchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ResumeMatchAgent",
            description="Agent responsible for evaluating the match between resumes and job descriptions across various developer roles.",
            instructions="You are responsible for using tools to assess resume-job fitment and reporting the match percentage.",
            tools=[ConfidenceLevelTool],
            temperature=0.5,
            max_prompt_tokens=25000,
        )

    def get_assistant_settings(self):
        return {
            "name": self.name,
            "description": self.description,
            "tools": [tool.__class__.__name__ for tool in self.tools],
        }

    def init_oai(self):
        # Custom initialization logic (if any)
        assistant_settings = self.get_assistant_settings()
        # If no custom logic is needed, this can remain empty


def evaluate_resume(resume_pdf_path, job_description):
    tool = ConfidenceLevelTool(
        resume_pdf_path=resume_pdf_path, job_description=job_description
    )
    return tool.run()
