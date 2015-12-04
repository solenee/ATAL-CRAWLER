import test_api
import os

def eval_extrinseque(toolName, languagesList=None) :
  if languagesList is None :
    languagesList = ["cn", "el", "en", "pl", "ru"]
  for lang in languagesList :
    outputFile = "results/"+toolName+"_"+lang+".extrinseque"
    with open(outputFile, "w") as f :
      toolDir = "Documents_"+toolName
      file_paths = os.listdir(toolDir+"/"+lang)
      for filename in file_paths:
        f.write(filename+"\t"+test_api.get_diagnosis(toolDir+"/"+lang+"/"+filename)+"\n")
        
if __name__ == "__main__" :
  eval_extrinseque("justText")
  eval_extrinseque("Boilerpipe")
  eval_extrinseque("Golden")
  os.system("./eval.sh")
    