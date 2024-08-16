import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html

from newspaper import Article

#from langchain.llms import Ollama

class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content, just pass a string with
    only the full url, no need for a final slash `/`, eg: https://google.com or https://clearbit.com/about-us"""
    # url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    # payload = json.dumps({"url": website})
    # headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    # response = requests.request("POST", url, headers=headers, data=payload)
    # elements = partition_html(text=response.text)
    # content = "\n\n".join([str(el) for el in elements])
    # content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    summaries = []


    #USE ARTICLE FOR SCRAPPING
    title = []
    text = []
    url=website
    # We scrape the news site to collect the content over there
    if url:
        article = Article(url)
        article.download()
        article.parse()
        title.append(article.title)
        text.append(article.text)
        content_new = [text[i:i + 8000] for i in range(0, len(text), 8000)]

    #print(f'\nScrapped Content raw: {content_new}\n')





    for chunk in content_new:
      agent = Agent(
          role='Principal Researcher',
          goal=
          'Do amazing researches and summaries based on the content you are working with',
          backstory=
          "You're a Principal Researcher at a big company and you need to do a research about a given topic.",
          #llm=Ollama(model=os.environ['MODEL']),
          allow_delegation=False)
      task = Task(
          agent=agent,
          description=
          f'Analyze and make a LONG summary the content bellow, make sure to include the ALL relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
      )
      summary = task.execute()
      summaries.append(summary)
      content_new = "\n\n".join(summaries)
      print(f'\nScrapped Content formatted: {content_new}\n')
    return f'\nScrapped Content: {content_new}\n'

# # Instantiate the class
# browser_tools = BrowserTools()

# # Call the method with a URL
# website_url = f"https://www.cp24.com/news/mounting-condo-inventories-could-put-downward-pressure-on-toronto-s-real-estate-market-report-1.6997431" # Replace with the actual URL you want to scrape
# browser_tools.scrape_and_summarize_website(website_url)