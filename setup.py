from setuptools import setup, find_packages
import os

install_required = [line.strip() for line in open("requirements.txt").readlines()]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'articlesummarizer',
      version = '0.0.1',
      author = 'Gerardo Rodriguez',
      author_email = 'gerardorodore@gmail.com',
      package_dir={'': 'src'},
      packages = ['Summarizer'],
      install_requires = install_required,
      entry_points = {'console_scripts':[
          'summarize_article = src.Summarizer.app:summarize_article',
          ]}
)