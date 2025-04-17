class bb:
    count =0
    @classmethod
    def incre(cls):
        cls.count += 1

bb.incre()
print(bb.count)