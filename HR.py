from Manager import Manager


class HR(Manager):

    def __init__(self, nume, prenume, angajat_id, manager_id, subalterni, hr_id):
        super().__init__(nume, prenume, angajat_id, manager_id, subalterni)
        self.hr_id = hr_id

    def listeaza_concedii(self):
        for subaltern in self.subalterni:
            for concediu in subaltern.concedii:
                print(f"Angajat {subaltern.nume} {subaltern.prenume}, "
                      f"Concediu {concediu['zi_start']} - {concediu['zi_stop']} "
                      f"{'aprobat' if concediu['aprobat'] else 'respins'}")

    def listeaza_reviewuri(self):
        for subaltern in self.subalterni:
            for review in subaltern.reviews:
                print(f"Angajat {subaltern.nume} {subaltern.prenume}, "
                      f"Comentariu: {review['comentariu']}, nota {review['nota']}")


