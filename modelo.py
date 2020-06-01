#  modelo é utilizado para criação de conceitos de classes
#  para representar dominios no sistema
#  from abc import ABC # abstract base class   o pacote de todas as ABCs criadas é o collections.abc

# from abc import ABCMeta, abstractmethod
# class Programa(metaclass = ABCMeta):
#    @abstractmethod
#    def __str__(self):
#        pass


class Programa:

    def __init__(self, nome_filme, ano):
        self._nome = nome_filme
        self._ano = ano
        self._likes = 0

    def __eq__(self, other):
        return self._nome == other

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    def duration(self):
        return ''

    def __str__(self):
        return f'Nome: {self._nome.title()} - Ano: {self._ano} - {self.duration()} - Likes: {self._likes}'


class Filme(Programa):

    def __init__(self, nome_filme, ano, duracao):
        super().__init__(nome_filme, ano)
        self.duracao = duracao

    def duration(self):
        return "{} min".format(self.duracao)


class Serie(Programa):

    def __init__(self, nome_serie, ano, temporadas):
        super().__init__(nome_serie, ano)
        self.temporadas = temporadas

    def duration(self):
        return "{} temporadas".format(self.temporadas)


class Playlist():
    def __init__(self, nome_playList, programas):  # dunder é o nome do metodo com 2 " _ "
        self.nome = nome_playList
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme("Vingadores", 2014, 160)
atlanta = Serie("Atlanta", 2015, 3)
temp = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

# print(vingadores)
vingadores.give_like()
vingadores.give_like()

# print(atlanta)
atlanta.give_like()
atlanta.give_like()
atlanta.give_like()

temp.give_like()
temp.give_like()
demolidor.give_like()
demolidor.give_like()
demolidor.give_like()

playlist_fim_de_Semana = Playlist('Fim de semana', [vingadores, atlanta, demolidor, temp])

print(f'Tamanho da playlist {len(playlist_fim_de_Semana)}')
print("***************Exibindo a lista de filmes seriado*************")

for programa in playlist_fim_de_Semana:
    detalhes = hasattr(programa, "duracao")  # verifica se a classe possui um atributo especifico
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas  # if em uma linha
    print(programa)

print(f"Tá ou não tá ? {demolidor in playlist_fim_de_Semana}")
