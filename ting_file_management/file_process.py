import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    can_process = True

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            can_process = False

    if can_process:
        process_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(data),
            "linhas_do_arquivo": data,
        }

        instance.enqueue(process_data)
        print(process_data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
