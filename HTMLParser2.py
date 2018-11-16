from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)

    def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))

# 4
# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->