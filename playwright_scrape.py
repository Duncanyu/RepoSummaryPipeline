import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def scrape(repo_url, repo_name):
    readme_text = ""

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(repo_url)

        try:
            readme_element = page.query_selector("article.markdown-body")
            if readme_element:
                readme_text = readme_element.inner_text()

                readme_path = Path(f"{repo_name}_README.md")
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_text)
                    print(f"README saved to {readme_path}")
        finally:
            browser.close()

    return readme_text, str(readme_path) if readme_text else None
