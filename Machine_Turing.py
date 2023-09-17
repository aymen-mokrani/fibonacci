class Machine_Turing :
    def __init__(self, etats,alphabets, transitions):
        self.etats = etats
        self.transitions = transitions
        self.etat = etat_initial
        self.alphabets = alphabets
        self.etat_initial = ''
        self.etat_accepte = ''
        self.etat_rejecte = ''
        self.mot = []
        self.position = 0
    

    
    def entree(self, mot, etat_initial, etat_accepte, etat_rejecte):
        self.etat_initial = etat_initial
        self.etat_accepte = etat_accepte
        self.etat_rejecte = etat_rejecte
        self.mot = list(mot)
    
    def demarrer(self):
        print ( '\n----------Machine De Turing----------\n')
        print('Notre mot est :')
        self.mot.append('#')
        self.mot.append('&')
        for i in self.mot:
            print(f'|{i}', end="")
        print('|')
        print(' ↑\n')
        while True :

            if self.etat == self.etat_accepte:
                return 'Accepté'
            if self.etat == self.etat_rejecte:
                return 'rejecté'
            if (self.etat,self.mot[self.position]) not in self.transitions:
                return 'rejecté'
            
            alphabet_actuel = self.mot[self.position]

            self.etat,alphabet_prochaine, direction = self.transitions[(self.etat,alphabet_actuel)]

            if direction == 'D':
                self.mot[self.position]=alphabet_prochaine
                self.position+=1
                for i in self.mot:
                    print(f'|{i}', end="")
                print('|')
                for i in range(self.position):
                    print('  ',end='')
                print(' ↑',end='')
                print(f'---- {self.etat}\n')
            elif direction == 'G':
                self.mot[self.position]=alphabet_prochaine
                self.position-=1
                for i in self.mot:
                    print(f'|{i}', end="")
                print('|')
                for i in range(self.position):
                    print('  ',end='')
                print(' ↑',end='')
                print(f'---- {self.etat}\n')
            if alphabet_actuel == "&":
                self.position-=1

if __name__ == '__main__':

    # Exemple d'utilisation
    etats = {'q0', 'q1', 'q2'}
    alphabets = {'0', '1'}
    transitions = {('q0', '0'): ('q1', '1', 'D'),
                   ('q0', '1'): ('q3', '1', 'D'),
                   ('q1', '0'): ('q1', '0', 'D'),
                   ('q1', '1'): ('q2', '1', 'D'),
                   ('q2', '0'): ('q2', '0', 'D'),
                   ('q2', '1'): ('q2', '0', 'D'),
                   ('q3', '1'): ('q2', '1', 'I')}
    etat_initial = 'q0'
    etat_accepte = 'q2'
    etat_rejecte = 'q3'

    mt = Machine_Turing(etats, alphabets, transitions)
    entree = "0011001"
    mt.entree(entree,etat_initial, etat_accepte, etat_rejecte)
    resultat = mt.demarrer()
    print(resultat) 

