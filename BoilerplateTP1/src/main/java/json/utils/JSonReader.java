package json.utils;

public class JSonReader {
	 public static void main(String[] args) {  
		  
		  JSONParser parser = new JSONParser();  
		  
		  try {  
		  
		   Object obj = parser.parse(new FileReader("E:\\CountryJSONFile.json"));  
		  
		   JSONObject jsonObject = (JSONObject) obj;  
		  
		   String nameOfCountry = (String) jsonObject.get("Name");  
		   System.out.println("Name Of Country: "+nameOfCountry);  
		  
		   long population = (Long) jsonObject.get("Population");  
		   System.out.println("Population: "+population);  
		  
		   System.out.println("States are :");  
		   JSONArray listOfStates = (JSONArray) jsonObject.get("States");  
		   Iterator<String> iterator = listOfStates.iterator();  
		   while (iterator.hasNext()) {  
		    System.out.println(iterator.next());  
		   }  
		  
		  } catch (FileNotFoundException e) {  
		   e.printStackTrace();  
		  } catch (IOException e) {  
		   e.printStackTrace();  
		  } catch (ParseException e) {  
		   e.printStackTrace();  
		  }  
		  
		 }

		Read more at http://www.java2blog.com/2013/11/jsonsimple-example-read-and-write-json.html#RzcSqpGL3HQ47oe6.99
}
