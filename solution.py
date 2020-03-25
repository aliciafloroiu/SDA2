from problem import Problem
import random
from random import sample
import string


def sample_string(sir, lungime):
    rez = []
    for i in range(lungime):
        ch = random.choice(sir)
        rez.append(ch)
    return rez


class Problem30(Problem):
    def __init__(self):
        statement = ""
        litere = ['a', 'b', 'c', 'd', 'e']
        l = random.randint(3, 5)
        v = sample_string(litere, l)

        statement += 'Se da sirul: ' + str(v) + '.\n'
        statement += 'Gasiti numarul minim de litere (si literele) care trebuie introduse astfel incat sirul sa devina palindrom.'
        data = [v]
        super().__init__(statement, data)


    def solve(self):
        v = self.data[0]
        l = len(v)
        solution = ''
        solution += '\n Scriem sirul invers: '
        w = v[::-1]
        solution += str(w) + '\n'
        
        if v==v[::-1]:
            solution+= '\n Sirul este deja un palindrom.'
        else:
            LCS = [[ 0 for i in range(len(v)+1)] for j in range(len(v)+1)]

            for i in range(l):
                for j in range(l):
                    LCS[0][j]=0
                    LCS[i][0]=0

            for i in range(1,l+1):
                for j in range(1, l+1):
                    if v[i-1] == w[j-1]:
                        #solution += str(v[i-1]) + '=' + str(w[j-1]) +'\n'
                        LCS[i][j] = 1 + LCS[i - 1][j - 1]
                    else:
                        LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

            solution+= "\n Calculam valorile matricei LCS ce are pe linie sirul initial, iar pe diagonala sirul scris invers."
            solution += '\n Se ia fiecare element de pe coloana si se compara cu elementele sirului de pe linie dupa regula urmatoare:\n'
            solution += '       * daca elementele sunt egale => LCS[i][j] = 1 + LCS[i - 1][j - 1] \n'
            solution += '       * daca elementele nu sunt egale => LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])\n'
            for i in range(len(LCS)):
                for j in range(len(LCS)):
                    solution+= '\t' + str(LCS[i][j])
                solution+= "\n"

            solution += ' Numarul de litere care trebuie introdus este diferenta dintre lungimea sirului si ultimul element al matrice.\n'
            ultim_elem = LCS[l][l]
            nr_litere = l - ultim_elem

            solution += '\nTrebuie introduse ' + str(nr_litere) + ' litere.'

        return solution