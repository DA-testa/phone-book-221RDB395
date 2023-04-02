# python3
# 221RDB395 Anastasija Bondare 13.grupa

class Query: # Tiek definēta klase Query, kas satur metodi __init__,
    def __init__(self, query): # kura tiek izsaukta pēc objekta 'Query'.
        self.type, self.number = query[0], int(query[1]) # Pirmā pozīcijā tiek saglabāts vaicājums jeb funkcija - add, del vai find.
        # Otrajā pozīcijā tiek saglabāts telefona numurs kā vesels skaitlis.
        if self.type == 'add': # Ja vaicājums jeb funkcija ir vienāda ar add, tad 
            self.name = query[2] # Trešajā pozīcijā tiek saglabāts vārds, kas tika piešķirts telefona numuram.

def read_queries(): # Tiek definēta "lasīšanas" funkcija. 
    n = int(input()) # No tastatūras ievada vaicājamu skaitu, cik kontaktu tiks apstrādāti.
    return [Query(input().split()) for i in range(n)] # Tiek izveidots saraksts ar kontaktiem, kuri tiks aprstādāti pēc atbilstošām funkcijām.

def write_responses(result): print('\n'.join(result)) # Tiek izvadīti apstrādātie kontakti jaunajā rindā (katrs apstrādātais kontakts būs jaunajā rindā).

def process_queries(queries): # Tiek definēta "apstrādāšanas" funkcija.
    result = [] # Tiek definēts tukšs saraksts, kur glabās apstrādātos kontaktus (beigas).
    phone_book = {} # Tiek definēts tukšs saraksts ar kontaktiem, kurus lietotājs manuāli ievadīs no tastatūras (sākums).
    for current_query in queries: 
        if current_query.type == 'add':
            phone_book[current_query.number] = current_query.name # Ja kontakts jau pastāv ar tādu pašu vārdu, tad tam tiks piešķirts jauns vārds.
        elif current_query.type == 'del':
            if current_query.number in phone_book:  # Ja kontaks jau pastāv sarakstā, 
                del phone_book[current_query.number] # tad tas tiks izdzēsts no tā.
        else:
            if current_query.number in phone_book: # Ja kontaksts jau pastāv esošā sarakstā,
                result.append(phone_book[current_query.number]) # tad tiks izvadīts vārds piešķirtajam numuram.
            else:
                result.append("not found") # Pretējā gadījumā tiks izvadīts paziņojums,ka kontakts netika atrasts.
    return result


if __name__ == '__main__': # Izsauc funkcijas, lai apstrādātu ievadītos kontaktus un pēc tam tos izvadītu.
    write_responses(process_queries(read_queries()))

