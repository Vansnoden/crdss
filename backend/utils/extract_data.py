# -*- coding: utf-8 -*-

import google.generativeai as genai
import json, os, re, ast, time, math
from typing import List
from os.path import expanduser

API_KEY = "AIzaSyBpTs8NRgOrtj1MD0E8-8r4PwXfELAbp3o"

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
    with open("llm_pipeline_data/gemini_results.txt", "w+") as f:
        f.write(response.text)
    with open("llm_pipeline_data/gemini_results.txt", "r") as f:
        txt = f.read()
        res = extract_triplet_from_text(txt)
    # with open(str(output_path), "w+") as f:
    #     f.write(json.dumps(res))
    with open(f"{output_path}", "w+", encoding='utf-8') as g:
        json.dump(res, g, ensure_ascii=False, indent=4)
    execution_time = time.time() - start_time
    return math.ceil(execution_time)
