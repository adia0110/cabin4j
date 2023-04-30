import heapq

class Autocomplete:
    def __init__(self):
        self.words = {}
    
    def add_word(self, word, weight):
        self.words[word] = weight
    
    def autocomplete(self, prefix, k):
        heap = []
        for word, weight in self.words.items():
            if word.startswith(prefix):
                heapq.heappush(heap, (-weight, word))
        return [word for _, word in heapq.nlargest(k, heap)]

autocomplete = Autocomplete()

with open("Challenge-3-Input.txt", encoding="utf8") as f:
    for line in f:
        split_1 = line.split()
        weight=split_1[0]
        result=split_1[1:]
        word = ','.join(result)
        autocomplete.add_word(word, float(weight))

while True:
    prefix = input("Enter prefix: ")
    k = int(input("Enter k: "))
    suggestions = autocomplete.autocomplete(prefix, k)
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
