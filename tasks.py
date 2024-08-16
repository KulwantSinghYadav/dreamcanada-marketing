from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
	def instagram_ad_copy_from_news(self, agent, product_summary, topic):
		return Task(description=dedent(f"""\
			Craft an engaging Instagram post copy.
			The copy should be informative, concise,
			and updating users with the news through the instagram post.
			
			This is the product you are working with: {product_summary}.
			This is the topic you are working with: {topic}.

			The news report summary has to be pulled from others tasks and agents.

			Focus on creating a message that resonates with
			the target audience and informative about the latest news article in context.

			Your ad copy should encourage viewers to take action, whether it's
			visiting the website, making a purchase, or learning
			more about the product.

			Your final answer MUST be 3 options for each news article along with the url for news article 
			and three ad copy for instagram for each that
			not only informs but also excites and persuades the audience.
			"""),
			agent=agent
		)
	


	def find_news_articles_summary_for_topic_task(self, agent, topic, product_description):
		return Task(description=dedent(f"""\
			You are worikng to find the latest news for the given topic and summarizing them, 
			you have the following topic provided by user: {topic}

			Serach internet with the exact topic provided by user.
			
			Scrape the url pages in the search results.
			
			Sysntesize only latest news related to the product. Ignore blogs and reports.
			you have the following product provided by user: {product_description}

			If the url scrapping fails, Use Snippet form internet search tool.

			Your final answer must be 3 options of news article, each with 1 paragraph
			describing summarizing the report along with the url for news article.
			"""),
			agent=agent
		)