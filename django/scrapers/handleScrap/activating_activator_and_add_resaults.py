from .factoryfllow.approad import main_activate
from django.conf import settings


def orenge_activate(object,type):
    """ get activated first when script is being compiled"""
    try:
       return main_activate(object,type)

    except Exception:
       raise Exception('Somthing wrong with scraping process') 


class sendScrapersValues:
    """ a class to new resaults objects based on data recieved from scrapers"""

    def __init__(self, resaults:dict, scraper_name, user) -> None:
        self.resaults = resaults
        self.scraper = scraper_name
        self.user = user

    def add_resaults_as_article_model(self):
        for resault in self.resaults:
            settings.ARTICLE_MODEL.objects.create(
                category = resault['category'],
                title = resault['title'],
                authors = resault['authors'],
                excerpt = resault['abstract'],
                content = resault['content'],
                date = resault['date'],
                scraper = self.scraper,
                user = self.user,
        )

        
class sendDoiValue:
    """ a class that returns pdf based on doi"""

    def __init__(self,link, doi:str) -> None:
        self.doi = doi
        self.link = link

    def return_resaults(self):
        return self.link


def main(object,type:str):
    if type == "scraper":
       new_resault_geter = sendScrapersValues(orenge_activate(
           object,type), object.name,object.user)
       return new_resault_geter.add_resaults_as_article_model()
    
    new_sci_file = sendDoiValue(orenge_activate(object,type),object)
    return new_sci_file.return_resaults()
    
    

