class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dictChar = {}
        for items in cpdomains:
            item = items.split(' ')
            print(item)
            i = item[1].index('.')
            subitem = item[1]
            while '.' in subitem:
                subitem = subitem[subitem.index('.')+1:]
                print(subitem)
                if subitem not in dictChar:
                    dictChar[subitem] = int(item[0])
                else:
                    dictChar[subitem] += int(item[0])

            if item[1] not in dictChar:
                dictChar[item[1]] = int(item[0])

            else:
                dictChar[item[1]] += int(item[0])
        ans = []
        for domain, num in dictChar.items():
            ans.append(str(num)+' '+domain)
        return ans

test = Solution()
test.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
str = 'dfdf'