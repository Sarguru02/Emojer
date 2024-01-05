from emoji import get_aliases_unicode_dict
from fuzzywuzzy import process

ALIASES = get_aliases_unicode_dict()

def searcher(query):
    results = process.extract(query, ALIASES.keys(), limit=5)
    out = []
    for result in results:
        out.append(ALIASES[result[0]])
    return out
