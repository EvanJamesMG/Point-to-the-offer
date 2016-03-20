java版本
public class test {
	public static void main(String[] args){
		
		int [] sequence ={5,7,6,9,11,10,8};
		boolean res = VerifySquenceOfBST(sequence);
        	System.out.print(res);
	}
    public static boolean VerifySquenceOfBST(int [] sequence) {
        int root;
    	int breakindex=0;
  
    	if(sequence == null || sequence.length==0){
    		return false;
    	}
      int length = sequence.length;
    	root = sequence[length-1];
    	while(breakindex<length-1 && sequence[breakindex]<root){
    		breakindex++;
    	}
    	for(int i=breakindex;i<length-1;i++){
    		if(sequence[i]<root)
    			return false;
    	}
    	
    	boolean left = true;
    	if(breakindex>0){
        	int[] leftsequence = new int[breakindex] ;
        	for(int i=0;i<breakindex;i++){
        		leftsequence[i]=sequence[i];
        	}
    		left = VerifySquenceOfBST(leftsequence);
    	}
    	
    	boolean right = true;
    	if(breakindex<length-1){    
        	int[] rightsequence = new int[length-1-breakindex];
	    	for(int i=breakindex;i<length-1;i++){
	    		rightsequence[i-breakindex]=sequence[i];
	    	}
    		right = VerifySquenceOfBST(rightsequence);
    	}
    	return left && right;
    }
}
