<div align="center">
 
# 📰 CrewNews 📰

⚡ Powered by ⚡<br>[Streamlit](https://streamlit.io/) | [Llama 3.1](https://www.llama.com/) | [AIML](https://aimlapi.com/) | [CrewAI](https://www.crewai.com/) | [AgentOps](https://agentops.ai/) | [Exa](https://exa.ai/) | [Firecrawl](https://www.firecrawl.dev/)

Enjoying what you find in this repository? Your star ⭐ would be greatly appreciated!

<br>

</div>

## 📖 Short description 📖

CrewNews is a [Streamlit](https://streamlit.io/) app designed for delivering an unbiased version of the news for a given question or topic by combining content from media providers from the United States across the political spectrum using [Llama 3.1](https://www.llama.com/) as LLM via [AIML](https://aimlapi.com/), [CrewAI](https://www.crewai.com/) for building AI agents, [AgentOps](https://agentops.ai/) for testing AI agents, [Exa](https://exa.ai/) as a web search tool, and [Firecrawl](https://www.firecrawl.dev/) as a web scraping tool.

<br>

## 🧐 Problem addressed 🧐

Biases in news reporting can distort public perception, leading to a skewed understanding of important issues and events. When media outlets present information from a single perspective, they risk creating echo chambers where only certain viewpoints are amplified while others are silenced. This not only undermines the integrity of journalism but also affects how individuals form opinions and make decisions based on incomplete information.

> In seeking truth you have to get both sides of a story. – Walter Cronkite

CrewNews addresses this critical issue by actively sourcing and presenting content from a diverse range of media providers from the United States, ensuring that multiple perspectives are represented in each report. By utilizing advanced AI technologies, CrewNews fosters a more balanced discourse, empowering users to hear all sides of the story for a given question or topic and come closer to the truth.

<br>

## 🚀 Getting started 🚀

### Step 1: Clone repository

Run the following command in the terminal to clone the repository:

```bash
git clone https://github.com/rokbenko/crew-news.git
```

### Step 2: Change directory

Run the following command in the terminal to change the directory:

```bash
cd crew-news
```

### Step 3: Create virtual environment

Run the following command in the terminal to create a virtual environment named `my-venv`:

```bash
python -m venv my-venv
```

> [!TIP]
> You can verify that the virtual environment is created successfully if you see a folder named `my-venv` inside the root directory.

> [!NOTE]
> `venv` is a built-in Python module that allows you to create and manage virtual environments. If you have Python `3.3` or higher installed, you can start using `venv` right away.

### Step 4: Activate virtual environment

Run the following command in the terminal to activate the virtual environment named `my-venv`:

```bash
my-venv/scripts/activate
```

> [!TIP]
> You can verify that the virtual environment is activated successfully if you see `(my-venv)` at the beginning of your terminal prompt, like this:
> 
> ```bash
> (my-venv) C:\your\path\to\crew-news\
> ```

### Step 5: Install requirements

Run the following command in the terminal to install all the required packages:

```bash
pip install -r requirements.txt
```

### Step 6: Set up API keys and add them to the `secrets.toml` file (optional but recommended)

> [!NOTE]
> Setting up all API keys is mandatory. You need your API keys if you want to use CrewNews.
>
> But adding API keys to the `secrets.toml` file is optional. You have two options for how to use your API keys with CrewNews:
>
> - adding them to the `secrets.toml` file, or
> - typing them into the input fields in the CrewNews's sidebar on the Home page.

Inside the `.streamlit` folder, create the `secrets.toml` file that should contain the following secrets:

```bash
AIML_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
AGENTOPS_API_KEY = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
EXA_API_KEY = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
FIRECRAWL_API_KEY = "fc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Step 7: Start Streamlit app

Run the following command in the terminal to start the Streamlit app:

```bash
streamlit run 1_Home.py
```

### Step 8: Access CrewNews in browser

Navigate to [http://localhost:8501](http://localhost:8501) to open CrewNews in the browser.

<br>

## ⚒️ Tech stack ⚒️

- [Python](https://www.python.org/) `3.11.8`
- [Streamlit](https://pypi.org/project/streamlit/) `1.38.0`
- [LangChain Python integration for OpenAI SDK](https://pypi.org/project/langchain-openai/) `0.1.23`
- [CrewAI Python SDK](https://pypi.org/project/crewai/) `0.55.2`
- [AgentOps Python SDK](https://pypi.org/project/agentops/) `0.3.10`
- [Exa Python SDK](https://pypi.org/project/exa-py/) `1.1.0`
- [Firecrawl Python SDK](https://pypi.org/project/firecrawl-py/) `1.2.3`

<br>

## 🤔 How does it work 🤔

1. **Input a question or news topic**

The user begins by entering a specific question or news topic they want to explore. CrewNews uses this input to target media sources relevant to the selected subject, creating a foundation for gathering diverse content from media providers across the United States.

2. **Collecting media providers across the political spectrum**

First, CrewNews activates the *Media Expert* agent to source media outlets representing various political viewpoints—left, center, and right. This ensures the collected content offers a balanced range of perspectives, avoiding bias from any single ideological standpoint.


3. **Retrieving media provider web domains**

After the media providers are gathered, the *Web Domain Expert* agent identifies and retrieves the web domain URLs of the selected media providers.

3. **Searching for written news content**

Once the web domain URLs are obtained, the *Written Content Expert* agent utilizes the Exa tool to search for relevant articles from each media provider’s website. CrewNews focuses solely on written content, filtering out videos or images.

4. **Extracting written content**

Following the retrieval of news URLs, the *Text Extractor Expert* agent uses the Firecrawl tool to scrape the full written content from each news article.

5. **Creating unbiased news**

Last, the *Unbiased Journalist* agent reviews all gathered content, analyzing how each media outlet reports on the same question or topic. By presenting the viewpoints of left, center, and right media outlets, the agent compiles an unbiased article that offers a complete and balanced perspective. Users can see all sides of the story and form more informed opinions, free from skewed narratives.

<br>

## 🎭 Behind the sceenes 🎭

### CrewAI architecture

CrewNews is built on a modular architecture that employs a crew of specialized AI agents using the CrewAI framework. Each agent is designed to handle specific tasks within the news generation pipeline, allowing for efficient and systematic processing of information.

### Agents

- *Media Expert* agent: This agent is responsible for sourcing media providers across the political spectrum (left, center, and right) from the United States. It ensures that the collected content reflects a diverse range of perspectives, mitigating the risks of bias.
- *Web Domain Expert* agent: This agent retrieves the web domain URLs of each outlet. It ensures that subsequent content extraction processes are performed on valid and accessible websites.
- *Written Content Expert* agent: This agent utilizes the Exa tool to search for relevant written articles from each media provider’s website. It focuses exclusively on text-based content to maintain analytical consistency.
- *Text Extractor Expert* agent: This agent employs the Firecrawl tool to scrape the full written content from the identified URLs. It ensures that comprehensive textual data is collected for analysis.
- *Unbiased Journalist* agent: This agent synthesizes the collected content, analyzing how different media outlets report on the same question or topic. It generates an unbiased article that encompasses all viewpoints.

### Tasks

- *Get Media Providers* task: Assigned to the *Media Expert* agent, this task specifies the requirement to collect a balanced number of media outlets from across the political spectrum.
- *Get Media Provider Web Domain* task: Assigned to the *Web Domain Expert* agent, this task focuses on identifying and retrieving the web domain URLs of the selected media providers.
- *Get Media Provider Written Content URLs* task: Assigned to the *Written Content Expert* agent, this task focuses on searching for and retrieving URLs of relevant written articles.
- *Get Written Content From URL* task: Assigned to the *Text Extractor Expert* agent, this task ensures the extraction of full written content from the gathered URLs.
- *Get Unbiased News* task: Assigned to the *Unbiased Journalist* agent, this task synthesizes the collected content into a coherent and unbiased article, providing a comprehensive perspective on the chosen question or topic.

### Tools

- *Exa* tool: The Exa tool serves as the web search engine, enabling the *Written Content Expert* agent to perform comprehensive web searches for relevant written content across various media provider websites.
- *Firecrawl* tool: The Firecrawl tool is utilized for web scraping, allowing the *Text Extractor Expert* agent to retrieve and parse the HTML content of articles.

<br>

## ⚠️ Limitations ⚠️

- Source URL accuracy: The source URLs included in the final report are usually incorrect. This can lead to `404` errors when users attempt to access the article directly from the source URL.
- Context window limitations: Due to the Llama 3.1 context window limit, longer inputs can sometimes result in the final report being cut off.

Both of these issues could very likely be resolved with further tweaking of the crew of AI agents.

<br>

## ⭐ Star history ⭐

[![Star history chart](https://api.star-history.com/svg?repos=rokbenko/crew-news&type=Date)](https://star-history.com/#rokbenko/crew-news&Date)

<br>

## 🤝 Contributing 🤝

Contributions are welcome! Feel free to [open issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue) or [create pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) for any improvements or bug fixes.

<br>

## 📝 License 📝

This project is open source and available under the [MIT License](https://github.com/rokbenko/crew-news/blob/main/LICENSE).
