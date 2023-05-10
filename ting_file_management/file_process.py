import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)  # função import do requisito 01 queue.py
    can_process = True  # variavel para verificação se dados de entrada

    # loop para verificacão se o arquivo existe na fila
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            can_process = False

    # Se o arquivo ainda não foi processado,
    #  é criado um dicionário chamado process_data contendo
    #  as informações do arquivo,
    #  como o nome, a quantidade de linhas e as linhas do arquivo.
    if can_process:
        process_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }

        # dicionário é então adicionado à fila
        #  utilizando o método enqueue, que adiciona o item ao final da fila
        instance.enqueue(process_data)
        print(process_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
