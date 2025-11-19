names=["smith","johnson","jones","brown","davis","miller","wilson","moore","taylor","anderson","thoms","jackson","white"]
from collections import defaultdict

print(names)

length=[(len(nam)) for nam in names]
print("length of each name is ",length)

groups= defaultdict(list)
for nam in names:
    groups[len(nam)].append(nam)

most_freq=sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
print("three most frequent name length are:")
for length, group in most_freq[:3]:
    print(f"{len(group)} names of length {length}: {group}")


least_freq=sorted(groups.items(), key=lambda x: len(x[1]))
print("three least frequent name length are:")
for length, group in least_freq[:3]:
    print(f"{len(group)} names of length {length}: {group}")







