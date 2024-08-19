import os
from textwrap import dedent
from crewai import Agent
from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from langchain.agents import load_tools

from langchain.llms import Ollama

class MarketingAnalysisAgents:
	def creative_content_creator_agent_from_article(self):
		return Agent(
			role="Creative Content Creator",
			goal=dedent("""\
				Develop compelling and innovative content
				for social media campaigns, with a focus on creating
				high-impact Instagram ad copies."""),
			backstory=dedent("""\
				As a Creative Content Creator at a top-tier
				digital marketing agency, you excel in crafting narratives
				that resonate with audiences on social media.
				Your expertise lies in taking a topic, search for the laterst news articles,
				create a summary and from the summary creating 
				engaging content that informs customers about the news and capture
				attention and inspire action."""),
			tools=[
					BrowserTools.scrape_and_summarize_website,
					SearchTools.search_internet,
					SearchTools.search_instagram
			],
			#llm=self.llm,
			verbose=True
		)
	
	def senior_photographer_agent(self):
		return Agent(
				role="Senior Photographer",
				goal=dedent("""\
					Take the most amazing photographs for instagram ads that
					capture emotions and convey a compelling message."""),
				backstory=dedent("""\
					As a Senior Photographer at a leading digital marketing
					agency, you are an expert at taking amazing photographs that
					inspire and engage, you're now working on a new campaign for a super
					important customer and you need to take the most amazing photograph."""),
				tools=[
					SearchTools.search_internet,
					SearchTools.search_instagram,
					SearchTools.search_images
				],
				#llm=self.llm,
				allow_delegation=False,
				verbose=True
		)

	def chief_creative_diretor_agent(self):
		return Agent(
				role="Chief Creative Director",
				goal=dedent("""\
					Oversee the work done by your team to make sure it's the best
					possible and aligned with the product's goals, review, approve,
					ask clarifying question or delegate follow up work if necessary to make
					decisions"""),
				backstory=dedent("""\
					You're the Chief Content Officer of leading digital
					marketing specialized in product branding. You're working on a new
					customer, trying to make sure your team is crafting the best possible
					content for the customer."""),
				tools=[
					SearchTools.search_internet,
					SearchTools.search_instagram,
					SearchTools.search_images
				],
				#llm=self.llm,
				verbose=True
		)
