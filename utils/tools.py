from crewai_tools import tool
from exa_py import Exa
from firecrawl.firecrawl import FirecrawlApp
import streamlit as st


class UnbiasedNewsTools:
    def _exa():
        """
        Returns an instance of the Exa search engine with the given API key.

        :return: An instance of Exa.
        """

        return Exa(api_key=st.session_state["exa_api_key"])

    def _firecrawl():
        """
        Returns an instance of FirecrawlScrapeWebsiteTool with the given API key.

        :return: An instance of FirecrawlScrapeWebsiteTool.
        """

        return FirecrawlApp(api_key=st.session_state["firecrawl_api_key"])

    @tool("Exa custom tool")
    def exa_search_and_get_contents_tool(
        question: str,
    ) -> str:
        """
        Searches the web for relevant content given a question and returns the contents of the most relevant result.

        :param question: The question to search for.
        :return: The HTML contents of the most relevant result.
        """

        response = UnbiasedNewsTools._exa().search_and_contents(
            query=question,
            type="neural",
            use_autoprompt=False,
            num_results=5,
            text=True,
            summary=True,
        )

        return response

    @tool("Firecrawl custom tool")
    def firecrawl_scrape_tool(
        url: str,
    ) -> str:
        """
        Scrapes the given URL and returns the HTML content.

        :param url: The URL to scrape.
        :return: The HTML content of the scraped URL.
        """

        response = UnbiasedNewsTools._firecrawl().scrape_url(url)

        return response

    @staticmethod
    def get_all_search_tools():
        """
        Returns all search tools available.

        :return: A list of search tools, currently only ExaSearchAndGetContentsTool.
        """

        return [UnbiasedNewsTools.exa_search_and_get_contents_tool]

    @staticmethod
    def get_all_scraping_tools():
        """
        Returns all scraping tools available.

        :return: A list of scraping tools, currently only FirecrawlScrapeTool.
        """

        return [UnbiasedNewsTools.firecrawl_scrape_tool]
