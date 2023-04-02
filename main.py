# python3
# 221RDB395 Anastasija Bondare 13.grupa

class Query:
    def _init_(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = []
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query.name
        elif query.type == 'del'
            if query.number in contacts:
                del contacts[query.number]
        else:
            response = contacts.get(query.number, 'not found')
            result.append(response)
    return result

if name == 'main':
    queries = read_queries()
    results = process_queries(queries)
    write_responses(results)
