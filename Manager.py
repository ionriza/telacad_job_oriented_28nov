from Angajat import Angajat


class Manager(Angajat):

    def __init__(self, nume, prenume, angajat_id, manager_id, subalterni):
        super().__init__(nume, prenume, angajat_id)
        self.manager_id = manager_id
        self.subalterni = subalterni

    def adauga_review(self, angajat, comentariu, nota):
        review = {
            'comentariu': comentariu,
            'nota': nota
        }
        angajat.reviews.append(review)
        print(f"Manager {self.nume} {self.prenume} lasa review-ul: "
              f"{review['comentariu']} cu nota {review['nota']} "
              f"lui {angajat.nume}")

    def aproba_concedii(self):
        for subaltern in self.subalterni:
            for concediu in subaltern.concedii:
                if concediu['aprobat'] is None:
                    raspuns_concediu = input(
                        f"Accepti concediul lui {subaltern.nume} "
                        f"incepand cu data {concediu['zi_start']} "
                        f"pana la {concediu['zi_stop']} ?")
                    if raspuns_concediu == 'da':
                        concediu['aprobat'] = True
                    elif raspuns_concediu == 'nu':
                        concediu['aprobat'] = False
                    else:
                        print('Nu ai introdus valoarea corecta (da/nu)')
                else:
                    print(f"Concediul lui {subaltern.nume}: "
                          f"{concediu['zi_start']} - {concediu['zi_stop']} "
                          f"este {'aprobat' if concediu['aprobat'] else 'respins'}")
