package boilerplate;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.Reader;
import java.net.MalformedURLException;
import java.net.URL;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import de.l3s.boilerpipe.BoilerpipeProcessingException;
import de.l3s.boilerpipe.extractors.ArticleExtractor;

public class Boilerpipe {
	public static String clean(String url_text) throws BoilerpipeProcessingException, MalformedURLException, FileNotFoundException {
		//URL url = new URL(url_text);
		// NOTE: Use ArticleExtractor unless DefaultExtractor gives better results for you
		Reader reader = new FileReader(url_text);
		String text = ArticleExtractor.INSTANCE.getText(reader);
		return text;
	}
	
	public JSONArray getJSONfile() {
		JSONArray array = null;
		JSONParser parser = new JSONParser();
	      String s = "[0,{\"1\":{\"2\":{\"3\":{\"4\":[5,{\"6\":7}]}}}}]";
		String jsonPattern = "[0,{\"1\":{\"2\":{\"3\":{\"4\":[5,{\"6\":7}]}}}}]";
//		12604": {
//		    "annotations": [
//		                    [
//		                      "N", 
//		                      "N", 
//		                      "N"
//		                    ]
//		                  ], 
//		                  "comment": "", 
//		                  "date_collecte": "None", 
//		                  "langue": "el", 
//		                  "path": "20120221_www.express.gr_9ebcd42d9bc47b4e2064bb65c640acb173d99a55c03f4e5bd4b6f584", 
//		                  "url": "http://www.express.gr/news/ygeia/567839oz_20120221567839.php3"
//		                }, 
	      try{
	         Object obj = parser.parse(s);
	         array = (JSONArray)obj;
				
	         System.out.println("The 2nd element of array");
	         System.out.println(array.get(1));
	         System.out.println();

	         JSONObject obj2 = (JSONObject)array.get(1);
	         System.out.println("Field \"1\"");
	         System.out.println(obj2.get("1"));    

	         s = "{}";
	         obj = parser.parse(s);
	         System.out.println(obj);

	         s = "[5,]";
	         obj = parser.parse(s);
	         System.out.println(obj);

	         s = "[5,,2]";
	         obj = parser.parse(s);
	         System.out.println(obj);
	      }catch(ParseException pe){
			
	         System.out.println("position: " + pe.getPosition());
	         System.out.println(pe);
	      }
	      return array;
	}
	
	public static void main(String[] args) throws FileNotFoundException {		

		try {
			System.out.println("Loading..");
			System.out.print(clean("/comptes/E15D861C/Bureau/Corpus/BoilerplateTP1/src/main/resources/test")); //http://www.rynekzdrowia.pl/Badania-i-rozwoj/Anglia-obiecujaca-szczepionka-przeciwko-HCV,115750,11.html"));
			System.out.println("Done.");
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (BoilerpipeProcessingException e) {
			e.printStackTrace();
		}
	}
}
