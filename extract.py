from newspaper import Article

def truncate(s, length):
  s = s.strip()
  s = s[:length]
  s = s.rstrip()
  return s

def retrieve_text(url, max_body_length=4000):
  ''' Returns (title, body), each being a string.
  If fails for whatever reason, returns None.

  '''
  article = Article(url=url)
  article.download()
  article.parse()
  title = article.title
  body = article.text
  if (title, body) != (u'', u''):
    body = truncate(body, max_body_length)
    return (title, body)

def test_retrieve_text():
  urls = [
    'https://techcrunch.com/2017/02/11/2017-the-year-your-startup-gets-funded/',
    'https://arstechnica.com/tech-policy/2017/02/oracle-refuses-to-accept-pro-google-fair-use-verdict-in-api-battle/',
    'http://www.theglobeandmail.com/news/world/us-politics/with-refugee-ban-on-hold-trump-vows-action-very-rapidly-to-protect-us/article33983461/'
    'foo',
  ]
  for url in urls:
    print url
    print retrieve_text(url, 400)
    print
