from crewai import Task


class UnbiasedNewsTasks:
    def get_media_providers_task(self, agent, selected_country):
        """
        Returns a Task that will get all media providers you can find in the given country.

        The Task will return a JSON object representing an array of objects as follows:
        [{"name": "Media Provider 1"}, {"name": "Media Provider 2"}]
        The Task will get all media providers you can find in the given country.
        At least 20 media providers should be returned.
        The number of all results should be equally divided into left, center and right media providers.
        So, 33.33% should be left, 33.33% center and 33.33% right media providers.

        :param agent: The Agent to which the Task should be assigned.
        :return: The Task.
        """

        return Task(
            description=f"Get all media providers you can find in {selected_country}. At least 20 media providers should be returned. The number of all results should be equally divided into left, center and right media providers. So, 33.33% should be left, 33.33% center and 33.33% right media providers.",
            expected_output='JSON representing an array of objects as follows: [{"name": "Media Provider 1"}]',
            agent=agent,
        )

    def get_media_provider_web_domain_task(self, agent):
        """
        Returns a Task that will get the domain for the given media provider.

        The Task will return the domain for the given media provider.

        :param agent: The Agent to which the Task should be assigned.
        :return: The Task.
        """

        return Task(
            description="Get the domain for the given media provider.",
            expected_output='JSON representing an array of objects as follows: [{"domain": "https://www.mediaprovider1.com"}]',
            agent=agent,
        )

    def get_media_provider_written_content_urls_task(self, agent, topic):
        """
        Returns a Task that will get multiple URLs of written content from multiple media providers on the given topic.

        The Task will return a JSON object representing an array of objects as follows:
        [{"news_urls":["https://www.mediaprovider1.com/news_1","https://www.mediaprovider1.com/news_2","https://www.mediaprovider1.com/news_3","https://www.mediaprovider1.com/news_4","https://www.mediaprovider1.com/news_5"]}]

        The Task will get multiple URLs of written content from multiple media providers on the given topic.
        Skip all non-written URLs. If you get a video URL (e.g., YouTube URL) or image URL, skip it.
        In the end, you should have multiple URLs of written content per media provider and multiple media providers.
        When using the search tool never search for multiple media providers at the same time, but only one at a time.

        :param agent: The Agent to which the Task should be assigned.
        :param topic: The topic for which to get the URLs of written content.
        :return: The Task.
        """

        return Task(
            description=f"Get multiple URLs of written content from multiple media providers on the following topic: {topic}. Skip all non-written URLs. If you get a video URL (e.g., YouTube URL) or image URL, skip it. In the end, you should have multiple URLs of written content per media provider and multiple media providers. When using the search tool never search for multiple media providers at the same time, but only one at a time.",
            expected_output='JSON representing an array of objects as follows: [{"news_urls":["https://www.mediaprovider1.com/news_1","https://www.mediaprovider1.com/news_2","https://www.mediaprovider1.com/news_3","https://www.mediaprovider1.com/news_4","https://www.mediaprovider1.com/news_5"]}]',
            agent=agent,
        )

    def get_written_content_from_url_task(self, agent):
        """
        Returns a Task that will get all written content for the given content URL.

        The Task will return a JSON object representing an array of objects as follows:
        [{"news_content":["This is content from the news 1.","This is content from the news 2.","This is content from the news 3.","This is content from the news 4.","This is content from the news 5."]}]

        The Task will get all written content for the given content URL.
        Don't summarize it, just take it all.
        Do this for every content URL.

        :param agent: The Agent to which the Task should be assigned.
        :return: The Task.
        """

        return Task(
            description="Get all written content for the given content URL. Don't summarize it, just take it all. Do this for every content URL.",
            expected_output='JSON representing an array of objects as follows: [{"news_content":["This is content from the news 1.","This is content from the news 2.","This is content from the news 3.","This is content from the news 4.","This is content from the news 5."]}]',
            agent=agent,
        )

    def get_unbiased_news_task(self, agent):
        """
        Returns a Task that will get all written content from multiple media providers for the given topic and make an unbiased version of the news.

        The Task will return a Markdown string representing an unbiased version of the news.
        The Task will get all written content from multiple media providers for the given topic and make an unbiased version of the news.
        You have a lot of content so make a very detailed and long unbiased version of the news. Don't waste any content. Don't be afraid of making a long article. I want to know everything.
        If different media providers have different views on the same topic, then write both sides of the news mentioning the media provider.
        Always, remember, always refer to the media provider that is mentioned in the news.
        For example: "Media provider 1 says about the topic x while media provider 2 says about the topic y.".
        That way the reader can get the whole picture from both left, centered and right media providers on the same topic.
        At the bottom, add the 'Sources' section where you list all content URLs that were used to write the unbised version of the news as follows: - Media provider: https://www.mediaprovider1.com/news_1

        :param agent: The Agent to which the Task should be assigned.
        :return: The Task.
        """

        return Task(
            description="""
                Collect and analyze all written content from multiple media providers on the given topic to create a comprehensive, unbiased news article. 
                Ensure the final version is highly detailed and thorough, incorporating all available content without omitting any relevant information. 
                Do not hesitate to make the article long; the goal is to provide a full, nuanced picture of the topic.

                When different media providers present contrasting views on the same subject, include both perspectives clearly, mentioning the media provider for each viewpoint. 
                For instance, you might write: 'Media provider 1 reports X on the topic, while media provider 2 states Y.' 
                This ensures readers can understand the entire spectrum of opinions, from left-leaning, right-leaning, and centrist sources.

                Always reference the media provider for any content you include.

                At the end of the article, create a 'Sources' section listing all the content URLs used in the report, formatted as: 
                - Media Provider: https://www.mediaprovider1.com/news_1
            """,
            expected_output="Markdown",
            agent=agent,
        )
