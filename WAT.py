__author__ = 's0544768'

# crawler spuckt aus
content = [
    ("text, plapla", 1),
    ("waaaaaaaaaat", 2),
    ("text tex2", 3)
]

urls = [
    "www.wat.de",
    "www.google.de"
]

link_structure = [
    {2,1,4},
    {1,1,2},
    {3,4,5,6}
]

terms = {
    "token1": {1,2,3},
    "token2": {2,2,4},
    "waaaat": {5, 6, 7}
}

print(content)
print(urls)
print(link_structure)
print(terms)