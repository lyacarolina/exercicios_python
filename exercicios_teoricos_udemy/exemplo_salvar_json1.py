import json

CAMINHO_ARQUIVO = 'exemplo.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

bd = [vars(p1), p2.__dict__, p3.__dict__] #tanto faz usar .__dict__, ou vars()

def fazer_dump():
    with open(CAMINHO_ARQUIVO,  'w') as arquivo:
        print('fazer dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
        
if __name__ == '__main__':
    print("ele é o main")
    fazer_dump()