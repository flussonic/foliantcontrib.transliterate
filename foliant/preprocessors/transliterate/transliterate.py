'''
Relocate files according to their transliterated title
'''

from pathlib import PosixPath, Path

import os.path
import re
from transliterate import translit
from slugify import slugify

from foliant.preprocessors.utils.combined_options import (CombinedOptions, Options,
                                                          boolean_convertor)
from foliant.preprocessors.utils.preprocessor_ext import (BasePreprocessorExt,
                                                          allow_fail)




class Preprocessor(BasePreprocessorExt):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.logger = self.logger.getChild('transliterate')
    self.logger.debug(f'Preprocessor inited: {self.__dict__}')
    self.rename = dict()


  def convert(self, chapters):
    for i,chapter in enumerate(chapters):
      if type(chapter) is dict:
        k1 = list(chapter.keys())[0]
        self.convert(chapter[k1])
      elif chapter == "index.md":
        True
      else:
        parts = re.sub("\\.md$","",chapter).split("/")
        parts2 = []
        while len(parts) > 0:
          s = self.slug("/".join(parts))
          orig = parts.pop()
          if s:
            parts2.insert(0, s)
          else:
            parts2.insert(0, orig)

        self.rename[chapter] = "/".join(parts2)+".md"
        chapters[i] = self.rename[chapter]



  def apply(self):
    self.convert(self.config['chapters'])
    for old in self.rename:
      new = self.rename[old]
      if new != old:
        (Path(self.working_dir) / new).parent.mkdir(parents=True,exist_ok=True)
        os.rename(Path(self.working_dir) / old, Path(self.working_dir) / new)
    self.logger.info('Preprocessor applied')

  def slug(self, chapter):
    header_pattern = re.compile(r'^# (?P<heading>.+?)(?P<customid>\{\#\S+\})?\s*$', re.MULTILINE)

    path1 = Path(self.working_dir) / chapter
    path2 = str(path1)+".md"
    if os.path.isfile(path1):
      path = path1
    elif  os.path.isfile(path2):
      path = path2
    else:
      return None

    with open(path, encoding='utf8') as f:
      chapter_source = f.read()

    for header in header_pattern.finditer(chapter_source):
      heading = header.group('heading')
      heading2 = slugify(translit(heading, "ru", reversed=True))
      return heading2


