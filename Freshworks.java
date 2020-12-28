
import java.util.*;
import java.io.*;
import java.lang.String;
import org.json.JSONObject; 
public class Freshworks 
{
 static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 public void Insert( ) throws IOException
 {
   Scanner in = new Scanner (System.in);
  System.out.println("Enter the country name : ");
	String country_Name=in.next();
	System.out.println("Enter the country capital : ");
	String country_capital=in.next();
	System.out.println("Enter the region : ");
	char  region=in.nextInt();
	System.out.println("Enter the language : ");
	char language=in.nextInt();     
  JSONObject obj=new JSONObject(); 
  obj.put("country_name",country_Name);    
  obj.put("country_capital",country_capital);    
  obj.put("region",region);
  obj.put("language",language);
  PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("Freshworks.txt",true)));
  pw.print(obj);
  System.out.println("Details added successfully.");
  pw.close();
 }
public static void main(String args[]) throws IOException
{
  Freshworks in = new Freshworks();
  in.Insert();
}
 
}
