class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = paragraph.lower()
        s = re.sub('[^a-z]', ' ', s)
        list_s = s.split(' ')
        for char in list_s[:]:
            if char == '':
                list_s.remove(char)
                
        for ban_word in banned:
            for one_of_word in list_s[:]:
                if one_of_word == ban_word:
                    list_s.remove(one_of_word)
        num_index = []
        for i in range(len(list_s)):
            num = 0
            for j in range(len(list_s)):
                if list_s[i] == list_s[j]:
                    num += 1
            num_index.append(num)

        tmp = max(num_index)
        index = num_index.index(tmp)

        return list_s[index]