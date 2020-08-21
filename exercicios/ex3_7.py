lista_de_convidados = ['Elon Musk', 'Monark', 'Duda Matte', 'Jesus Cristo', 'Augusto Cury', 'Eminem', 'Marcelinho Carioca']
print(f'Salve, {lista_de_convidados[0]}. Venho por meio dessa mensagem tá te convidando ai pra uma janta deliciossima na minha goma, espero que você brote, quero muito conversar com você sobre coisas do futuro.\n')
print(f'Salve, {lista_de_convidados[1]}. Venho por meio dessa mensagem te convidar pra uma janta, já que você é uma pessoa muito legal e eu consegui mais 3 vagas.\n')
print(f'Salve, {lista_de_convidados[2]}. Venho por meio dessa mensagem primeiramente pra falar que você é muito bonita e queria tá ai te convidando pra gente troca umas ideia na minha goma e pa. Tmj\n')
print(f'Salve, {lista_de_convidados[3]}. Venho por meio dessa mensagem estar ai te convidando pra uma janta, espero que o senhor compareça, sempre quis falar muito com o senhor, pelo que eu sei você é uma pessoa muito inteligente e seria um prazer te ter aqui na minha goma, tmj Jesus.\n')
print(f'Salve, {lista_de_convidados[4]}. Venho por meio dessa mensagem chamar você para uma janta aqui em casa, passar umas ideia pra gente do psicológico, sei que você manda muito nessa área, tmj.')
print(f'Salve, {lista_de_convidados[5]}. Venho por meio dessa mensagem te convidar para um jantar, já que o Sócrates não pode vir, é claro que eu gosto muito de você, mas só havia 4 vagas e depois pensei em você. Espero que compareça, gosto muito do seu trabalho.\n')
print(f'Salve, {lista_de_convidados[6]}. Venho por meio dessa mensagem te convidar pra uma janta aqui em casa, sei que você manja de uns exercícios ai, espero que brote pra passar uns exercícios pra gente depois da comida.\n')
print(f'Salve {lista_de_convidados}, acabei de descobrir que a mesa de jantar não chegará a tempo para o jantar e tenho apenas espaço para dois convidados.\n')
elon_musk = lista_de_convidados.pop(0) # remove o index 0 da lista, mas armazena na variavel.
print(f'Oi {elon_musk}, sinto muito em não poder te convidar ao jantar.\n')
monark = lista_de_convidados.pop(0)
print(f'Oi {monark}, sinto muito em não poder te convidar ao jantar.\n')
augusto = lista_de_convidados.pop(2)
print(f'Oi {augusto}, sinto muito em não poder te convidar ao jantar.\n')
eminem = lista_de_convidados.pop(2)
print(f'Oi {eminem}, sinto muito em não poder te convidar ao jantar.\n')
marcelinho_carioca = lista_de_convidados.pop(2)
print(f'Oi {marcelinho_carioca}, sinto muito em não poder te convidar ao jantar.\n')
print(f'Olá {lista_de_convidados[0]}, te deixei na lista da janta, pois gosto muito de você e acredito que teremos uma ótima conversa!\n')
print(f'Olá {lista_de_convidados[1]}, te deixei na lista da janta, gosto muito do senhor e acredito que teremos uma ótima conversa juntos!\n')
del lista_de_convidados[0]
del lista_de_convidados[0]
print(lista_de_convidados)