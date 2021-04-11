import threading
from threading import Thread

class Cubul:
    def __init__(self, latura):
        self.latura = latura

    def volumul(self):
        volum = self.latura ** 3
        return volum

    def lungime_totala(self):
        lungime_tot = self.latura * 12
        return lungime_tot

if __name__ == "__main__":
    th1 = threading.Thread(target=Cubul.lungime_totala, args=())
    th2 = threading.Thread(target=Cubul.volumul, args=())

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("Finish")


my_cub1 = Cubul(7)

print("Lungimea totala a laturilor este:", my_cub1.lungime_totala())
print("Volumul este:", my_cub1.volumul())