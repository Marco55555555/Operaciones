import math
def print_hi(name):
    print(f'Hi, {name}')
# Suma
def sumacplx(c1,c2):
    parteR=c1[0]+c2[0]
    parteI=c1[1]+c2[1]
    return(parteR,parteI)
# Resta
def restacplx(a1,a2):
    parteR=a1[0]-a2[0]
    parteI=a1[1]-a2[1]
    return(parteR,parteI)
# Multiplicación
def multicplx(b1,b2):
    parteR=((b1[0]*b2[0])-(b1[1]*b2[1]))
    parteI=(b1[0]*b2[1])+(b2[0]*b1[1])
    return(parteR,parteI)
# División
def divcplx(e1,e2):
    parteR= (((e1[0]*e2[0])+(e1[1]*e2[1]))/((e2[0]**2)+(e2[1]**2)))
    parteI= (((e2[0]*e1[1])-(e1[0]*e2[1]))/((e2[0]**2)+(e2[1]**2)))
    return(parteR,parteI)
#Módulo
def modulocplx(m1,m2):
    parteR= ((m1**2)+(m2**2))**(1/2)
    return(parteR)
#Conjugado
def conjugadocplx(j1,j2):
    parteR= j1
    parteI= -j2
    return(parteR,parteI)
#Conversión polar a cartesiano
def conversptoccplx(t1,t2):
    parteR= t1*math.cos(math.radians(t2))
    parteI= t1*math.sin(math.radians(t2))
    return(parteR,parteI)
#Conversión cartesiano a polar
def conversctopcplx(u1,u2):
    parteR= ((u1**2)+(u2**2))**(1/2)
    x= math.degrees(math.atan(u2/u1))
    if u1>0 and u2>0:
        parteI=x
    elif u1<0 and u2<0:
        parteI=x+180
    elif u1>0 and u2<0:
        parteI=360-x
    elif u1<0 and u2>0:
        parteI=180-x
    return(parteR,parteI)
#Fase de un número
def fasecplx(f1,f2):
    x= math.degrees(math.atan(f2/f1))
    if f1>0 and f2>0:
        angulo=x
    elif f1<0 and f2<0:
        angulo=x+180
    elif f1>0 and f2<0:
        angulo=360-x
    elif f1<0 and f2>0:
        angulo=180-x
    return(angulo)
if __name__ == '__main__':
    print(sumacplx((3,2),(-5,5.2)))
    print(restacplx((3,2),(-5,5.2)))
    print(multicplx((3,2),(-5,5.2)))
    print(divcplx((3,2),(-5,5.2)))
    print(modulocplx((3),(-5.2)))
    print(conjugadocplx((3),(-5.2)))
    print(conversptoccplx((2),(-75)))
    print(conversctopcplx((3*((3)**(1/2))),(3)))
    print(fasecplx((3),(-5.2)))
import unittest
class TestCibreriaComplejos(unittest.TestCase):

    # Casos prueba de la suma
    def test_sumacplx(self):
        # Primer caso de prueba
        suma1 = sumacplx((3, 2), (-5, 5.2))
        self.assertAlmostEqual(suma1[0], -2)
        self.assertAlmostEqual(suma1[1], 7.2)
        # Segundo caso de prueba
        suma2 =sumacplx((10, 3), (9, 2))
        self.assertAlmostEqual(suma2[0], 19)
        self.assertAlmostEqual(suma2[1], 5)
# Casos prueba de la resta
    def test_restacplx(self):
        # Primer caso de prueba
        resta1 = restacplx((3, 2), (-5, 5.2))
        self.assertAlmostEqual(resta1[0], 8)
        self.assertAlmostEqual(resta1[1], -3.2)
        # Segundo caso de prueba
        resta2 = restacplx((10, 3), (9, 2))
        self.assertAlmostEqual(resta2[0], 1)
        self.assertAlmostEqual(resta2[1], 1)

    # Casos prueba de la multiplicación
    def test_multiplicacioncplx(self):
        # Primer caso de prueba
        multi1 = multicplx((3, 2), (-5, 5.2))
        self.assertAlmostEqual(multi1[0], -25.4)
        self.assertAlmostEqual(multi1[1], 5.6)
        # Segundo caso de prueba
        multi2 = multicplx((10, 3), (9, 2))
        self.assertAlmostEqual(multi2[0], 84)
        self.assertAlmostEqual(multi2[1], 47)

    # Casos prueba de la división
    def test_divisioncplx(self):
        # Primer caso de prueba
        div1 = divcplx((5, 10), (4, 3))
        self.assertAlmostEqual(div1[0], 2)
        self.assertAlmostEqual(div1[1], 1)
        # Segundo caso de prueba
        div2 = divcplx((-4, -4), (-4, 4))
        self.assertAlmostEqual(div2[0], 0)
        self.assertAlmostEqual(div2[1], 1)

    # Casos de prueba del módulo
    def test_modulocplx(self):
        # Primer caso de prueba
        mod1 = modulocplx(0, -2)
        self.assertAlmostEqual(mod1, 2)
        # Segundo caso de prueba
        mod2 = modulocplx(3, -1)
        self.assertAlmostEqual(mod2, 3.16227766)

    # Casos de prueba del conjugado
    def test_conjugado(self):
        # Primer caso de prueba
        con1 = conjugadocplx(5, -5)
        self.assertAlmostEqual(con1[0], 5)
        self.assertAlmostEqual(con1[1], 5)
        # Segundo caso de prueba
        con2 = conjugadocplx(34, 345)
        self.assertAlmostEqual(con2[0], 34)
        self.assertAlmostEqual(con2[1], -345)

    # Casos de prueba conversión polar a cartesiano
    def test_convptoc(self):
        # Primer caso de prueba
        ptoc1 = conversptoccplx(2, 120)
        self.assertAlmostEqual(ptoc1[0], -1)
        self.assertAlmostEqual(ptoc1[1], 1.732050808)
        # Segundo caso de prueba
        ptoc2 = conversptoccplx(2, -75)
        self.assertAlmostEqual(ptoc2[0], 0.517638090)
        self.assertAlmostEqual(ptoc2[1], -1.93185165)

    # Casos de prueba conversión cartesiano a polar
    def test_convctop(self):
        # Primer caso de prueba
        ctop1 = conversctopcplx(1, (3 ** (1 / 2)))
        self.assertAlmostEqual(ctop1[0], 2)
        self.assertAlmostEqual(ctop1[1], 60)
        # Segundo caso de prueba
        ctop2 = conversctopcplx(-1, -(3 ** (1 / 2)))
        self.assertAlmostEqual(ctop2[0], 2)
        self.assertAlmostEqual(ctop2[1], 240)

    # Casos de prueba retorno de fase de un número complejo
    def test_fasecplx(self):
        # Primer caso de prueba
        fase1 = fasecplx(-1, -(3 ** (1 / 2)))
        self.assertAlmostEqual(fase1, 240)
        # Segundo caso de prueba
        fase2 = fasecplx(1, (3 ** (1 / 2)))
        self.assertAlmostEqual(fase2, 60)
