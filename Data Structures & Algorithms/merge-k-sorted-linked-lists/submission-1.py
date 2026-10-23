# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
     def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        # 1. 各リストの先頭をヒープに入れる
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(h, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        # 2. 一番小さいものを取り出してつなぐ
        while h:
            val, i, node = heapq.heappop(h)
            tail.next = ListNode(val)
            tail = tail.next
            # 3. 取り出したノードの次があれば、ヒープに入れる
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        return dummy.next
