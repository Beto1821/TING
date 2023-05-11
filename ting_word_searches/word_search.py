def exists_word(word, instance):
    occurrences = []
    for i in range(len(instance)):
        item = instance.search(i)
        found_occurrences = []

        #  itera sobre as linhas do arquivo atual
        #  e retorna o índice e a linha atual.
        for j, line in enumerate(item["linhas_do_arquivo"]):
            # Palavra buscada
            if word.lower() in line.lower():
                found_occurrences.append({"linha": j})

        if found_occurrences:
            # append lista de ocorrencias
            occurrences.append({
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": found_occurrences
            })

    return occurrences


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
