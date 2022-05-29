# def word_slices(word):
#     slices = []
#     if len(word) < 3:
#         slices.append(word)
#         print(slices)
#     else:
#         n = 0
#         while n < len(word):
#             j = 0
#             while j < len(word):
#                 print(word[n:n+j])
#             j += 1
#         n += 1

def word_slices(word):
    if len(word) == 1:
        print([word])
    print([word[a:b] for a in range(len(word)+1) for b in range(len(word)+1) if len(word[a:b]) >= 2])
    #print([word[a:b] if (len(word[a:b]) >= 2) else 'x' for a in range(len(word)+1) for b in range(len(word)+1)])
    #print([word if (len(word) <= 2) else word[a:b] for a in range(len(word)+1) for b in range(len(word)+1)])

word_slices('i')
word_slices('to')
word_slices('table')
word_slices('tablespoon')
