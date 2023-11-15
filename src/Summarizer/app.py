import click

from PyPDF2 import PdfReader
from transformers import pipeline


import bs4
import re
import requests


summarizer = pipeline('summarization',model = 'facebook/bart-large-cnn')
token_len = 1024
max_len = 5 #percent of original article


#@click.command()
#@click.argument('article',nargs=1,type=click.Path())
#@click.option('--is_url',is_flag=True,help='Article is an url.')
def summarize_article(article,is_url):
    body_text = ''
    
    if is_url:
        body_text = collect_text(article) #extract article from the url
        fid = article
    else:
        fid = article.split('/')[-1][:-4] + '.txt'
        reader = PdfReader(article) #extract article from pdf
        for p in reader.pages:
            body_text += p.extract_text()
            
    #percentage of total text, divided by the number of subqueries we do of the model so that the total of all queries adds up to expected total length
    max_len = round( max_len/100 * token_len)
    
    text_summary = ''     
    for ind in range(0,len(body_text),token_len): #model has max 1024 tokens, so split into sections to analyze
        text_summary += summarizer(body_text[ind : ind + token_len], max_length = max_len, min_length = round(max_len*.1) )[0]['summary_text']
    
    with open(f'summaries/{fid}','w') as _f:
        _f.write(text_summary)
    
def collect_text(url):
        soup = requests.get(url).text
        soup = bs4.BeautifulSoup(soup,'html.parser`')
    
    
    