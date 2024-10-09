# format date to MM/DD/YY
def format_date(date):
  return date.strftime('%m/%d/%y')

# format URL to remove http, https, www, and query strings
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# pluralize word based on amount
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word