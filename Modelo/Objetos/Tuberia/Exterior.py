from Tubo import *


class Exterior (General):
    boca_liner = 0
    CAnular = 0
    VolAnular = 0
    tinterior = ""

    def set_boca_liner(self, dato):
        self.boca_liner = dato

    def get_boca_liner(self):
        return self.boca_liner
