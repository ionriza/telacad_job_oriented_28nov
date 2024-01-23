class Angajat:

    def __init__(self, nume, prenume, angajat_id):
        self.nume = nume
        self.prenume = prenume
        self.angajat_id = angajat_id
        self.concedii = []
        self.reviews = []

    def adauga_concediu(self, zi_start, zi_stop):
        concediu = {
            'zi_start': zi_start,
            'zi_stop': zi_stop,
            'aprobat': None
        }
        self.concedii.append(concediu)


if __name__ == '__main__':
    print('Ma apuc sa testez codul')
    # instantiez un angajat de test
    angajat_test = Angajat('test1', 'test2', 1)
    # verificam ca atributele de instanta s-au initializat cum trebuie
    print(angajat_test.nume == 'test1')
    print(angajat_test.prenume == 'test2')
    print(angajat_test.angajat_id == 1)
    # vreau sa verific ca metoda adauga_concediu adauga un dictionar 'concediu'
    # in lista sa de concedii

    # 1. Verificam ca lista de concedii este goala (inainte sa apelam adauga_concediu)
    # print(len(angajat_test.concedii) == 0)
    if len(angajat_test.concedii) > 0:
        print('Ceva este in neregula, lista de concedii trebuie sa fie goala la initializare')
    else:
        print('Este ok. E ready pt adaugare concedii')
    # 2. Dupa ce apelam adauga_concediu, vrem sa verificam ca lista concedii are 1 element
    angajat_test.adauga_concediu(1, 2)
    print(len(angajat_test.concedii) == 1)
    print(angajat_test.concedii)
    # 3. Vrem sa verificam ca elementul (concediul) din lista concedii are valorile corecte:
    # - zi_start == 1
    # - zi_stop == 2
    # - aprobat == None
    print(angajat_test.concedii[0])
    # print(angajat_test.concedii[0]['zi_start'])
    if angajat_test.concedii[0]['zi_start'] == 1 and angajat_test.concedii[0]['zi_stop'] == 2:
        print('Datele sunt corecte')
    else:
        print('Datele sunt incorecte, codul este prost')

    print(__name__)
