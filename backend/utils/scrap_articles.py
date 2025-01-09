# -*- coding: utf-8 -*-

import pandas as pd
import os

def getPDFsFromDOIs():
    pubmed_data = pd.read_csv("./pubmed_search_res.csv")
    clean_dois = pubmed_data["DOI"].dropna().to_list()
    for doi in clean_dois:
        os.system(f"""python3 -m PyPaperBot --query=\"{doi}\" --scholar-pages=1  --min-year=1900 --dwn-dir=\"../pdfs\" --scihub-mirror=\"https://sci-hub.se\"""")


if __name__ == "__main__":
    getPDFsFromDOIs()