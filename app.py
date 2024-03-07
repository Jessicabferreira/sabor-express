import os

print("""𝗦𝗮𝗯𝗼𝗿 𝗘𝘅𝗽𝗿𝗲𝘀𝘀\n""")

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')


opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')


if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    finalizar_app()
