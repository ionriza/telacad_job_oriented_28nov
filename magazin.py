# importam libraria mysql.connector
# dupa ce am instalat-o folosind
# pip install mysql-connector-python
from time import sleep
import mysql.connector # pip install mysql-connector-python
import requests # pip install requests
import random

# Cream un obiect de tip connection
# prin apelul metodei connect
# care primeste ca argumente, host, user, password si port
while True:

    obiect_response = requests.get('https://randomuser.me/api/?nat=gb')

    dictionar_response = obiect_response.json()

    telefon = dictionar_response['results'][0]['cell']
    nume = dictionar_response['results'][0]['name']['first']
    prenume = dictionar_response['results'][0]['name']['last']

    nume_full = nume + ' ' + prenume

    print(f'Salut, sunt {nume_full} si am intrat pe site-ul tau')

    stoc_magazin = {'tricou': 25, 'blugi': 50, 'hanorac': 45, 'sandale': 60, 'adidasi': 90,
                    'sacou': 70, 'rochie': 120, 'pantofi': 50, 'chiloti': 15, 'sosete': 10}

    produs_aleator = random.choice(list(stoc_magazin))

    pret = stoc_magazin[produs_aleator]

    data = '01-02-2024'

    cantitate = random.randint(1, 6)

    print(f"Am cumparat {cantitate} produse de tip {produs_aleator}")

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="telacad",
        port=3306,
        database='telacad' # USE telacad;
    )

    cursor = connection.cursor()

    cursor.execute("INSERT INTO comenzi "
                   "(produs, pret, cantitate, nume_client, nr_telefon, data_zi) "
                   f"VALUES ('{produs_aleator}', {pret}, {cantitate}, '{nume_full}', '{telefon}', '{data}')")

    connection.commit()
