import tp1
import tp2
import extrinseque

if __name__ == "__main__":
  print "============== Step 1 : Crawling"
  print "Files are downloaded into 'Documents' directory"
  jsonDesc = loadJson("corpus_daniel/daniel.json")
  buildCorpus_JSon(jsonDesc)
  