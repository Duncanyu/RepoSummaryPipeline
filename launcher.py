from datetime import datetime

from brave_search import search
from github import get_git, get_name
from filesystem import save, load
from playwright_scrape import scrape
from sequential import think

#CHANGE personal.personal TO config
from personal.personal import BRAVE_API_KEY, GITHUB_TOKEN, SAVE_DIR, GPT_API, GPT_MODEL

query = input("Query: ")
github_links = search(query, BRAVE_API_KEY, 10)

repo_data_list = []

if github_links:
    for url in github_links:
        print(f"Fetching Info for {url}... {github_links.index(url) + 1}/{len(github_links)}")
        data = get_git(url, GITHUB_TOKEN)
        if data:
            repo_data_list.append(data)
            
        print(f"Fetching README for {url}... {github_links.index(url) + 1}/{len(github_links)}")
        readme = scrape(url, get_name(url))
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    fname = f"repos_{timestamp}.json"
    save(repo_data_list, fname, SAVE_DIR)
    print(f"Saved to {SAVE_DIR}repos_{timestamp}.json")
else:
    print("Nothing found.")

print(think(GPT_API, repo_data_list[0], GPT_MODEL, readme[1]))