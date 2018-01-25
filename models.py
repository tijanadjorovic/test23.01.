"""Models."""


class Comment(object):
    def __init__(self, text, date):
        self.text = text
        self.date = date

    def __repr__(self):
        """Return string represantation of the object of type Comment."""
        return "Comment(text={}, date={})".format(self.text, self.date)

COMMENTS=[
        Comment('a','1111.11.11'),
        Comment('b','2222.22.22'),
        Comment('c','3333.33.33')
]