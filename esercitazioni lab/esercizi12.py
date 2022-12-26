# Ignorare le righe fino alla 31
import json
from typing import Any, Callable, List


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}.\n'
              f'Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Helper functions
def load_json(filename):
    with open(filename) as f:
        return json.load(f)


# Helper functions
def save_json(filename, js):
    with open(filename, 'w') as f:
        json.dump(js, f, indent=2)


# Helper functions
def from_json1(filename):
    def convert(d):
        return Node(tag=d['tag'] if 'tag' in d else '', nodes=[convert(n) for n in d['nodes']] if 'nodes' in d else [])

    return convert(load_json(filename))


# Helper functions
def from_json2(filename):
    def convert(d):
        return Internal(nodes=[convert(n) for n in d['nodes']]) if 'nodes' in d else Leaf(tag=d['tag'])

    return convert(load_json(filename))


# Questo esercizio differisce dai precedenti perchè implementeremo sia funzione
# che classi. Ci focalizzeremo su due modi diversi di implemetare gli alberi.
# Nel resto di questo esercizio, chiameremo nodi interni i nodi che contengono
# altri nodi, mentre useremo il nome foglie per i nodi che non contengono altri
# nodi.
# In questo esercizio, il codice da scrivere è molto poco, ma richiede di capire
# bene come rappresentare gli alberi.


# Implementare la classe Node che rappresenta un nodo di un albero.
# Ogni nodo contiene due variabili: una stringa chiamata tag e una lista di
# nodi chiamati nodes. Il construttore prende come parametri opzionali tag e nodes.
# Si ricorda che nodes va copiato per evitare problemi.
# Implementare __repr__ e __eq__
class Node:
    def __init__(self, tag: str, nodes: list):
        self.tag = tag
        self.nodes = nodes.copy()

    def __eq__(self, other):
        if issubclass(other, Node):
            return self.tag == other.tag and self.nodes == other.nodes
        raise AttributeError

    def __repr__(self):
        return f'Node(tag={repr(self.tag)}, nodes={repr(self.nodes)})'


# Implementare una funzione ricorsiva che conta il numero di nodi di un albero.
def num_nodes(node: Node) -> int:
    return 1 + sum(num_nodes(child) for child in node.nodes)


# Implementare una funzione ricorsiva che conta il numero di foglie di un albero.
def num_leaves(node: Node) -> int:
    return sum(num_leaves(child) for child in node.nodes) if node.nodes else 1


# Implementare una funzione ricorsiva che ritorna una stringa ottenuta
# concatenando le stringhe tag di tutti i nodi.
def get_alltags(node: Node) -> str:
    return node.tag + ''.join(get_alltags(child) for child in node.nodes)


# Implementare una funzione che converte un dizionario che rappresenta un albero, le cui chiavi
# sono i parametri del construttore. Vedere il file tree01.json per avere un'idea di come il dizionario
# definisce ricorsivamente l'albero.
def from_dict(d: dict) -> Node:
    return Node(
        tag=d.get('tag', ''),
        nodes=[from_dict(n) for n in d['nodes']] if 'nodes' in d else [],
    )


# Implementare una funzione che converte un node in un dizionario ricorsivo.
def to_dict(node: Node) -> dict:
    diz = {"tag": node.tag, "nodes": []}
    for n in node.nodes:
        diz["nodes"] += [to_dict(n)]
    return diz


# Nella seconda parte di questo esercizio implementeremo le stesse funzionalità
# su un albero eterogeneo. In questo albero, i nodi interni sono di classe
# Internal e contengono solo altri nodi, mentre i nodi foglia sono di classe
# Leaf e contengono solo tag. Internal e Leaf derivano da una classe Tree.

# In questa seconda implemetazione, le funzionalità descritte prima vanno
# implementate come metodi sulle classi. Avremo quindi metodi num_nodes(),
# num_leaves(), get_alltags() e to_dict(). Per from_dict() definiamo un
# metodo di classe in Tree.

# Implementare __eq__ e __repr__ in Internal e Leaf

class Tree:
    def __init__(self) -> None:
        pass

    def num_nodes(self) -> int: return 1

    def num_leaves(self) -> int: return 0

    def get_alltags(self) -> str: return ''

    def to_dict(self) -> dict: return {}

    def __repr__(self) -> str:
        return 'Tree()'

    @staticmethod
    def from_dict(d: dict):
        return Internal.from_dict(d) if 'tag' not in d else Leaf.from_dict(d)


class Internal(Tree):
    def __init__(self, nodes=None) -> None:  # sourcery skip: default-mutable-arg
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def num_nodes(self) -> int:
        return 1 + sum(n.num_nodes() for n in self.nodes)

    def num_leaves(self) -> int:
        return sum(n.num_leaves() for n in self.nodes)

    def get_alltags(self) -> str:
        return ''.join(n.get_alltags() for n in self.nodes)

    def to_dict(self) -> dict:
        return {'nodes': [n.to_dict() for n in self.nodes]}

    def __repr__(self) -> str:
        return f'Internal(nodes={repr(self.nodes)})'

    def __eq__(self, o) -> bool:
        return self.nodes == o.nodes

    @staticmethod
    def from_dict(d: dict):
        return Internal(nodes=[Tree.from_dict(n) for n in d['nodes']])


class Leaf(Tree):
    def __init__(self, tag='') -> None:
        self.tag = tag

    def num_leaves(self) -> int: return 1

    def get_alltags(self) -> str:
        return self.tag

    def to_dict(self) -> dict:
        return {'tag': self.tag}

    def __repr__(self) -> str:
        return f'Leaf(tag={repr(self.tag)})'

    def __eq__(self, o) -> bool:
        return self.tag == o.tag

    @staticmethod
    def from_dict(d: dict):
        return Leaf(d['tag'])


# Test funzioni
check_test(num_nodes, 5, from_json1('tree01.json'))
check_test(num_leaves, 3, from_json1('tree01.json'))
check_test(get_alltags, 'Rickard Stark, padre di Eddard Stark (padre di Robb e Arya ) e Benjen Stark',
           from_json1('tree01.json'))
check_test(to_dict, {'tag': 'Rickard Stark, padre di ',
                     'nodes': [{'tag': 'Eddard Stark (padre di ', 'nodes': [{'tag': 'Robb e ', 'nodes': []},
                                                                            {'tag': 'Arya ', 'nodes': []}]},
                               {'tag': ') e Benjen Stark', 'nodes': []}]}, from_json1('tree01.json'))
# For some reason it doesn't pass even with the solution given by the teacher
check_test(from_dict, from_json1('tree01.json'), load_json('tree01.json'))
check_test(lambda node: node.num_nodes(), 5, from_json2('tree02.json'))
check_test(lambda node: node.num_leaves(), 3, from_json2('tree02.json'))
check_test(lambda node: node.get_alltags(),
           'Robb e Arya ) e Benjen Stark', from_json2('tree02.json'))
check_test(lambda node: node.to_dict(),
           {'nodes': [{'nodes': [{'tag': 'Robb e '}, {'tag': 'Arya '}]}, {'tag': ') e Benjen Stark'}]},
           from_json2('tree02.json'))
check_test(Tree.from_dict, from_json2('tree02.json'), load_json('tree02.json'))
