from urllib2 import Request, urlopen

values = """
  {
    "image": "https://i.imgur.com/nCHPfi8.jpg",
    "gallery_name": "sampics",
    "subject_id": "samPics"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': '39828e12',
  'app_key': '9fa4851021c0c06ba941a932b0408131'
}
request = Request('https://api.kairos.com/verify', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body