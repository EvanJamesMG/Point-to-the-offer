/*
题目描述

一个链表中包含环，请找出该链表的环的入口结点。
*/

public class Solution {

	    public ListNode EntryNodeOfLoop(ListNode pHead){
	    	
	    	if(pHead ==null || pHead.next==null){
	    		return null;
	    	}
			ListNode slow = pHead;
			ListNode fast = pHead;
			while (fast !=null && fast.next !=null){
					slow = slow.next;
					fast = fast.next.next;
					if(slow ==fast)
						break;
			}
		
			if(slow==fast){
				slow = pHead;
				while(slow!=fast){	
					slow = slow.next;
					fast = fast.next;
				}
				return slow;
			}
			return null;

	    }
}
