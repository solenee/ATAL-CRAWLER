import tp1
import tp2
import extrinseque

if __name__ == "__main__":
  print "============== Step 1 : Crawling"
  print "Please execute crawl.py to perform the crawling phase"
  
  print "============== Step 2 : Boilerplate removal"  
  #Boilerpipe
  print "Tool 1 : Boilerpipe "
  print "Please open BoilerplateTP1 eclipse project and run src/main/java/Boilerpipe.java (see details in README file)"
  #TODO ant file
  print "Cleaned pages will be available in Documents_Boilerpipe directory"
  
  #jusText
  print "Tool 2 : jusText"
  input("Press enter to clean the corpus using jusText")
  jsonDesc = tp1.loadJson("corpus_daniel/daniel.json")
  tp1.writePages_jusText(jsonDesc, "corpus_daniel/files")
  print "Cleaned pages are available in Documents_justText"
  
  
  print "============== Step 3 : Intrinsic evaluation"
  #jusText
  input("Press enter to start the evaluation")
  print "Preparing workspace..."
  tp1.formatGoldenDir(jsonDesc, "corpus_daniel/files") 
  print "Evaluating jusText..."
  eval_intrinseque("Documents_justText", "Documents_Golden")
  print "Evaluating Boilerpipe..."
  eval_intrinseque("Documents_Boilerpipe", "Documents_Golden")
  print "Please check 'results' directory for the results (.intrinseque)"
  
  print "============== Step 3 : Extrinsic evaluation"
  input("Press enter to start the evaluation")
  eval_extrinseque("Golden")
  print "Please check 'results' directory for the results (.extrinseque)"
  print "Evaluating jusText..."
  eval_extrinseque("justText")
  print "Evaluating Boilerpipe..."
  eval_extrinseque("Boilerpipe")
  print "Evaluating Golden files..."
  
  