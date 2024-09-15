import streamlit as st


def main():
    """
    The main function for the Home page.

    This function sets up the Streamlit page configuration, retrieves API keys for AIML,
    AgentOps, Exa, and Firecrawl, and stores them in the session state. It also handles
    user input for these API keys, displays warnings if any keys are missing, and controls
    the functionality of the call-to-action button based on the presence of valid keys.
    When all API keys are present and the button is clicked, it redirects the user to the
    News Generator page.

    Key Responsibilities:
        - Configures the Streamlit page settings, including title, icon, and custom sidebar
          elements for enhanced user experience.
        - Retrieves API keys for AIML, AgentOps, Exa, and Firecrawl, either from
          Streamlit secrets or user input, and stores them in the session state for later
          access.
        - Validates the presence of all necessary API keys, disabling the call-to-action button
          if any keys are missing.
        - Renders a sidebar with navigation links to the Home and News Generator pages,
          while ensuring that the button for the News Generator page is enabled only when
          valid API keys are provided.
        - Displays a visually appealing title and subtitle for the application, along with a
          quote emphasizing the importance of seeking truth.
        - Provides a detailed description of CrewNews, highlighting its mission to deliver
          unbiased news by aggregating content from diverse media sources.
        - Displays a warning message if any API keys are not entered, prompting users to
          provide the necessary information.
        - Implements a call-to-action button that, when clicked and valid API keys are present,
          navigates the user to the News Generator page.

    Parameters:
        None

    Returns:
        None
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

    def get_api_key(
        api_provider: str,
        api_name: str,
        placeholder: str,
    ) -> str:
        """
        Retrieves the API key for a given provider, either from Streamlit secrets or user input.

        Parameters:
            api_provider (str): The name of the API provider.
            api_name (str): The key name to access the API key from Streamlit secrets.
            placeholder (str): The placeholder text for the input field.

        Returns:
            str: The API key for the given provider.
        """

        # Check if API key is provided in Streamlit secrets
        if api_name in st.secrets:
            # If yes, use it
            api_key = st.secrets[api_name]
        else:
            # If not, ask user to enter it manually in the sidebar
            api_key = st.sidebar.text_input(
                label=f"#### Set your {api_provider} API key 👇",
                placeholder=placeholder,
                type="password",
            )

        # Store API key in Streamlit session state
        st.session_state[api_name.lower()] = api_key

        # Return API key
        return api_key

    # Retrieve API keys for AIML, AgentOps, Exa, and Firecrawl and store them in Streamlit session state
    st.session_state["aiml_api_key"] = get_api_key(
        api_provider="AIML",
        api_name="AIML_API_KEY",
        placeholder="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )

    st.session_state["agentops_api_key"] = get_api_key(
        api_provider="AgentOps",
        api_name="AGENTOPS_API_KEY",
        placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    )

    st.session_state["exa_api_key"] = get_api_key(
        api_provider="Exa",
        api_name="EXA_API_KEY",
        placeholder="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    )

    st.session_state["firecrawl_api_key"] = get_api_key(
        api_provider="Firecrawl",
        api_name="FIRECRAWL_API_KEY",
        placeholder="fc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )

    # Check if all API keys are stored in Streamlit session state
    if (
        not st.session_state["aiml_api_key"]
        or not st.session_state["agentops_api_key"]
        or not st.session_state["exa_api_key"]
        or not st.session_state["firecrawl_api_key"]
    ):
        # If not, disable CTA button
        button_disabled_status = True

        # Render sidebar
        with st.sidebar:
            # Render divider
            st.divider()
    else:
        # If yes, enable CTA button
        button_disabled_status = False

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
            disabled=button_disabled_status,
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
    col_left, col_middle, col_right = st.columns(spec=[0.1, 0.8, 0.1])

    # Render middle column
    with col_middle:
        # Render quote
        st.markdown(
            body="""
                :blue-background[In seeking truth you have to get both sides of a story. – Walter Cronkite]
            """,
            unsafe_allow_html=True,
        )

    # Render description
    st.markdown(
        body="""
            Introducing CrewNews, your AI news generator powered by Llama 3.1, AIML, CrewAI, AgentOps, Exa, and Firecrawl. Developed for the <a href="https://lablab.ai/event/ai-agents-hack-with-lablab-and-mindsdb">LabLab September 2024 hackathon</a>, CrewNews delivers an unbiased version of the news for a given question or topic by combining content from media providers from the United States across the political spectrum.
        
            Biases in news reporting can distort public perception, leading to a skewed understanding of important issues and events. When media outlets present information from a single perspective, they risk creating echo chambers where only certain viewpoints are amplified while others are silenced. This not only undermines the integrity of journalism but also affects how individuals form opinions and make decisions based on incomplete information.
            
            CrewNews addresses this critical issue by actively sourcing and presenting content from a diverse range of media providers from the United States, ensuring that multiple perspectives are represented in each report. By utilizing advanced AI technologies, CrewNews fosters a more balanced discourse, empowering users to hear all sides of the story for a given topic and come closer to the truth.
        """,
        unsafe_allow_html=True,
    )

    # Check if all API keys are provided
    if (
        not st.session_state["aiml_api_key"]
        or not st.session_state["agentops_api_key"]
        or not st.session_state["exa_api_key"]
        or not st.session_state["firecrawl_api_key"]
    ):
        # If not, display warning
        st.warning(
            body="Please enter your AIML, AgentOps, Exa, and FireCrawl API keys in the sidebar.",
            icon="⚠️",
        )

    # Initalize columns for layout
    col_left, col_middle, col_right = st.columns(3)

    # Render middle column
    with col_middle:
        # Render CTA button
        cta_button = st.button(
            label="Start using CrewNews 🚀",
            type="primary",
            use_container_width=True,
            disabled=button_disabled_status,
        )

    # If CTA button is clicked and all API keys are stored in Streamlit session state, switch to the next page
    if (
        cta_button
        and st.session_state["aiml_api_key"]
        and st.session_state["agentops_api_key"]
        and st.session_state["exa_api_key"]
        and st.session_state["firecrawl_api_key"]
    ):
        st.switch_page(page="pages/2_News_Generator.py")


# Run the app
if __name__ == "__main__":
    main()
