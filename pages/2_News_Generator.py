import streamlit as st
from utils.crews import UnbiasedNewsCrew
import agentops
import time

# Solve error when deploying Streamlit app on Streamlit Cloud: "Your system has an unsupported version of sqlite3. Chroma requires sqlite3 >= 3.35.0. Please visit https://docs.trychroma.com/troubleshooting#sqlite to learn how to upgrade."
__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")


def format_time(
    milliseconds: int,
) -> str:
    """
    Converts a time in milliseconds to a human-readable string.

    If the time is less than 1 second, it is displayed in milliseconds.
    If the time is less than 1 minute, it is displayed in seconds.
    If the time is 1 minute or more, it is displayed in minutes and seconds.

    Parameters:
        milliseconds (int): Time in milliseconds.

    Returns:
        str: Human-readable string representation of the time.
    """

    if milliseconds < 1000:
        return f"{int(milliseconds)} ms"
    elif milliseconds < 60000:
        return f"{int(milliseconds/1000)} s"
    else:
        minutes = milliseconds // 60000
        seconds = (milliseconds % 60000) // 1000

        return f"{minutes}min {seconds}s"


def main():
    """
    The main function for the News Generator page.

    This function sets up the Streamlit page configuration and user interface,
    initializes the AgentOps session for efficient management of AI agents,
    and orchestrates the UnbiasedNewsCrew to fetch and generate unbiased news content.

    Key Responsibilities:
        - Configures the Streamlit page settings, including title, icon,
          and sidebar navigation for a seamless user experience.
        - Initializes the AgentOps session, allowing for robust interaction
          and monitoring of AI agents throughout the news generation process.
        - Collects user input for news topics through a text input widget
          and triggers the news generation process upon user request.
        - Displays loading indicators to inform users of ongoing processing
          and provide humorous remarks to enhance user experience.
        - Presents the generated unbiased news in an organized format,
          ensuring clarity and readability.
        - Displays execution details, including total elapsed time and
          token usage statistics, to give users insight into the process
          and performance of the AI agents.

    Parameters:
        None

    Returns:
        None

    Pro Tip:
        While our AI agents are busy crafting the news, why not take a moment to
        relax with a coffee? You deserve it!
    """

    # Set up Streamlit page configuration
    st.set_page_config(
        page_title="CrewNews – US News Unbiased",
        page_icon="📰",
        menu_items={
            "Report a bug": "https://github.com/rokbenko/crew-news",
        },
    )

    # Add custom CSS for button hover effect
    st.markdown(
        body="""
            <style>
                button:hover {
                    transition: 0.2s all ease-in-out;
                }
            </style>
        """,
        unsafe_allow_html=True,
    )

    # Initialize AgentOps
    agentops.init(
        api_key=st.session_state["agentops_api_key"],
        default_tags=[
            "agentops",
            "llama-3.1-70b",
            "exa",
            "firecrawl",
        ],
        auto_start_session=False,
        skip_auto_end_session=True,
    )

    # Render sidebar
    with st.sidebar:
        # Render Home page link
        st.page_link(
            page="1_Home.py",
            label="Home",
            icon="🏠",
        )

        # Render News Generator page link
        st.page_link(
            page="pages/2_News_Generator.py",
            label="News Generator",
            icon="🤖",
        )

        # Render divider
        st.divider()

        # Render social media links
        st.markdown(
            body="""
                <div style='text-align: center; padding: 1rem 2rem; background-color: rgb(14, 17, 23); border-radius: 0.5rem;'>
                    <div style='margin-bottom: 0.5rem;'>
                        Made with ❤️ by Rok Benko
                    </div>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
                    <a href="https://www.linkedin.com/in/rokbenko/" style='text-decoration: none;'>
                        <i style='color: #0072B1; margin-right: 1rem;' class="fa-xl fa-brands fa-linkedin"></i>
                    </a>
                    <a href="https://stackoverflow.com/users/10347145/" style='text-decoration: none;'>
                        <i style='color: #F48024; margin-right: 1rem;' class="fa-xl fa-brands fa-stack-overflow"></i>
                    </a>
                    <a href="https://github.com/rokbenko" style='text-decoration: none;'>
                        <i style='color: #FFFFFF; margin-right: 1rem;' class="fa-xl fa-brands fa-github"></i>
                    </a>
                    <a href="https://www.youtube.com/@rokbenko?sub_confirmation=1" style='text-decoration: none;'>
                        <i style='color: #FF0000; margin-right: 1rem;' class="fa-xl fa-brands fa-youtube"></i>
                    </a>
                </div>
            """,
            unsafe_allow_html=True,
        )

        # Render space
        st.markdown(
            body="<div>&nbsp;</div>",
            unsafe_allow_html=True,
        )

        # Render powered by list of links
        st.markdown(
            body="""
                <div>Powered by:</div>
                <ul>
                    <li><a href="https://streamlit.io/">Streamlit</a> as a GUI</li>
                    <li><a href="https://www.llama.com/">Llama 3.1 70B</a> as LLM via <a href="https://aimlapi.com/">AIML</a></li>
                    <li><a href="https://www.crewai.com/">CrewAI</a> for building AI agents</li>
                    <li><a href="https://agentops.ai/">AgentOps</a> for testing AI agents</li>
                    <li><a href="https://exa.ai/">Exa</a> as a web search tool</li>
                    <li><a href="https://www.firecrawl.dev/">Firecrawl</a> as a web scraping tool</li>
                </ul>
            """,
            unsafe_allow_html=True,
        )

    # Render title
    st.markdown(
        body="<h1 style='text-align: center;'>📰 CrewNews 📰</h1>",
        unsafe_allow_html=True,
    )

    # Render subtitle
    st.markdown(
        body="<h3 style='text-align: center;'>US News Unbiased</h3>",
        unsafe_allow_html=True,
    )

    # Initalize columns for layout
    col_left, col_middle, col_right = st.columns([0.2, 0.6, 0.2])

    # Render middle column
    with col_middle:
        # Render text input
        user_question = st.text_input(
            label="Enter a topic or question (see the example below):",
            value="US Presidential Debate 2024 Harris vs Trump",
            help="CrewNews will provide an unbiased version of the news for a given topic you enter by combining content from media providers from the United States across the political spectrum.",
        )

        # Render search button
        search_button = st.button(
            label="Search 🚀",
            type="primary",
            use_container_width=True,
        )

    # If search button is clicked and user enters a question, start news agents
    if search_button and user_question:
        # Render status container
        with st.status(
            label="Just a moment! I'm coordinating with my AI agent coworkers... Unfortunately, one of them seems to be on a coffee break. Just kidding! This might take us 2-3 minutes. Go grab yourself a coffee—just don't be surprised if I ask for a refill!",
            state="running",
            expanded=True,
        ) as status:
            # Start AgentOps session
            agentops.start_session(
                tags=[
                    "agentops",
                    "llama-3.1-70b",
                    "exa",
                    "firecrawl",
                ],
            )

            # Start timer
            start_time = time.time()

            # Create an instance of the UnbiasedNewsCrew class
            crew = UnbiasedNewsCrew(
                selected_country="United States",
                topic=user_question,
            )

            # Start the news generation process using the initialized crew
            crew_response = crew.start_news_agents()

            # If any of the agents stopped due to iteration limit or time limit, update status and render error
            if (
                crew_response.raw
                == "Agent stopped due to iteration limit or time limit."
            ):
                # Update status
                status.update(
                    label="CrewNews stopped due to iteration limit or time limit. ☹️",
                    state="error",
                )

                # Render error
                st.error(
                    body="Agent stopped due to iteration limit or time limit. If you see this error, it's likely because the topic or question you entered is phrased in a way that AI agents behind the CrewNews couldn't pass to the AI tools in a way to get meaningful results. Please try to rephrase the topic or question.",
                    icon="❌",
                )

            # If CrewNews generated an unbiased version of the news, update status and render response
            else:
                # Stop timer
                stop_time = int((time.time() - start_time) * 1000)

                # Update status
                status.update(
                    label="CrewNews successfully generated an unbiased version of the news! 🎉",
                    state="complete",
                )

                # Render response
                st.write(crew_response.raw)

                # Render divider
                st.divider()

                # Reder run details
                st.markdown(
                    body=f"""
                        <h4>Run Details</h4>
                        <p>Total elapsed time: {format_time(stop_time)}</p>

                        <div>
                            Total tokens used: {crew_response.token_usage.total_tokens}<br>
                            Prompt tokens used: {crew_response.token_usage.prompt_tokens}<br>
                            Completion tokens used: {crew_response.token_usage.completion_tokens}<br>
                            Successful requests: {crew_response.token_usage.successful_requests}<br>
                        </div>
                    """,
                    unsafe_allow_html=True,
                )

            # End AgentOps session
            agentops.end_session(end_state="Success")


# Run the app
if __name__ == "__main__":
    main()
