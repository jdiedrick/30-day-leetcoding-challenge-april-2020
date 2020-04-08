class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length_of_list = 0
        
        first_pass_pointer = head
        
        while first_pass_pointer:
            length_of_list += 1
            first_pass_pointer = first_pass_pointer.next
        
        mid = length_of_list // 2
        
        second_pass_pointer = head
        i = 0
        
        while i != mid:
            second_pass_pointer = second_pass_pointer.next
            i += 1
        
        return second_pass_pointer
