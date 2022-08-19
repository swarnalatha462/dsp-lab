S1={"apple","bananas","guava","1apple"}
S1.add("Green")
print(S1)
S1.update({1,2,3})
print(S1)
S1.remove("apple")
S1.discard("guava")
S1.pop()
S1.remove(2)
S1.clear()
print(S1)
S1={1,2,3}
S2={3,4,5}
print(S1.union(S2))
print(S1.intersection(S2))
S1.update(S2)
print(S1)
S1.intersection_update(S2)
S1.isdisjoint({12,13})
S1.issubset({1,2,3,4,5})
S1.pop()
print(S1)




