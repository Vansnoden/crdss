# -*- coding: utf-8 -*-

import google.generativeai as genai
import json, os, re, ast, time, math
from typing import List
from os.path import expanduser
from tqdm import tqdm
from utils.common import walkpath_get_files
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def extract_triplet_from_text(text:str) -> List[tuple]:
    res = []
    pattern = r"\(.+.,.+.,.+.\)"
    matches = re.findall(pattern, text)
    for match in matches:
        res.append(tuple(refined_tuple(match)))
    return res

def refined_tuple(triple:str) -> list:
    triple = triple.replace('(', '')
    triple = triple.replace(')', '')
    triple = triple.split(',')
    if len(triple) > 3:
        for i in list(range(len(triple) - 3)):
            triple[2] = triple[2] + triple[i+2]
    triple = triple[:3]
    return triple

def extract_triple_with_gemini(txt, output_path):
    start_time = time.time()
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    instruction = """ Extract knowledge triples from the following text: {text}"""
    response = model.generate_content(instruction.format(text=txt))
    with open("../json_extractions/gemini_results.txt", "w+") as f:
        f.write(response.text)
    with open("../json_extractions/gemini_results.txt", "r") as f:
        txt = f.read()
        res = extract_triplet_from_text(txt)
    with open(f"{output_path}", "w+", encoding='utf-8') as g:
        json.dump(res, g, ensure_ascii=False, indent=4)
    execution_time = time.time() - start_time
    return math.ceil(execution_time)


def test_extraction():
    sample_txt = """
        Malaria is a mosquito-borne infectious disease that affects vertebrates and Anopheles mosquitoes.[6][7][3] Human malaria causes symptoms that typically include fever, fatigue, vomiting, and headaches.
        [1][8] In severe cases, it can cause jaundice, seizures, coma, or death.[1][9] Symptoms usually begin 10 to 15 days after being bitten by an infected Anopheles mosquito.[10][4] If not properly treated, 
        people may have recurrences of the disease months later.[3] In those who have recently survived an infection, reinfection usually causes milder symptoms.[1] This partial resistance disappears over months 
        to years if the person has no continuing exposure to malaria.[1] The mosquito vector is itself harmed by Plasmodium infections, causing reduced lifespan.[11]
        Human malaria is caused by single-celled microorganisms of the Plasmodium group.[10] It is spread exclusively through bites of infected female Anopheles mosquitoes.[10][12] The mosquito bite introduces 
        the parasites from the mosquito's saliva into a person's blood.[3] The parasites travel to the liver, where they mature and reproduce.[1] Five species of Plasmodium commonly infect humans.[10] The three 
        species associated with more severe cases are P. falciparum (which is responsible for the vast majority of malaria deaths), P. vivax, and P. knowlesi (a simian malaria that spills over into thousands of 
        people a year).[13][14] P. ovale and P. malariae generally cause a milder form of malaria.[1][10] Malaria is typically diagnosed by the microscopic examination of blood using blood films, or with 
        antigen-based rapid diagnostic tests.[1] Methods that use the polymerase chain reaction to detect the parasite's DNA have been developed, but they are not widely used in areas where malaria is common, 
        due to their cost and complexity.[15]
        The risk of disease can be reduced by preventing mosquito bites through the use of mosquito nets and insect repellents or with mosquito-control measures such as spraying insecticides and draining 
        standing water.[1] Several medications are available to prevent malaria for travellers in areas where the disease is common.[3] Occasional doses of the combination medication sulfadoxine/pyrimethamine 
        are recommended in infants and after the first trimester of pregnancy in areas with high rates of malaria.[3] As of 2023, two malaria vaccines have been endorsed by the World Health Organization.[16] 
        The recommended treatment for malaria is a combination of antimalarial medications that includes artemisinin.[17][18][1][3] The second medication may be either mefloquine, lumefantrine, or 
        sulfadoxine/pyrimethamine.[19] Quinine, along with doxycycline, may be used if artemisinin is not available.[19] In areas where the disease is common, malaria should be confirmed if possible 
        before treatment is started due to concerns of increasing drug resistance.[3] Resistance among the parasites has developed to several antimalarial medications; for example, chloroquine-resistant 
        P. falciparum has spread to most malarial areas, and resistance to artemisinin has become a problem in some parts of Southeast Asia.[3]
        The disease is widespread in the tropical and subtropical regions that exist in a broad band around the equator.[20][1] This includes much of sub-Saharan Africa, Asia, and Latin America.[3] In 2022, 
        some 249 million cases of malaria worldwide resulted in an estimated 608,000 deaths, with 80 percent being five years old or less.[21] Around 95% of the cases and deaths occurred in sub-Saharan Africa. 
        Rates of disease decreased from 2010 to 2014, but increased from 2015 to 2021.[18] According to UNICEF, nearly every minute, a child under five died of malaria in 2021,[22] and "many of these deaths 
        are preventable and treatable".[23] Malaria is commonly associated with poverty and has a significant negative effect on economic development.[24][25] In Africa, it is estimated to result in losses 
        of US$12 billion a year due to increased healthcare costs, lost ability to work, and adverse effects on tourism.[26] The malaria caseload in India was slashed by 69 per cent from 6.4 million 
        (64 lakh) in 2017 to two million (20 lakh) in 2023. Similarly, the estimated malaria deaths decreased from 11,100 to 3,500 (a 68-per cent decrease) in the same period.[27] 
    """
    execution_time = extract_triple_with_gemini(sample_txt, "llm_pipeline_data/gemini_results.json")
    print(f"extraction completed in: {execution_time} s")


def extract_from_file(filepath:str) -> bool:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            fname = os.path.basename(filepath).split('.')[0]
            res = extract_triple_with_gemini(text, f"../json_extractions/{fname}.json")
            with open("../json_extractions/execution_time_summary.csv", "a+") as g:
                g.write(f"\n{res},{fname}")
            return True
    except Exception as e:
        with open(filepath, 'r', encoding='latin-1') as f:
            text = f.read()
            fname = os.path.basename(filepath).split('.')[0]
            res = extract_triple_with_gemini(text, f"../json_extractions/{fname}.json")
            with open("../json_extractions/execution_time_summary.csv", "a+") as g:
                g.write(f"\n{res},{fname}")
            return True
    return False 


def extract_from_folder(parent_folder:str):
    files = walkpath_get_files(parent_path=parent_folder, extension=".txt")
    for filepath in tqdm(files):
        extract_from_file(filepath)
    return True



if __name__ == '__main__':
    parent_folder = "../text_extractions"
    res = extract_from_folder(parent_folder)
