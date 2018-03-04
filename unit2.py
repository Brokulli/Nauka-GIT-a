#! /usr/bin/python

import unittest
import kato
import random
import re

class TestStringMethods(unittest.TestCase):

    # def test_f1_1(self):
    #     k=kato.f1(0) # funkcja f1 zdefiniowana w kato.py
    #     self.assertEqual(k,0)
    #
    # def test_f1_2(self):
    #     k=kato.f1(1)
    #     self.assertEqual(k,1)
    #
    # def test_f1_3(self):
    #     k=kato.f1(2)
    #     self.assertEqual(k,4)

    def test_f1_4(self):
        k=kato.f1(2,1)
        self.assertEqual(k,5)

    def test_f1_5(self):
        k=kato.f1(2,3)
        self.assertEqual(k,7)

    def test_f1_6(self):
        k=kato.f2('ala')
        self.assertEqual(k,'a')

    def test_f1_7(self):
        k=kato.f2([1,2,3])
        self.assertEqual(k,1)

    def test_f1_8(self):
        k=kato.f2([])
        self.assertEqual(k,'BUUUUM')

    def test_f1_9(self):
        k=kato.f3(1)
        self.assertEqual(k,'jeden')

    def test_f1_10(self):
        k=kato.f3(2)
        self.assertEqual(k,'dwa')

    def test_f1_11(self):
        k=kato.f3(3)
        self.assertEqual(k,'trzy')

# jesli nie znajdzie czegos w slowniku (def f3) korzysta z random

    def test_f1_13(self):
        k=kato.f4('ala')
        self.assertEqual(k,'ala ma kota')

    def test_f1_14(self):
        k=kato.f4(0,'kot')
        self.assertEqual(k,'kot ma kota')

    def test_f1_15(self):
        k=kato.f4('kot','psa')
        self.assertEqual(k,'kot ma kota i psa')

    def test_f1_16(self):
        k=kato.f4('kot','mysz')
        self.assertEqual(k,'kot ma kota i mysz')

    def test_f1_17(self):
        k=kato.f5(0)
        self.assertEqual(k,[])

    def test_f1_18(self):
        k=kato.f5(1)
        self.assertEqual(k,[0])

    def test_f1_19(self):
        k=kato.f5(2)
        self.assertEqual(k,[0,1])

    def test_f1_20(self):
        k=kato.f5(7)
        self.assertEqual(k,[0,1,2,3,4,5,6])

    def test_f1_21(self):
        k=kato.f5(7,2)
        self.assertEqual(k,[0,2,4,6])

    def test_f1_22(self):
        k=kato.f5(17,2)
        self.assertEqual(k,[0,2,4,6,8,10,12,14,16])

    def test_f1_23(self):
        k=kato.f5(17,5)
        self.assertEqual(k,[0,5,10,15])

    def test_f1_24(self):
        k=kato.f6(1,'*')
        self.assertEqual(k,'*')

    def test_f1_25(self):
        k=kato.f6(7,'*')
        self.assertEqual(k,'*******')

    def test_f1_26(self):
        k=kato.f7('ala')
        self.assertEqual(k,'slowo')

    def test_f1_27(self):
        k=kato.f7(1)
        self.assertEqual(k,'cyfra')

    def test_f1_28(self):
        k=kato.f7(11111)
        self.assertEqual(k,'liczba')

    def test_f1_29(self):
        k=kato.f7(-11111)
        self.assertEqual(k,'liczba_ze_znakiem')

    def test_f1_30(self):
        k=kato.f7('ala ma kota')
        self.assertEqual(k,'zdanie')


    def test_test(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
