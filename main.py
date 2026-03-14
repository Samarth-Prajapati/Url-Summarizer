import validators, streamlit as st
from UrlSummarizer import prompt, loader, summarizer

import warnings
warnings.filterwarnings("ignore")

class StreamlitSummarizer:
    """Summarize Text From YT/Website using Streamlit"""

    def __init__(self):
        self.groq_api_key = None
        self.generic_url = None
        self.docs = None
        self.chain = None
        self.output = None

    def streamlit_frontend(self):
        """
        Streamlit frontend for YT/Website
        :return: None
        """

        # Page Configuration
        st.set_page_config(
            page_title = "Summarize Text",
            page_icon = "🤖"
        )

        st.title("Summarize Text From YT/Website")
        st.subheader("Summarize URL")

        # Sidebar Configuration
        st.sidebar.title("Settings")
        with st.sidebar:
            self.groq_api_key = st.text_input(
                "Groq API Key",
                value = "",
                type = "password",
                placeholder = "Enter your Groq API Key"
            )

        # Page Body Configuration and Workflow
        self.generic_url = st.text_input(
            "URL",
            label_visibility = "collapsed"
        )

        if st.button("Summarize"):
            if not self.groq_api_key.strip() or not self.generic_url.strip():
                st.error("Please provide the information to get started.")

            elif not validators.url(self.generic_url):
                st.error("Please enter a valid URL.")

            else:
                try:
                    with st.spinner("Analyzing URL and generating summary..."):     # type: ignore
                        self.docs = loader.load_url(self.generic_url)
                        if not self.docs:
                            st.error("Unable to extract content from this URL. Try another website.")
                            st.stop()

                        self.chain = summarizer.create_chain(self.groq_api_key, prompt)

                        st.info("Generating summary")
                        self.output = self.chain.run(self.docs)
                        st.text("Output:")
                        st.success(self.output)

                except Exception as error:
                    st.error("Something went wrong while processing the URL.")
                    st.exception(error)

if __name__ == "__main__":
    app = StreamlitSummarizer()
    app.streamlit_frontend()