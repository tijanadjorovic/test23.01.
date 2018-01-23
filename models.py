"""Models."""

class Comment(object):
    def __init__(self, text, date):
        self.text = text
        self.date = date

    def __repr__(self):
        return "text: {}, date: {}".format(
            self.text,
            self.date
    )

    def tr(self):
        """Return user as HTML table row."""
        tr = "<tr>"
        tr += "<td>{}</td>".format(self.text)
        tr += "<td>{}</td>".format(self.date)
        tr += "</tr>"
        return tr

if __name__ == '__main__':
    COMMENTS=[
        Comment('sanja','1991.24.01'),
        Comment('tijana','1989.03.12'),
        Comment('ceca','2018.15.07')
]