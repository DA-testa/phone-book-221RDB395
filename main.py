# Anastasija Bondare 13.grupa 221RDB395
# python3

class Query: # Tiek definēta klase ar metodi _init_, 
    def __init__(self, query): # kurā ir viens arguments "query".
        self.type = query[0] # "type" vērtība tiek piešsaņemtaķirsaņemta kā pirmā vērtība sarakstā.
        self.number = int(query[1]) # "number" vērtība tiek saņemta kā otrā skaitliskā (int) vērtība sarakstā.
        if self.type == 'add': # Ja "type" ir vienāds ar "add",
            self.name = query[2] # tad "name" tiek piešķirta trešā vērtība sarakstā

def read_queries(): # Tiek definēta lasīšanas funkcija
    n = int(input()) # n - skaits, cik daudz vaicājumu (queries) tiks apstrādāti
    return [Query(input().split()) for i in range(n)] # Tiek atgriezsts saraksts, kas tika izveidots no lietotāja ievadītajiem datiem

def write_responses(result):
    print('\n'.join(result)) # Ar motodi "join" tiek apvienoti visi elementi vienā rindā, kur katrs elements tiek atdalīts "\n" 
    # ar jaunu rindu un pēc tam iegūtais rezultāts tiks izvadīts konsolē.

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [] # Tiek izveidots saraksts ar kontaktiem, kas satur visus telefona numurus
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name # Pievieno jaunu ierakstu sarakstā
            # if we already have contact with such number,
            # we should rewrite contact's name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                contacts.pop(cur_query.number) # Tiek izdzēsts numurs no saraksta,ja tas iepriekš pastāvēja
        else:
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__': # Ja programma tiek izpildīta kā galvenā programma, tad
    write_responses(process_queries(read_queries())) # tiek izsauktas funkcijas, kas izveidota sarakstu, apstrādā sarakstā iegūtos datus
    # un pēc tam izvada rezultātu konsolē.