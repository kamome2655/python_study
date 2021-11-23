import eel
import desktop2
import amazon_web2

app_name="html"
end_point="index2.html"
size=(700,600)


@ eel.expose
def main(search_url):
    amazon_web2.main(search_url)
    
desktop2.start(app_name,end_point,size)