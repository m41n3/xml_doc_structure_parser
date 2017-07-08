import re
import logging


class Node:
    """Node represents ...

    Longer class information....

    Attributes:
        name: string name of Node
        parent: reference to parent Node
        children: list of child Nodes
    """

    PRINT_INDENT = '  '

    def __init__(self, name, parent=None, value=None):
        self.name = name
        self.parent = parent
        self.value = value
        self.children = []

    def __repr__(self):
        return "<Node name:%s>" % (self.name)

    def __str__(self):
        return self.name

    def add_child(self, name, value=None):
        child = Node(name, parent=self, value=value)
        self.children.append(child)
        return child

    def get_ancestors(self):
        """Returns list of ancestor nodes up till root"""
        # TODO: remove

        p = []
        c = self
        while c.parent is not None:
            c = c.parent
            p.append(c)
        return p

    def get_anc(self):
        """Returns list of ancestor nodes up till root"""

        if self.parent is not None:
            anc = self.parent.get_anc()
            anc.append(self.parent)
            return anc
        else:
            return []

    def print(self):
        """Returns string with the name of the node and its descendants"""

        ret = self.name
        if (self.value is not None):
            ret += ": " + self.value

        if len(self.children) == 0:
            pass
        else:
            ret += "\n"
            desc_print = []

            # get children and their descendants as array of strings
            for c in self.children:
                desc_print.append(c.print())

            desc_print = "\n".join(desc_print)
            ret += re.sub("^", self.PRINT_INDENT, desc_print, flags=re.MULTILINE)

        return ret

    def xmlify(self):
        """Returns string with the name of the node and its descendants"""

        ret = "<%s>" % self.name
        if (self.value is not None):
            ret += self.value

        if len(self.children) == 0:
            ret += "</%s>" % self.name
        else:
            ret += "\n"
            desc_print = []

            # get children and their descendants as array of strings
            for c in self.children:
                desc_print.append(c.xmlify())

            desc_print = "\n".join(desc_print)
            ret += re.sub("^", self.PRINT_INDENT, desc_print, flags=re.MULTILINE)
            ret += "\n</%s>" % self.name

        return ret
