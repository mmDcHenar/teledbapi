from threading import Thread
from re import search


class Search:
    def __init__(self, cmd):
        self.threads = []
        self.result = 0
        self.start(cmd)
        self.join()

    def __repr__(self):
        return self.result

    def search(self, file, cmd):
        with open(file) as users:
            for user in users:
                if not self.result:
                    if cmd in user:
                        data = search('''{'id': (.*)?, 'username': '(.*)?', 'phone': '(.*)?'}''', user)
                        self.result = {'id': data[1], 'username': data[2], 'phone': data[3]}
                else:
                    break
            return False

    def start(self, cmd):
        t0 = Thread(target=self.search, args=['0.txt', cmd])
        self.threads.append(t0)
        t1 = Thread(target=self.search, args=['1.txt', cmd])
        self.threads.append(t1)
        t2 = Thread(target=self.search, args=['2.txt', cmd])
        self.threads.append(t2)
        t3 = Thread(target=self.search, args=['3.txt', cmd])
        self.threads.append(t3)
        t4 = Thread(target=self.search, args=['4.txt', cmd])
        self.threads.append(t4)
        t5 = Thread(target=self.search, args=['5.txt', cmd])
        self.threads.append(t5)
        t6 = Thread(target=self.search, args=['6.txt', cmd])
        self.threads.append(t6)
        t7 = Thread(target=self.search, args=['7.txt', cmd])
        self.threads.append(t7)
        t8 = Thread(target=self.search, args=['8.txt', cmd])
        self.threads.append(t8)

        for thread in self.threads:
            thread.start()

    def join(self):
        for thread in self.threads:
            thread.join()
