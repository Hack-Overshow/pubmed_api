import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

class StudySearch:
    def __init__(self, query="", num=0):
        self.query = '+'.join(query.split(" ")) if query else ""
        self.results_num = num if num else 10  # Default number of results is 10

    def search_to_df(self) -> pd.DataFrame:
        URL = f"https://pubmed.ncbi.nlm.nih.gov/?term={self.query}&size={self.results_num}&filter=simsearch1.fha"
        page = requests.get(URL)
        page_data = BeautifulSoup(page.content, "html.parser")

        search_results = page_data.find_all("article", class_="full-docsum")
        studies_list = self.data_parser(search_results)
        
        return pd.DataFrame(data=studies_list)

    def data_parser(self, search_results) -> list:
        studies = []
        for study_data in tqdm(search_results, desc="Compiling Data"):
            study_title = study_data.find("a", class_="docsum-title").text.strip()
            study_id = study_data.find("a", class_="docsum-title")
            study_authors = study_data.find("div", class_="docsum-citation full-citation").find("span", class_="docsum-authors full-authors").text.strip()
            study_URL = f"https://pubmed.ncbi.nlm.nih.gov{study_id['href']}"
            study_page = BeautifulSoup(requests.get(study_URL).content, "html.parser")
            study_abstract = study_page.find("div", class_="abstract").find_all("p")
            abstract_text = ''
            for section in study_abstract:
                abstract_text += section.text.strip() + "\n"
            study_citation = study_data.find("div", class_="docsum-citation full-citation").find("span", class_="docsum-journal-citation full-journal-citation").text.strip()
            studies.append({"Title": study_title, "Authors": study_authors,
                            "Abstract": abstract_text, "Citation": study_citation,
                            "URL": study_URL})
        return studies
