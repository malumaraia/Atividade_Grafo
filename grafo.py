# Atividade_Grafo
# ==========================================
# REDE DE DISCIPLINAS E PRÉ-REQUISITOS
# Modelagem de grafo direcionado em Python
# ==========================================

def adicionar_disciplina(grafo, disciplina):
    if disciplina not in grafo:
        grafo[disciplina] = []
        print(f"✅ Disciplina '{disciplina}' adicionada com sucesso.")
    else:
        print("⚠️ Essa disciplina já existe.")


def remover_disciplina(grafo, disciplina):
    if disciplina in grafo:
        grafo.pop(disciplina)
        for prereqs in grafo.values():
            if disciplina in prereqs:
                prereqs.remove(disciplina)
        print(f"🗑️ Disciplina '{disciplina}' removida.")
    else:
        print("⚠️ Disciplina não encontrada.")


def adicionar_prerequisito(grafo, prereq, disciplina):
    if prereq in grafo and disciplina in grafo:
        if disciplina not in grafo[prereq]:
            grafo[prereq].append(disciplina)
            print(f"✅ '{prereq}' agora é pré-requisito de '{disciplina}'.")
        else:
            print("⚠️ Essa relação já existe.")
    else:
        print("⚠️ Uma das disciplinas não existe.")


def remover_prerequisito(grafo, prereq, disciplina):
    if prereq in grafo and disciplina in grafo[prereq]:
        grafo[prereq].remove(disciplina)
        print(f"🗑️ Pré-requisito '{prereq} -> {disciplina}' removido.")
    else:
        print("⚠️ Relação não encontrada.")


def consultar_prerequisitos(grafo, disciplina):
    prereqs = [d for d, deps in grafo.items() if disciplina in deps]
    if prereqs:
        print(f"📘 Pré-requisitos de '{disciplina}': {', '.join(prereqs)}")
    else:
        print(f"📘 '{disciplina}' não possui pré-requisitos.")


def existe_dependencia(grafo, origem, destino, visitados=None):
    if visitados is None:
        visitados = set()
    if origem == destino:
        return True
    visitados.add(origem)
    for vizinho in grafo[origem]:
        if vizinho not in visitados:
            if existe_dependencia(grafo, vizinho, destino, visitados):
                return True
    return False


def tem_ciclo(grafo):
    visitados = set()
    pilha = set()

    def dfs(v):
        visitados.add(v)
        pilha.add(v)
        for vizinho in grafo[v]:
            if vizinho not in visitados:
                if dfs(vizinho):
                    return True
            elif vizinho in pilha:
                return True
        pilha.remove(v)
        return False

    for v in grafo:
        if v not in visitados:
            if dfs(v):
                return True
    return False


def ordenacao_topologica(grafo):
    visitados = set()
    ordem = []

    def dfs(v):
        visitados.add(v)
        for vizinho in grafo[v]:
            if vizinho not in visitados:
                dfs(vizinho)
        ordem.append(v)

    for v in grafo:
        if v not in visitados:
            dfs(v)
    ordem.reverse()
    return ordem


def caminho_ate(grafo, inicio, fim, caminho=None):
    if caminho is None:
        caminho = [inicio]
    if inicio == fim:
        return caminho
    for vizinho in grafo[inicio]:
        if vizinho not in caminho:
            novo_caminho = caminho_ate(grafo, vizinho, fim, caminho + [vizinho])
            if novo_caminho:
                return novo_caminho
    return None


# ==========================================
# MENU INTERATIVO
# ==========================================

def mostrar_menu():
    print("\n===== REDE DE DISCIPLINAS =====")
    print("1. Adicionar disciplina")
    print("2. Remover disciplina")
    print("3. Adicionar pré-requisito")
    print("4. Remover pré-requisito")
    print("5. Consultar pré-requisitos de uma disciplina")
    print("6. Verificar dependência entre duas disciplinas")
    print("7. Verificar se há ciclos")
    print("8. Gerar ordem de disciplinas (ordenação topológica)")
    print("9. Visualizar caminho até uma disciplina final")
    print("0. Sair")
    return input("Escolha uma opção: ")


def main():
    grafo = {}

    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            d = input("Nome da disciplina: ")
            adicionar_disciplina(grafo, d)

        elif opcao == "2":
            d = input("Nome da disciplina a remover: ")
            remover_disciplina(grafo, d)

        elif opcao == "3":
            p = input("Nome do pré-requisito: ")
            d = input("Nome da disciplina: ")
            adicionar_prerequisito(grafo, p, d)

        elif opcao == "4":
            p = input("Nome do pré-requisito: ")
            d = input("Nome da disciplina: ")
            remover_prerequisito(grafo, p, d)

        elif opcao == "5":
            d = input("Nome da disciplina: ")
            consultar_prerequisitos(grafo, d)

        elif opcao == "6":
            o = input("Disciplina de origem: ")
            d = input("Disciplina de destino: ")
            if o in grafo and d in grafo:
                dep = existe_dependencia(grafo, o, d)
                print("🔗 Existe dependência?" , "Sim" if dep else "Não")
            else:
                print("⚠️ Uma das disciplinas não existe.")

        elif opcao == "7":
            print("♻️ O grafo possui ciclos?", "Sim" if tem_ciclo(grafo) else "Não")

        elif opcao == "8":
            ordem = ordenacao_topologica(grafo)
            print("📚 Ordem possível de conclusão:")
            print(" → ".join(ordem))

        elif opcao == "9":
            i = input("Disciplina inicial: ")
            f = input("Disciplina final: ")
            if i in grafo and f in grafo:
                caminho = caminho_ate(grafo, i, f)
                if caminho:
                    print("🧭 Caminho:", " → ".join(caminho))
                else:
                    print("⚠️ Não há caminho entre essas disciplinas.")
            else:
                print("⚠️ Uma das disciplinas não existe.")

        elif opcao == "0":
            print("👋 Encerrando o programa...")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()