# python3

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
    # Keep list of all existing (i.e. not deleted yet) contacts.
    y = 2 + 9999999 
    contacts = []
    for i in range(0,y+1):
        contacts.append('0')
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name

            if contacts[cur_query.number] != '0':
                contacts[cur_query.number] = cur_query.name

            else: # otherwise, just add it
                contacts[cur_query.number] = cur_query.name
                               
        elif cur_query.type == 'del':
            if contacts[cur_query.number] != '0':
                contacts[cur_query.number] = '0'
                
        else:
            response = 'not found'
            if contacts[cur_query.number] != '0':
                response = contacts[cur_query.number]

            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

