# import math
#
# n =14
# p= [1,3,7,11,2,4]
#
#
# def getUmbrellas(n, p):
#
#     umb_list = []
#
#     if not p:
#         return -1
#
#     for i in p:
#
#         sum = 0
#
#         if n%i ==0:
#             sum = sum + n/i
#             umb_list.append(sum)
#
#         else:
#             k = n%i
#             d = p
#             d.remove(i)
#
#             sum = n/i
#             val = getUmbrellas(k, d)
#             if val != -1:
#                 sum = sum + val
#                 umb_list.append(sum)
#
#             else:
#                 return -1
#
#     return(int(min(umb_list)))
#
# def binSearch(arr, low, high, num):
#
#     if high >= low:
#         mid = low + high / 2
#         mid = math.floor(mid)
#         if arr[mid] == num:
#             return mid
#         elif arr[mid] > num:
#             return binSearch(arr, low, mid - 1, num)
#         else:
#             return binSearch(arr, mid + 1, high, num)
#
#
# def twoSum(arr, target):
#     hashTable = []
#     temp = []
#     result = []
#     for i in range(len(arr)):
#         required = target - arr[i]
#         if required in hashTable:
#             index = hashTable.index(required)
#             temp.append(index)
#             temp.append(i)
#         hashTable.append(arr[i])
#     result.append(temp)
#     return result
#
# # print(twoSum([0,1,2,3,4,5,6], 5))
#
# def threeSum(arr, target):
#     hashTable = []
#     result = []
#
#     for i in range(len(arr)):
#         current = target - arr[i]
#         for j in range(i+1, len(arr)):
#             required = current - arr[j]
#             if required in hashTable:
#                 temp = hashTable.index(required)
#                 result.append(temp)
#                 result.append(i)
#                 result.append(j)
#         hashTable.append(arr[i])
#     return result
#
# # print(threeSum([2,7,1,3,4,5,6],17))
#
# # def subArray(arr1, arr2):
# #     global flag
# #     len1 = len(arr1)
# #     len2 = len(arr2)
# #     if len1 > len2:
# #         flag = 1
# #     length = max(len1, len2)
# #     for i in range(length):
#
#
# arr = [1,3,5,6,7,9]
# search = 7
# # print('Binary search on - [1,3,5,6,7,9], searching for position of 7 : ', binSearch(arr, 0, len(arr)-1, search))
#
#
#
# # N =4
# # print(getUmbrellas(N, p))
#
# def arrRotation(arr, d):
#     print(arr[0:d])
#     first = arr[0:d].reverse()
#     print('first:', first)
#     last = arr[d+1:].reverse()
#     print('last:', last)
#     final = []
#     final.append(first)
#     final.append(last)
#     result  = final.reverse()
#     print(result)
#     return result
#
# # print(arrRotation([1,2,3,4,5,6,7], 2))
#
#
# def countRotations(arr):
#     cnt = 0
#     for i in range(len(arr)):
#         if arr[i] > arr[i+1]:
#             high = i
#             low = i+1
#             break
#     i = 1
#     while cnt != low:
#         leftRotatebyOne(arr)
#         cnt += 1
#     print('Output : ', arr)
#     print('No. of Rotations required : ', cnt)
#
# def leftRotatebyOne(arr):
#     temp = arr[0]
#     n = len(arr)
#     for i in range(n-1):
#         arr[i] = arr[i + 1]
#     arr[n-1] = temp
#
#     # Driver program to test above functions */
# arr = [7,8,1,2,3]
# # print('Input : ', arr)
# # countRotations(arr)
#
# #########linkedLists##########
#
# class node(object):
#     def __init__(self, d):
#         self.data = d
#         self.next_node = None
#
# class linkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def add(self, d):
#         new_node = node(d)
#
#         if not self.head:
#             self.head = new_node
#         else:
#             temp = self.head
#             while temp.next_node is not None:
#                 temp = temp.next_node
#             temp.next_node = new_node
#             new_node.next_node = None
#
#     def add_at(self, d, value):
#         new_node = node(value)
#         temp = self.head
#         while temp.next_node.data != d:
#             temp = temp.next_node
#         current_node = temp
#         new_node.next_node = current_node.next_node
#         current_node.next_node = new_node
#
#     def find(self, d):
#         temp = self.head
#         while temp is not None and temp.data != d:
#             temp = temp.next_node
#         if temp is None:
#             print('Not found')
#         else:
#             print('Found')
#
#     # def remove(self):
#
#     def to_list(self):
#         lis = []
#         temp = self.head
#         while temp:
#             lis.append(temp.data)
#             temp = temp.next_node
#         print(lis)
#
#
#
#
#
# l = linkedList()
# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.add(5)
# l.add(6)
# l.add_at(2, 2.55)
# # l.to_list()
# # l.find(10)
#
#
# def lis(arr):
#     hashCount = [1]*len(arr)
#     print(hashCount)
#     for j in range(1, len(arr)):
#         i = 0
#         while i != j:
#             if arr[i] < arr[j]:
#                 hashCount[j] = max(hashCount[j], hashCount[i]+1)
#             i += 1
#         print(hashCount)
#
#     return max(hashCount)
# arr = [2, 4, 5, 6, 1, 3, 7, 0, 9, -3, 14]
# # print('Longest increasing Subsequence for', arr,' : ', lis(arr))
#
#
# #######Valid Parenthesis#######
# def validParen(str):
#     stack = []
#     for i in range(len(str)):
#         if str[i] == ')':
#             temp = stack.pop()
#             if temp != '(':
#                 return 'Not valid!'
#             elif i == len(str) and stack == []:
#                 return 'Valid'
#         elif str[i] == '}':
#             temp = stack.pop()
#             if temp != '{':
#                 return 'Not valid!'
#             elif i == len(str) and stack == []:
#                 return 'Valid'
#         elif str[i] == ']':
#             temp = stack.pop()
#             if temp != '[':
#                 return 'Not valid!'
#             elif i == len(str) and stack == []:
#                 return 'Valid'
#         else:
#             stack.append(str[i])
#         print('Stack:', stack)
#     if stack == []:
#         return 'Valid!!'
#     else:
#         return 'Not valid!'
#
# # expression='[{({{[]}})()}]'
# # print('Checking for Valid Parenthesis in sequence, Input : ', expression)
# # print('Output : ', validParen(expression))
#
# ########Add two numbers using Linked Lists########
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#        self.val = x
#        self.next = None
#
# class Solution:
#     def __init__(self):
#         self.head = None
#
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         q = 0
#
#         while l1 is not None and l2 is not None:
#             if q:
#                 sum = l1.val + l2.val + q
#                 q = 0
#             else:
#                 sum = l1.val + l2.val
#             if sum > 9 :
#                 rem = sum % 10
#                 q = sum / 10
#                 print(rem,'->')
#             else:
#                 print(sum, '->')
#
#
# def longestSubstring(s):
#     result = []
#     helper = ""
#
#     for i in range(len(s)):
#         if s[i] not in helper:
#             helper += s[i]
#         else:
#             helper = ""
#             helper += s[i]
#         result.append(helper)
#     print('All substrings :', result)
#     return max(result, key=len)
#
# s = 'bbbbbbb'
# print('Longest Sunstring, Input : ', s)
# print('Output : ', longestSubstring(s))

