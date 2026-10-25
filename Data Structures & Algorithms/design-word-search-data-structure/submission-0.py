class WordDictionary:

    # end = False
    # children = {
    #     "a": WordDictionary
    #         end = False
    #         children = {
    #             "a": WordDictionary
    #                     end = True
    #                     children = {
    #                     "y": WordDictionary
    #                             end = True
    #                             children = {}
    #                     }
    #         },
    #     "b": WordDictionary
    #         end = True
    #         children = {
    #             "b": {}
    # 
    #         }
    # }

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for i, c in enumerate(word):
            if c == '.':
                for child in curr.children.values():
                    if child.search(word[i + 1:]):
                        return True
                return False

            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.end


