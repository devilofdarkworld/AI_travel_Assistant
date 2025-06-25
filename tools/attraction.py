import wikipedia
from langchain.tools import tool

@tool
def get_attractions(destination: str) -> str:
    """
    Fetches top tourist attractions dynamically using Wikipedia search and summary.
    """
    try:
        # Search for "Tourist attractions in {destination}"
        query = f"Tourist attractions in {destination}"
        search_results = wikipedia.search(query)

        if not search_results:
            return f"No attraction data found for {destination}."

        # Use the top result
        page = wikipedia.page(search_results[0])
        summary = wikipedia.summary(page.title, sentences=3)

        return f"Top attractions in {destination}:\n{summary}"

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found for {destination}, be more specific. Example: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for attractions in {destination}."
    except Exception as ex:
        return f"An error occurred while fetching attractions: {str(ex)}"
    
