from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain

class Summarizer:
    """Summarizer class that summarizes content using groq model"""

    def __init__(self):
        self.llm = None
        self.chain = None

    def load_llm(self, groq_api_key):
        """
        Loading Groq LLM model
        :return: None
        """

        try:
            self.llm = ChatGroq(
                api_key = groq_api_key,
                model = "llama-3.3-70b-versatile",
                temperature = 0.3
            )

        except Exception as error:
            print(error)

    def create_chain(self, groq_api_key, prompt):
        """
        Creating Chain model
        :return: chain
        """

        self.load_llm(groq_api_key)

        try:
            self.chain = load_summarize_chain(
                self.llm,
                chain_type = "stuff",
                prompt = prompt
            )
            return self.chain

        except Exception as error:
            raise error

summarizer = Summarizer()