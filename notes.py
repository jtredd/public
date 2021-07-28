""" some useful ideas """



# not tested
def text_cleaner(source):
  stripped = (line.strip() for lin source)
  partitioned = (line.partitioned("#") for line in stripped)
  decommented = (data.rstrip() for data, sharp, comment in partitioned)
  non_empty   = (line for line in decommented if line)
  return non_empty


"""
>>> data.sort(key=lambda x: int(x[1]))
# sorted() creates list from generator
>>> by_count = sorted(data, key=lambda x: int(x[1]))
"""

"""
>>> wrapped = [(int(x[1]), x) for x in data]
>>> wrapped.sort()
>>> by_count = [x[1] for x in wrapped]
>>>
>>> map(lambda item: (int(x[1]), item), data)
"""


## Exception
"""
>>> obj = Exception("some message", "additional detals")
>>> raise obj
>>>
"""

def clean_number(text):
  try:
    value = float(text)
  except ValueError:
    value = None
  return value

"""
>>> row = ['heading', '23', '2.14']
>>> list(map(clean_number, row))
[None, 23.0, 2.14]
>>>
"""


#import os
def names(path="."):
  try:
    return [name
        for name in os.listdir(path)
        if not name.startswith('.')]
  except OSError as exc:
    print( exc.__class__.__name__, exc )
    raise


# ICO
#
ico_data = b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x00\x00\x18\x00h\x03\x00\x00\x16
\x00\x00\x00'
#import struct
### two-byte have words, single -bytes, four-byte ints
struct.unpack('<hhhbbbbhhii', ico_data[:22])


#import re
def tests_run(log_file):
  """basic regex use-case to find lines with pattern """
  data_pat = re.compile(r"\s*([\w ]+):\s+(\d+\.?\d*)\s*")
  for line in log_file:
    match= data_pat.findall(line)
    if match:
      yield match



# FILE HANDLE
# let's try not to forget how simple this is...lol.
file_in = 'dir/file.txt'
file_out = 'dir/file_out.txt'
with open(file_in) as source, open(file_out, 'w') as target:
  for stats in tests_run(source):
    print(stats, file=target)


# simple GET request with context handler
# import contextlib
# import http.client

with contextlib.closing(http.client.HTTPConnection('www.example.com')) as host:
  host.request('GET', '/url/path/stuff/')
  response= host.getresponse()
  print(response.read())

#from os import walk, path
class diskwalk(object):
  """ API for getting directory walking collections """
  def __init__(self, path):
    self.path = path

  def enumerate_paths(self):
    """ Returns the path to all the files in a directory list """
    path_collection = []
    for dirpath, dirnames, filenames in walk(self.path):
      for file in filenames:
        fullpath = path.join(dirpath, file)
        path_collection.append(fullpath)

    return path_collection


  def enumerate_files(self):
    file_collection = []
    for dirpath, dirnames, filenames in walk(self.path):
      for file in filenames:
        file_collection.append(file)

    return file_collection


  def enumerate_dir(self):
    dir_collection = []
    for dirpath, dirnames, filenames in walk(self.path):
      for dir in dirnames:
        dir_collection.append(dir)

    return dir_collection

"""
>>> dirA = set(listdir('/path/to/dirA')
>>> from diskwalk_api import diskwalk
>>> d = diskwalk('/path/to/dir')
>>> files = d.enumerate_paths()
>>> len(files)
...
>>> dup = []
>>> record = {}
>>> for file in files:
# needs size from 'os.path.getsize'
  compound_key = (getsize(file), create_checksum(file))
  if compound_key in record:
    dup.append(file)
  else:
    record[compound_key] = file

>>> print(dup)
...
"""
#import hashlib
def create_checksum(path):
  """
  Reads in a file. Creates checksum of file line by line.
  Returns complete checksum total for file.
  """
  fp = open(path)
  checksum = hashlib.md5()
  while True:
    buffer = fp.read(8192)
    if not buffer: break
    checksum.update(buffer)
  fp.close()
  checksum = checksum.digest()
  return checksum











from flask import Flask, request
from PIL import Image, ImageDraw, ImageColor
import tempfile

spiral_app = Flask(__name__)

@spiral_app.route('/image/<spec>', methods=('GET',))
def image(spec):
  spec_uq= urllib.parse.unquote_plus(spec)
  spec_dict = urllib.parse.parse_qs(spec_uq)
  spiral_app.logger.info( 'image spec {0!r}'.format(spec_dict))
  try:
    angle= float( spec_dict['angle'][0])
    incr= float(spec_dict['incr'][0])
    size= int( spec_dict['size'][0])
  except Exception as e:
    return make_response('URL {0} is invalid'.format(spec), 403)

  # working di should be under Apache Home.
  _, temp_name = tempfile.mkstemp('.png')

  im = Image.new('RGB', (400, 300), color=ImageColor.getrgb('white'))
  pen = Pen(im)
  spiral(pen, angle=angle, incr=incr, size=size)
  im.save(temp_name, format='png')

  # should redirect so that Apache serves the image.
  spiral_app.logger.debug( ' image file {0!r}'.format(temp_name) )
  with open(temp_name, format='png') as image_file:
    data = image_file.read()
  return (data, 200, {'Content-Type':'image/png'})


if __name__ == '__main__':
  spiral_app.run(debug=True)

