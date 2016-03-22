import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.PrimitiveIterator.OfDouble;
import java.util.concurrent.BlockingDeque;
import java.util.concurrent.ThreadFactory;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

import org.omg.PortableServer.ID_ASSIGNMENT_POLICY_ID;

public class test {
	
	public static void main(String[] args){
		
		ArrayList<String> res = new ArrayList<String>();
		res= Permutation("abc");
		System.out.println(res);
	
		
	}

    public static ArrayList<String> Permutation(String str) {
		ArrayList<String> res = new ArrayList<String>();
		char prenode=0;
    	if(str == null || str.length()==0)
			return res;
    	if(str.length()==1){
    		res.add(str);
    		return res;
    	}
    	
    	for (int i=0;i<str.length();i++){
    		if(prenode == str.charAt(i)){
    			continue;
    		}else {
    			ArrayList<String> temlist;
    			temlist = Permutation(str.substring(0,i)+str.substring(i+1));
    			for(int i1 =0;i1<temlist.size();i1++){
    				res.add(str.charAt(i)+temlist.get(i1));
    			}
			}
    		prenode = str.charAt(i);
    	}
    	
		return res;
    }

}
