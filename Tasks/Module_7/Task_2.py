dict = {}
number_of_pairs = int(input())

for i in range(0, number_of_pairs):
    synonym, synonym2 = input().split()
    dict[synonym] = synonym2
#print(dict)

reversed_dict = {}
for key, item in dict.items():
    reversed_dict[item] = key
#print(reversed_dict)

word = input()
print(reversed_dict.get(word))