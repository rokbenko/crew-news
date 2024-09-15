from crewai import Agent
from utils.tools import UnbiasedNewsTools
from langchain_openai import ChatOpenAI
import streamlit as st

# Initialize Llama 3.1 70B LLM
llm = ChatOpenAI(
    openai_api_base="https://api.aimlapi.com/v1",
    api_key=st.session_state["aiml_api_key"],
    model_name="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
)

# Initialize search tools from the UnbiasedNewsTools utility
search_tools = UnbiasedNewsTools().get_all_search_tools()

# Initialize scraping tools from the UnbiasedNewsTools utility
scraping_tools = UnbiasedNewsTools().get_all_scraping_tools()


class UnbiasedNewsAgents:
    def media_expert_agent(self):
        """
        Returns an Agent responsible for getting media providers, both left, centered, and right for a given country.

        This agent is responsible for getting media providers, both left, centered, and right for a given country.

        :return: An Agent with the given role, goal, backstory, and parameters.
        """

        return Agent(
            role="Senior media expert",
            goal=f"Get media providers, both left, centered, and right for a given country.",
            backstory="You're an expert on media providers for any given country.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
            max_iter=1,
        )

    def web_domain_expert_agent(self):
        """
        Returns an Agent responsible for getting the domain URL for a given media provider.

        This agent is responsible for getting the domain URL for a given media provider.

        :return: An Agent with the given role, goal, backstory, and parameters.
        """

        return Agent(
            role="Senior web domain expert",
            goal="Get the domain URL for a given media provider.",
            backstory="You're an expert on the domain URL for any given media provider.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
            max_iter=1,
        )

    def written_content_expert_agent(self):
        """
        Returns an Agent responsible for getting URLs of written content for a given topic for a given media provider.

        This agent is responsible for getting URLs of written content for a given topic for a given media provider.

        :return: An Agent with the given role, goal, backstory, and parameters.
        """

        return Agent(
            role="Senior written content expert",
            goal="Get URLs of written content for a given topic for a given media provider.",
            backstory="You're an expert on written content for any given topic for any given media provider.",
            llm=llm,
            tools=search_tools,
            allow_delegation=False,
            verbose=True,
            max_iter=20,
        )

    def text_extraction_expert_agent(self):
        """
        Returns an Agent responsible for extracting all written content from a given content URL.

        This agent is responsible for extracting all written content from a given content URL.

        :return: An Agent with the given role, goal, backstory, and parameters.
        """

        return Agent(
            role="Senior text extraction expert",
            goal="Get all written content for a given content URL.",
            backstory="You're an expert on written content for any given content URL. You know all the written content that the given content URL has.",
            llm=llm,
            tools=scraping_tools,
            allow_delegation=False,
            verbose=True,
            max_iter=20,
        )

    def unbiased_journalist_agent(self):
        """
        Returns an Agent responsible for writing an unbiased comprehensive article based on all written content from multiple media providers.

        This agent is responsible for writing an unbiased comprehensive article based on all written content from multiple media providers.

        :return: An Agent with the given role, goal, backstory, and parameters.
        """

        return Agent(
            role="Senior unbiased journalist",
            goal="Write an ubiased comprehensive article based on all written content from multiple media providers.",
            backstory="You're an unbiased journalist. You know all the written content from multiple media providers. You hate when a news is biased meaning it only represents one view on the given topic. You know that there are left, centered and right media providers and they only represent one view on the given topic. You want to make all written content from multiple media providers for the given topic unbiased by emphasizing multiple views.",
            llm=llm,
            allow_delegation=False,
            verbose=True,
            max_iter=1,
        )
