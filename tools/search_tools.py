import json
import os

import requests

import requests
from langchain.tools import tool


class SearchTools():

  @tool("Search internet")
  def search_internet(query):
    """Useful to search the internet about a given topic and return relevant
    results."""
    return SearchTools.search(query)

  @tool("Search instagram")
  def search_instagram(query):
    """Useful to search for instagram post about a given topic and return relevant
    results."""
    query = f"site:instagram.com {query}"
    return SearchTools.search(query)



  def search(query, n_results=5):
    try:
      print("XXXXXXXXXXXXXXXXXXX Internet search call with query: " + query + " XXXXXXXXXXXXXXXXXXXXX")
      
      # Ensure the API key is available
      api_key = os.environ.get('SERPER_API_KEY')
      print(f"Using API Key: {api_key}")
      if not api_key:
          raise ValueError("API key for Serper is not set in environment variables.")
      
      url = "https://google.serper.dev/news"
      payload = json.dumps({
         "q": query,
         "gl": "ca"
         })
      headers = {
        'X-API-KEY': api_key,
        'content-type': 'application/json',
      }

      print("XXXXXXXXXXXXXXXXXXX Making SERPER API CALL  XXXXXXXXXXXXXXXXXXXXX")
      # Make the API request
      response = requests.post(url, headers=headers, data=payload)
      print("XXXXXXXXXXXXXXXXXXX Internet search response: " + str(response) + " XXXXXXXXXXXXXXXXXXXXX")
      
      # Check if the response is successful
      response.raise_for_status()
      
      # Parse the response
      response_data = response.json()
      results = response_data.get('news', [])
      
      print("XXXXXXXXXXXXXXXXXXX Internet search results: " + str(results) + " XXXXXXXXXXXXXXXXXXXXX")
      
      # Process the results
      stirng = []
      for result in results[:n_results]:
          try:
              stirng.append('\n'.join([
                  f"Title: {result.get('title', 'No title')}"
                  f"URL: {result.get('link', 'No URL')}"
                  f"Snippet: {result.get('snippet', 'No snippet')}",
                  "\n-----------------"
              ]))
          except KeyError as e:
              print(f"KeyError: {e} in result: {result}")
      
      content = '\n'.join(stirng)
      return f"\nSearch result:\n{content}\n"
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {str(e)}")
        return f"An error occurred during the API request: {str(e)}"
    except ValueError as ve:
        print(f"Configuration error: {str(ve)}")
        return f"Configuration error: {str(ve)}"
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return f"An unexpected error occurred: {str(e)}"

