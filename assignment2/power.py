import unittest

def power1(b,n):
    if (n == 0):
        return 1
    elif (n % 2 == 0):
        p = power1(b,int(n/2))
        return p*p
    else:
        p = power1(b,int(n/2))
        if (n  < 0):
            return p*p/b
        else:
            return p*p*b


def power2(b,n):
    if (n == 0):
        return 1
    elif n>0:
        p = power2(b,int(n/2))
        if (n % 2 == 0):
            return p*p
        else:
            return p*p*b
    else:
        p = power2(b,int(n/2))
        if (n % 2 == 0):
            return p*p
        else:
            return p*p/b

def power3(b,n):
    if (n == 0):
        return 1
    else:
        m = abs(n)
        p = power3(b,int(m/2))
        if (m % 2 == 0):
            result = p*p
        else:
            result = p*p*b
        if n<0:
            return  1/result
        else:
            return result

class SearchTest(unittest.TestCase):
    def test_power1(self):
        self.assertAlmostEqual(power1(3,10), 3**10)
        self.assertAlmostEqual(power1(3,-11), 3**-11)
        self.assertAlmostEqual(power1(10,21), 10**21)
        self.assertAlmostEqual(power1(10,-22), 10**-22)

    def test_power2(self):
        self.assertAlmostEqual(power2(3,10), 3**10)
        self.assertAlmostEqual(power2(3,-11), 3**-11)
        self.assertAlmostEqual(power2(10,21), 10**21)
        self.assertAlmostEqual(power2(10,-22), 10**-22)

    def test_power3(self):
        self.assertAlmostEqual(power3(3,10), 3**10)
        self.assertAlmostEqual(power3(3,-11), 3**-11)
        self.assertAlmostEqual(power3(10,21), 10**21)
        self.assertAlmostEqual(power3(10,-22), 10**-22)

if __name__ == '__main__':
    unittest.main()

# def power(b,n):
#     if (n == 0):
#         return 1
#     else:
#         p = power(b,int(n/2))
#         if (n % 2 == 0):
#             return p*p
#         else:
#             return p*p*b


