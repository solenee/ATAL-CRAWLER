#coding:utf-8

import tp1
import requests
import justext
import re, sys, os


def eval_intrinseque(toolDir, goldenDir, languagesList=None) :
  if languagesList is None :
    languagesList = ["cn", "el", "en", "pl", "ru"]
  for lang in languagesList :
    os.system("echo =================="+lang+ "; python cleaneval.py -t "+toolDir+"/"+lang+" "+goldenDir+"/"+lang)


if __name__ == "__main__" :
  jsonDesc = tp1.loadJson("corpus_daniel/daniel.json")
  #tp1.writePages_jusText(jsonDesc, "corpus_daniel/files") 
  #tp1.formatGoldenDir(jsonDesc, "corpus_daniel/files") 
  #eval_intrinseque("Documents_justText", "Documents_Golden")
  #eval_intrinseque("Documents_Boilerpipe", "Documents_Golden")
  