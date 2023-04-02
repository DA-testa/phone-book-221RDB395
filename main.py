class Query:
    def __init__(self, query):
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
    # Use a dictionary to store contacts instead of a list
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # If we already have a contact with such number, overwrite its name
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            # If the contact exists, delete it from the dictionary
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            # If the contact exists, return its name, otherwise return "not found"
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
