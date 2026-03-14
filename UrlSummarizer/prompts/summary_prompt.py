from langchain_core.prompts import PromptTemplate

class SummaryPrompt:
    """Prompt class for summarizing content"""

    def __init__(self):
        self.template = None
        self.prompt_template = None

    def system_prompt(self):
        """
        Prompt Template that generate summary content according to our requirements
        :return: prompt_template
        """

        try:
            self.template = """
                You are an expert content summarizer.

                Summarize the following content in clear bullet points.
                Focus on key ideas, insights, and conclusions.

                Language: English
                Limit: 300 words maximum.

                CONTENT: {text}
            """

            self.prompt_template = PromptTemplate(
                template = self.template,
                input_variables = ["text"]
            )

            return self.prompt_template

        except Exception as error:
            raise error

prompt = SummaryPrompt().system_prompt()