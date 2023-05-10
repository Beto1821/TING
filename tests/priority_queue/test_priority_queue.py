from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Criando uma instância da PriorityQueue
    pq = PriorityQueue()

    # Verificando se a fila está vazia
    assert len(pq) == 0

    # Adicionando arquivos prioritários
    pq.enqueue({"nome_do_arquivo": "arq1.txt", "qtd_linhas": 4,
                "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4"]})
    pq.enqueue({"nome_do_arquivo": "arq2.txt", "qtd_linhas": 2,
                "linhas_do_arquivo": ["linha1", "linha2"]})

    # Verificando se os arquivos foram adicionados corretamente e
    #  na ordem esperada
    assert len(pq) == 2
    assert pq.search(0) == {"nome_do_arquivo": "arq2.txt", "qtd_linhas": 2,
                            "linhas_do_arquivo": ["linha1", "linha2"]}
    assert pq.search(1) == {"nome_do_arquivo": "arq1.txt", "qtd_linhas": 4,
                            "linhas_do_arquivo": ["linha1", "linha2", "linha3",
                                                  "linha4"]}

    # Adicionando arquivos não-prioritários
    pq.enqueue({"nome_do_arquivo": "arq3.txt", "qtd_linhas": 5,
                "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4",
                                      "linha5"]})
    pq.enqueue({"nome_do_arquivo": "arq4.txt", "qtd_linhas": 3,
                "linhas_do_arquivo": ["linha1", "linha2", "linha3"]})

    # Verificando se os arquivos foram adicionados corretamente e
    #  na ordem esperada
    assert len(pq) == 4
    assert pq.search(0) == {"nome_do_arquivo": "arq2.txt", "qtd_linhas": 2,
                            "linhas_do_arquivo": ["linha1", "linha2"]}
    assert pq.search(1) == {"nome_do_arquivo": "arq1.txt", "qtd_linhas": 4,
                            "linhas_do_arquivo": ["linha1", "linha2", "linha3",
                                                  "linha4"]}
    assert pq.search(2) == {"nome_do_arquivo": "arq4.txt", "qtd_linhas": 3,
                            "linhas_do_arquivo": ["linha1", "linha2",
                                                  "linha3"]}
    assert pq.search(3) == {"nome_do_arquivo": "arq3.txt", "qtd_linhas": 5,
                            "linhas_do_arquivo": ["linha1", "linha2", "linha3",
                                                  "linha4", "linha5"]}

    # Removendo arquivos da fila
    assert pq.search() == {"nome_do_arquivo": "arq2.txt", "qtd_linhas": 2,
                           "linhas_do_arquivo": ["linha1", "linha2"]}
    assert pq.search() == {"nome_do_arquivo": "arq1.txt", "qtd_linhas": 4,
                           "linhas_do_arquivo": ["linha1", "linha2", "linha3",
                                                 "linha4"]}
    assert pq.search() == {"nome_do_arquivo": "arq4.txt", "qtd_linhas": 3,
                           "linhas_do_arquivo": ["linha1", "linha2", "linha3"]}
    assert pq.search() == {"nome_do_arquivo": "arq3.txt", "qtd_linhas": 5,
                           "linhas_do_arquivo": ["linha1", "linha2", "linha3",
                                                 "linha4", "linha5"]}
