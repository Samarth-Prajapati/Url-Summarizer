from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

class UrlLoader:
    """URL Loader class for checks and load URL for summarizing content"""

    def __init__(self):
        self.loader = None
        self.language = ["gu", "hi", "en"]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/120 Safari/537.36"
        }
        self.docs = None

    def check_url(self, generic_url):
        """
        Checks if the url provided is valid or not
        :return: None
        """

        try:
            if "youtube.com" in generic_url or "youtu.be" in generic_url:

                # Loader for loading YouTube video URL in 3 different languages
                self.loader = YoutubeLoader.from_youtube_url(
                    generic_url,
                    add_video_info = False,
                    language = self.language
                )

            else:

                # Loader for loading normal website URL
                self.loader = UnstructuredURLLoader(
                    urls = [generic_url],
                    ssl_verify = False,
                    headers = self.headers
                )

        except Exception as error:
            print(error)

    def load_url(self, generic_url):
        """
        Loads the url provided
        :return: docs
        """

        self.check_url(generic_url)

        try:
            self.docs = self.loader.load()
            return self.docs

        except Exception as error:
            print(error)

loader = UrlLoader()