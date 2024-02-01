import mysql.connector
import matplotlib.pyplot as plt # pip install matplotlib

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="telacad",
    port=3306,
    database='telacad'
)
cursor = connection.cursor()

cursor.execute('SELECT count(*), produs FROM comenzi GROUP BY produs;')

rezultate = cursor.fetchall()

print(f"{rezultate=}")

produse = [elem[1] for elem in rezultate]
cantitate = [elem[0] for elem in rezultate]

fig = plt.figure(figsize=(10, 5))

plt.bar(produse, cantitate, color='blue', width=0.4)

plt.xlabel("Produse")
plt.ylabel("Cantitate")
plt.title("Produse vandute pe 01-02-2024")
plt.show()
