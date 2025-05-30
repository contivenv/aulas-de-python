# verificando lista de pacotes instalados na máquina

# py -m pip list

"""
    Pacotes precisam de algumas dependências para funcionar em nossa máquina, por esse motivo, um pacote puxa para a instalação de outro
    e assim por diante.

    Fizemos a instalação da biblioteca que se chama "matplotlib", que serve basicamente para a exibição de gráficos em nossa tela. Usamos os
    seguintes comandos para que elas fossem baixados: py -m pip install matplotlib.

    Dica: caso você não saiba o nome do pacote que deve instalar ou não sabe ainda o que está precisando ao certo, vá no site https://pypi.org/
    e busque pela biblioteca que está procurando. Lembrando que estou rodando esses comando via Prompt de Comando.

    Para informações específicas do pacote de documentações, tutoriais e etc, você pode colocar na linha de comando sobre o seguinte pacote que
    quer ver: py -m pip show matplotlib

    Para tirar um pacote use: py -m pip uninstall <nome_do_pacote>
""" 