import java.util.ArrayList;

public class test {
	
	public static void main(String[] args){
	
		
	}
    public RandomListNode Clone(RandomListNode pHead){
    	if(pHead == null)
    		return pHead;
    	RandomListNode currenthead = pHead;
    	
    	RandomListNode clonehead;
		//节点复制
    	while(currenthead !=null){
    		clonehead = new RandomListNode(currenthead.label);
    		clonehead.next = currenthead.next;
    		currenthead.next = clonehead;
    		currenthead = clonehead.next;
    	}
    	
    	//随机指针的复制
    	currenthead = pHead;
    	while(currenthead !=null){
    		clonehead = currenthead.next;
    		if(currenthead.random!=null)
    			clonehead.random = currenthead.random.next;
    		currenthead = clonehead.next;
    	}
    	
    	//将长字符串进行拆分
    	currenthead = pHead;
    	clonehead = pHead.next;
    	while(currenthead.next!=null){
    		RandomListNode tem = currenthead.next;
    		currenthead.next = tem.next;
    		currenthead = tem;
    	}
    	
		return clonehead;
    }

}
