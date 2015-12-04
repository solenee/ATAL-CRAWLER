#coding:utf-8

import requests
import justext
import json
import codecs
import re, sys, os, nltk

LANGUAGES = []
CODE_LANG = {"cn" : "Chinese" , "el" : "Greek" , "en" : "English", "pl" : "Polish", "ru" : "Russian"}
filename = "url_list.txt"
idNames = "path_list.txt"

def loadJson(filename) : 
  with open(filename, "r") as f:
    text = f.read()
    jsonDesc = json.loads(text)
    #print(len(jsonDesc))
    #print(jsonDesc)
  return jsonDesc
    
def buildCorpus() :
  with open(filename, "r") as f:
    with open(idNames, "r") as fIds : 
      for url in f:
        fIds.readline()
	path = fIds.readline().strip()
        os.system(" wget -O "+"Documents/"+ path + " "+ url.strip() + " -o log/"+path+".log")    
    
def clean_jusText_localFile(filename, language, outputfile) : 
  try : 
    with codecs.open(filename, "r", "utf-8") as f:
      with open(outputfile, "w") as output:
        content = f.read()
        paragraphs = justext.justext(content, justext.get_stoplist(CODE_LANG[language]))
        for paragraph in paragraphs:
          if not paragraph.is_boilerplate:
            output.write(paragraph.text.encode('utf-8')+"\n")
  except ValueError :
    print "[jusText] Stopwords list not available for "+language
      
def clean_jusText_url(url="http://planet.python.org/", outputfile="") : 
  response = requests.get(url)
  paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
  for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
      print paragraph.text

def formatGoldenDir(jsonDesc, rawGoldenDir) :
  languagesList = []
  try :
    os.system("mkdir Documents_Golden")
  except Exception : 
    print "Workspace ready?"
  for anID in jsonDesc :
    desc = jsonDesc[anID]
    language = desc["langue"]
    filename = rawGoldenDir+"/"+ desc["path"]
    if language not in languagesList : 
      os.system(" mkdir Documents_Golden/"+ language)
      languagesList.append(language)
    outputfile = "Documents_Golden/"+ language +"/"+ (desc["path"].strip())
    try :
      os.system("cp "+filename+" "+outputfile)
    except Exception as details:
      print "["+language+"] "+filename+" : ", details
      
def writePages_jusText(jsonDesc, goldenDir) : 
  languagesList = []
  try :
    os.system("mkdir Documents_justText")
  except Exception : 
    print "Workspace ready?"
  for anID in jsonDesc :
    desc = jsonDesc[anID]
    language = desc["langue"]
    filename = goldenDir+"/"+ desc["path"]
    if language not in languagesList : 
      os.system(" mkdir Documents_justText/"+ language)
      languagesList.append(language)
    outputfile = "Documents_justText/"+ language +"/"+ (desc["path"].strip())
    try :
      clean_jusText_localFile(filename, language, outputfile)
    except Exception as details:
      print "["+language+"] "+filename+" : ", details

def buildCorpus_JSon(jsonDesc) :
  for anID in jsonDesc :
    desc = jsonDesc[anID]
    if desc["langue"] not in LANGUAGES : 
      os.system(" mkdir Documents/"+ desc["langue"])
      LANGUAGES.append(desc["langue"])
    os.system(" wget -O "+"Documents/"+desc["langue"]+"/"+ (desc["path"].strip()) + " "+ (desc["url"].strip()) + " -o log/"+desc["path"]+".log")
  print LANGUAGES

if __name__ == "__main__":
  jsonDesc = loadJson("corpus_daniel/daniel.json")
  buildCorpus_JSon(jsonDesc)
  


