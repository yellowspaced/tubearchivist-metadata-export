import os
from elasticsearch import Elasticsearch
import re
import xml.etree.ElementTree as ET

rootfile = ####<root file path>####

regex = re.compile('[^a-zA-Z]')

es = Elasticsearch(####<elastic server>####)

res = es.search(index="ta_video", query={"match_all": {}})


for hit in res['hits']['hits']:

    filex = (hit["_source"]["media_url"]).split(".")
    file = rootfile + filex[0] + ".nfo"
    print(file)
    
    tree = ET.ElementTree("tree")

    document = ET.Element("episodedetails")
    n1 = ET.SubElement(document, "plot")
    n1.text = hit["_source"]["description"]
    n2 = ET.SubElement(document, "title")
    n2.text = hit["_source"]["title"]
    n3 = ET.SubElement(document, "aired")
    n3.text = hit["_source"]["published"]
    n4 = ET.SubElement(document, "youtubeid")
    n4.text = hit["_source"]["youtube_id"]

    tree._setroot(document)
    tree.write(file, encoding = "UTF-8", xml_declaration = True)  
    os.chmod(file, 0o777)
