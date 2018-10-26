class Buffer:
    def __init__(self):
        self.now = []

    def add(self, *a):
        for each in a:
            self.now.append(int(each))
        while len(self.now) >= 5:
            ans = 0
            for each in range(5):
                ans += self.now.pop(0)
            print(ans)

    def get_current_part(self):
        print(self.now)
