from config import Url,Service,Database
from selenium.webdriver import Chrome 

url = Url("prod")
service = Service("prod")
database = Database("prod")
print (url.get_main_url()+url.get_document_register_url())
print (service.get_endpoint())
print (database.get_database())