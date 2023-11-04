from Summarizer import app

def test_loading_no_url(self):
    in_test = 'article_one'
    out_test = app.article_summarizer(in_test)
    assert out_test == in_test

def test_loading_url(self):
    in_test = 'article_2'
    out_test = app.article_summarizer(in_test,'--is_url')
    assert out_test == in_test + 'is_url'
    
    
