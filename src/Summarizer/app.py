from transformers import pipeline

import click

import PyPDF2 import PdfReader

import bs4
import re
import requests



summarizer = pipeline('summarization',model = 'faceboook/bart-large-cnn')
token_len = 1023


@click.command()
@click.argument('article',nargs=1,type=click.Path())
@click.option('--is_url',is_flag=True,help='Article is an url.')
def summarize_article(article,is_url):
    body_text = ''
    
    if is_url:
        body_text = collect_text(article) #extract article from the url
    else:
        reader = PdfReader(article) #extract article from pdf
        for p in reader.pages:
            body_text += p.extract_text()
    
    text_summary = ''     
    for ind in range(0,len(body_text),token_len): #model has max 1024 tokens, so split into sections to analyze
        text_summary += summarizer(article[ind : ind + token_len])
    
    with fopen(f'summaries/{article}','w') as _f:
        _f.write(text_summary)
    _f.close()
    
def collect_text(url):
        soup = requests.get(url).text
        soup = bs4.BeautifulSoup(soup,'html.parser`')
    