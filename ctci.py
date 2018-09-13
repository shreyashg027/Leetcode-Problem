class Solution:
    def checkPermutationOfPalindrome(self, str):
        str = str.lower().replace(" ", '')
        # print(str)
        charDict = dict()
        for char in str:
            if not char in charDict:
                charDict[char] = 1
            else:
                charDict[char] += 1
        # print(charDict)
        flag = 0
        for char in charDict:
            if charDict[char]%2 !=0:
                flag += 1
        if flag == 1:
            return True
        return False

    def checkCharacterEdits(self, originChar, editedChar):
        dictChar = dict()
        for char in originChar:
            dictChar[char] = char
        if len(originChar) == len(editedChar):
            flag = 0
            for char in editedChar:
                if char in dictChar:
                    flag += 1
            if flag == len(editedChar)-1:
                return True
        if len(editedChar) == len(originChar)-1:
            for char in editedChar:
                if not char in dictChar:
                    return False
                else:
                    return True
        if len(editedChar) == len(originChar)+1:
            flag = 0
            for char in editedChar:
                if char in dictChar:
                    flag += 1
            if flag == len(originChar):
                return True
        else:
            return False

    def stringCompression(self, string):
        string = string.lower()
        compressedStr = ''
        count = 1
        for i in range(len(string)-1):
            if string[i] != string[i+1]:
                compressedStr += string[i] + str(count)
                count = 1
            else:
                count += 1
        compressedStr += string[i] + str(count)
        if len(compressedStr) < len(string):
            return compressedStr
        else:
            return string


    def sherlockAndAnagrams(self, s):
        dictChar = dict()
        for char in s:
            if char not in dictChar:
                dictChar[char] = 1
            else:
                dictChar[char] += 1
        # print(dictChar)

    def checkMagazine(self, magazine, note):
        dictChar = dict()
        magazineArray = magazine.split(' ')
        for char in magazineArray:
            if char not in dictChar:
                dictChar[char] = 1
            else:
                dictChar[char] += 1
        noteArray = note.split(' ')
        for char in noteArray:
            if char not in dictChar:
                return "No"
            elif dictChar[char] == 0:
                return "No"
            else:
                dictChar[char] -= 1
        return "Yes"

    def countTriplets(self, arr, r):
        count = 0
        dict = {}
        dictPairs = {}

        for i in reversed(arr):
            if i*r in dictPairs:
                count += dictPairs[i*r]
            if i*r in dict:
                dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

            dict[i] = dict.get(i, 0) + 1
        print(dict)
        print(dictPairs)
        return count






test = Solution()

ans = test.checkPermutationOfPalindrome('Tact coa')
editedChar1 = test.checkCharacterEdits('pale', 'ple')
compressedStr = test.stringCompression('abcdefff')
# anagramCount = test.sherlockAndAnagrams('abba')
checkMagazine = test.checkMagazine('give me one grand today night', 'give one grand today')
countTriplets = test.countTriplets([1, 2, 3, 4], 2)
print(countTriplets)
print(checkMagazine)
# print(compressedStr)
