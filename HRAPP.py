# importam toate clasele
from Angajat import Angajat
from Manager import Manager
from HR import HR

angajat1 = Angajat('riza', 'ion', 1)
angajat2 = Angajat('paun', 'razvan', 2)
angajat3 = Angajat('preotescu', 'bogdan', 3)
manager1 = Manager('ionascu', 'eliza', 4, 1, [angajat1, angajat2, angajat3])
hr1 = HR('scaunasu', 'lucica', 5, 2, [angajat1, angajat2, angajat3, manager1], 1)
angajat1.adauga_concediu(1, 2)
angajat2.adauga_concediu(2, 3)
angajat3.adauga_concediu(3, 4)
manager1.aproba_concedii()
print("Manager accepta concediile de pe 1-2 si 2-3, dar refuza concediul de pe 3-4")
manager1.adauga_review(angajat3, 'vrea sa ia concediu si nu se gandeste la altii', 1)
manager1.adauga_concediu(3, 4)
hr1.listeaza_concedii()
print("HR-ul vede ca manager-ul a refuzat concediul angajatului de pe 3-4 si vede cererea managerului de concediu")
hr1.aproba_concedii()
print("refuza cererea managerului")
hr1.listeaza_reviewuri()
print("HR-ul vede si review-ul negativ si alege sa-i lase un review negativ managerului")
hr1.adauga_review(manager1, 'un manager nu foarte bun', 1)