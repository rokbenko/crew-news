from crewai import Crew, Process
from utils.agents import UnbiasedNewsAgents
from utils.tasks import UnbiasedNewsTasks
from langchain_openai import ChatOpenAI
import streamlit as st

# Initialize Llama 3.1 70B LLM
llm = ChatOpenAI(
    openai_api_base="https://api.aimlapi.com/v1",
    api_key=st.session_state["aiml_api_key"],
    model_name="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
)


class UnbiasedNewsCrew:
    def __init__(self, topic: str, selected_country: str):
        """
        Initializes the UnbiasedNewsCrew.

        The UnbiasedNewsCrew is responsible for getting all written content from multiple media providers for the given topic and making an unbiased version of the news.

        :param topic: The topic for which to get the unbiased news.
        :param selected_country: The country for which to get the unbiased news.

        :return: An instance of UnbiasedNewsCrew.
        """

        # Instantiate agents and tasks for the crew
        agents = UnbiasedNewsAgents()

        tasks = UnbiasedNewsTasks()

        # Create agent instances for various roles
        self.media_expert = agents.media_expert_agent()

        self.web_domain_expert = agents.web_domain_expert_agent()

        self.written_content_expert = agents.written_content_expert_agent()

        self.text_extraction_expert = agents.text_extraction_expert_agent()

        self.unbiased_journalist = agents.unbiased_journalist_agent()

        # Define tasks for the crew
        self.get_media_providers = tasks.get_media_providers_task(
            self.media_expert,
            selected_country,
        )

        self.get_media_provider_web_domain = tasks.get_media_provider_web_domain_task(
            self.web_domain_expert,
        )

        self.get_media_provider_written_content_urls = (
            tasks.get_media_provider_written_content_urls_task(
                self.written_content_expert,
                topic,
            )
        )

        self.get_written_content_from_url = tasks.get_written_content_from_url_task(
            self.text_extraction_expert,
        )

        self.get_unbiased_news = tasks.get_unbiased_news_task(
            self.unbiased_journalist,
        )

        # Create the crew with the specified agents and tasks
        self.crew = Crew(
            agents=[
                self.media_expert,
                self.web_domain_expert,
                self.written_content_expert,
                self.text_extraction_expert,
                self.unbiased_journalist,
            ],
            tasks=[
                self.get_media_providers,
                self.get_media_provider_web_domain,
                self.get_media_provider_written_content_urls,
                self.get_written_content_from_url,
                self.get_unbiased_news,
            ],
            manager_llm=llm,
            process=Process.sequential,
            share_crew=False,
            verbose=True,
        )

    def start_news_agents(self):
        """
        Starts all the agents in the crew.

        This function returns the result of the crew's kickoff function, which is a dictionary
        containing the results of all the tasks in the crew.

        :return: The result of the crew's tasks.
        """

        return self.crew.kickoff()
