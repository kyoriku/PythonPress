# format date to MM/DD/YY
def format_date(date):
  month_names = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
  }
  return f"{month_names[date.month]} {date.day}, {date.year}"

# format URL to remove http, https, www, and query strings
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# pluralize word based on amount
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word