
import random

class lotto:


    def lottery(self):
        lottoNumber = []
        for i in range(0,6):
            num = random.randint(1,45)
            while num in lottoNumber:
                num = random.randint(1,45)
            lottoNumber.append(num)
            lottoNumber.sort()
        return lottoNumber

if __name__=="__main__":
    a = lotto()


    print(a.lottery())