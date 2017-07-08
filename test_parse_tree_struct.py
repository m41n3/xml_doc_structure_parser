import os

import logging

from tree_builder import TreeBuilder

# set up logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(os.path.abspath(__file__))  # os.getcwd()


# set up grammar and test data

DOC_STRUCT_SYNTAX1 = {
    'LINE_PREFIX': r'\|-',  # escape pipe with backslash for regexp
    'INDENT': '-',
    'NAME_SEPARATOR': '> ',
    'VALUE_SEPARATOR': r''
}

DOC_STRUCT_SYNTAX2 = {
    'LINE_PREFIX': r'',
    'INDENT': '  ',
    'NAME_SEPARATOR': '',
    'VALUE_SEPARATOR': r'\s+'
}

DOC_STRUCT_SYNTAX3 = {
    'LINE_PREFIX': r'',
    'INDENT': r'\t',
    'NAME_SEPARATOR': '',
    'VALUE_SEPARATOR': r'\s+'
}

doc1 = """|-> L1
|--> L2
|---> L3
|----> L4
|---> L3
|----> L4"""

doc2 = """World
  Continent       Europe
    Country       France
      Capital     Paris
    Country       Germany
      Capital     Berlin"""

# doc 3 is copy-pasted directly from Excel from a structure where element names are in
# columns A, B, C, D and element values are in column F
doc3 = """
World					
	Continent				Europe
		Country			France
			Capital		Paris
		Country			Germany
			Capital		Berlin
"""

# logger.debug(tree_struct)


# load doc 1
tr1 = TreeBuilder(DOC_STRUCT_SYNTAX1)
tree_root = tr1.load(doc1)
logging.info(tree_root.print())

# load doc 2
tr2 = TreeBuilder(DOC_STRUCT_SYNTAX2)
tree_root2 = tr2.load(doc2)
logging.info(tree_root2.print())
logging.info(tree_root2.xmlify())

# load doc 3
tr3 = TreeBuilder(DOC_STRUCT_SYNTAX3)
tree_root3 = tr3.load(doc3)
logging.info(tree_root3.print())
logging.info(tree_root3.xmlify())
