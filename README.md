#### CRDSS

CRDSS which stands for Crop Rotation Decision Support System

and it is a system towards prediction the best crop rotation 

patter in order to maxime the overall yield.

#### Installation / deployment steps

1. Requirements
  * Docker installed locally : <a href="https://docs.docker.com/engine/install/" target="_blank"> Click here for mode details </a>
  * Node Js and NPM installed locally: <a href="https://nodejs.org/en/download"  target="_blank"> Click here for more details </a>
  * Google gemini API key: <a href="https://ai.google.dev/gemini-api/docs/api-key"  target="_blank"> Click here for more details </a>
  
    edit the environment file found at <a href="/backend/utils/.env.template">/backend/utils/.env.template</a>, change the file name
    from ```.env.template``` to ```.env```</a> and replace it content by providing your personal API KEY.
2. Deploy the backend

  * run the following command at the root the the project:

    ```docker compose build```

    ```docker compose up -d```
    
    now the backend will be available and running at 
    <a href="http://localhost:8000/docs" target="_blank">http://localhost:8000/docs</a>


  * the frontend should the be up and running at <a href="http://localhost:3000" target="_blank">http://localhost:3000</a>


#### Data collection

##### Scrapping

The scrapping script was use to download scientific articles from published literature, for further data extraction from these documents. 

  * Navigate to <a href="/backend/utils/">backend/</a>
  * Create virtual environment and install dependencies by using the following commands:

  ```python3 -m venv venv```

  Linux: ```source venv/bin/activate``` 

  Windows: ```./venv/Scripts/activate.sh```

  * Navigate to <a href="/backend/utils/">backend/utils/</a>

  ```cd /backend/utils/```

  * Run the following command the get the PDF documents from the internet

  ```python3 scrap_articles.py```
  
  All the downloaded files can be found in <a href="/backend/pdfs/">/backend/pdfs/</a>


##### Text Extraction from PDF

  * Ensure you are in <a href="/backend/utils/">backend/utils/</a>

  * Run the following command:

  ```python3 pdf_text_extraction.py```

  All the extraction outputs can be found in <a href="/backend/text_extractions/">/backend/text_extractions/</a>


##### Crop Rotation Knowledge extraction from text

Harnessing the capability of large language models, precisely 
Gemini model from Google, we define function to extraction knowledge triples and filter them from text. This process
is essential is building the dataset for model training.
To perfom this action you can run the following command:

```python3 extract_data.py```

All the extraction outputs can be found in <a href="/backend/json_extractions/">/backend/json_extractions/</a>

  
#### Prediction model

The trained ai model is stored in the <a href="/backend/model/">/backend/model/</a>.