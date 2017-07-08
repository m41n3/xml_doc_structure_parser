import re
import logging

from node import Node

class TreeBuilder:

    def __init__(self, syntax):
        self.syntax = syntax

    def load(self, tree_struct):
        """ returns root node of a tree of Nodes, created from textual structure of tree """
        tree_struct_ar = self.parse_tree(tree_struct, self.syntax)
        tree_root = self.build_tree(tree_struct_ar)
        return tree_root

    def parse_tree(self, tree_struct, syntax):
        """ returns array with lines of tree_struct string parsed to level and name """

        # any row may have a prefix, may have a number of indents, has a name and may have a value
        match_row = r"(%s)((%s)*)(%s)(\w*)(%s)*(.*)" % (
            syntax['LINE_PREFIX'],
            syntax['INDENT'],
            syntax['NAME_SEPARATOR'],
            syntax['VALUE_SEPARATOR']
        )

        tree_struct = tree_struct.split("\n")
        ret = []

        for i, row in enumerate(tree_struct):
            if len(row) == 0:
                continue  # skip empty rows

            r = re.search(match_row, row)
            # logging.debug("matches: %s, indent: %s, name: %s", r.groups(), r.group(2), r.group(5))
            # for multi-character indent, divide match length by indentation size
            lvl = len(r.group(2)) / len(syntax['INDENT'])
            row = {'lvl': lvl, 'name': r.group(5)}
            if r.group(7) is not None and r.group(7) != '':
                row['value'] = r.group(7)
            ret.append(row)

        return ret

    def build_tree(self, tree_struct):
        """ returns root node of a tree of Nodes, created from array presentation of tree """
        root = Node(tree_struct[0]['name'])  # use always first row for root
        cntx = root

        # print(tree_struct[1:])

        # TODO: check error conditions, such as trying to add grand-child
        for i, row in enumerate(tree_struct[1:]):
            anc_no = len(cntx.get_anc())

            # set context to the parent element
            if row['lvl'] > anc_no:  # only direct children possible
                pass  # don't change context
            else:
                while row['lvl'] <= anc_no:  # move up hierarchy until right depth
                    cntx = cntx.parent
                    anc_no = len(cntx.get_anc())

            # add child and set the context to newly created element
            if 'value' in row and row['value'] is not None:
                cntx = cntx.add_child(row['name'], row['value'])
            else:
                cntx = cntx.add_child(row['name'])

        return root
