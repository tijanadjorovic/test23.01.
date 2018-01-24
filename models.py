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

    # def tr(self):
    #     """Return user as HTML table row."""
    #     tr = "<tr>"
    #     tr += "<td>{}</td>".format(self.text)
    #     tr += "<td>{}</td>".format(self.date)
    #     tr += "</tr>"
    #     return tr

# class ComTable(Table):
#     text = Col('text')
#     date = Col('date')

# class Comment(object):
#     def __init__(self, text, date):
#         self.text = text
#         self.date = date

# COMMENTS=[
#     Comment('sanja','1991.24.01'),
#     Comment('tijana','1989.03.12'),
#     Comment('ceca','2018.15.07')
# ]

# table = ComTable(Comment)

# print(table.__html__())

if __name__ == '__main__':
    COMMENTS=[
        Comment('a','1111.11.11'),
        Comment('b','2222.22.22'),
        Comment('c','3333.33.33')
]