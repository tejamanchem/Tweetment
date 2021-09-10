import re

class Tweet:
    def __init__(self,data):
        self.data = data

    def user_link(self):
        return "http://twitter.com/{}".format(self.data['username'])

    def filtered_text(self):
        print(self.data)
        print(self.data["text"])
        return self.filtered_brands(self.filter_urls(self.data['text']))

    def filtered_brands(self,text):
        brands = ["@pspk","@warbyparker","@bonoboss","@casper","@glossier","@dollarshaveclub","@allbirds"]


        for brand in brands:
            print(brand)
            print(text)
            if(brand in text):
                
                text=text.replace(brand,"<mark>{}</mark>".format(brand))
            else:
                continue

        return text

    def filter_urls(self,text):
        return re.sub("(https?:\/\/\w+(\.\w+)+(\/[\w\+\-\,\%]+)*(\?[\w\[\]]+(=\w*)?(&\w+(=\w*)?)*)?(#\w+)?)",r'<a href="\1" target="_blank">\1</a>',text)
        