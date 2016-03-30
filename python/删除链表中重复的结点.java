/*
题目描述

在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
*/
public class Solution {
	    public static ListNode deleteDuplication(ListNode pHead)
	    {
	    	if(pHead==null || pHead.next ==null)
	    		return pHead;
	    	ListNode dummy = new ListNode(0);
	    	dummy.next = pHead;
	    	ListNode node = dummy;
	    	while(node.next !=null && node.next.next !=null){
	    		if(node.next.val !=node.next.next.val)
	    			node = node.next;
	    		else {
					while(node.next!=null && node.next.next!=null &&node.next.val==node.next.next.val){
						node.next = node.next.next;
					}
					node.next = node.next.next;
				}

	    	}
			return dummy.next;
	    }
}
