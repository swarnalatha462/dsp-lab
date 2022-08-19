d={"one":1,"two":2,"three":3,"four":4}
print(type(d))
print(len(d))
print(d["two"])
d.get("three")
print(d.keys())
d.update({"seven":7})
print(d)
d.pop("one")
print(d.popitem())
del d["three"]
print(d)
d.clear()
print(d)
del d
print(d)

