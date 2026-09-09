# 🎮 Projeto Jokenpô

## 👥 Alunos
- **Caio Guilherme**
- **Taina Nakashima**

---

## 📋 Descrição do Projeto

Implementação do clássico jogo de Jokenpô (Pedra, Papel e Tesoura) em Python, com suporte a três modalidades de jogo e múltiplas partidas.

---

## 🎯 Requisitos Implementados

### 1. Regras do Jokenpô
- ✅ Pedra ganha da Tesoura
- ✅ Tesoura ganha do Papel
- ✅ Papel ganha da Pedra

### 2. Modalidades de Jogo
O programa oferece três modos de jogo, selecionados no início da execução:
- **Humano vs Humano** (PvP local)
- **Humano vs Computador** (PvE)
- **Computador vs Computador** (CPU vs CPU)

*A modalidade não pode ser modificada durante a execução.*

### 3. Sistema de Múltiplas Partidas
- Após cada partida, o programa pergunta ao jogador se deseja **CONTINUAR** ou **SAIR**
- O placar geral é atualizado e exibido após cada partida

### 4. Dinâmica das Partidas
- **Jogadores Humanos:** Digitam sua jogada (PEDRA, PAPEL ou TESOURA)
- **Jogadores Computador:** Jogada gerada aleatoriamente
- Exibição automática do vencedor
- Placar geral atualizado em tempo real

### 5. Encerramento
Ao escolher SAIR, o programa:
- Exibe o placar final
- Mostra mensagem de agradecimento com os nomes dos estudantes

### 6. Documentação do Código
- Código comentado e bem estruturado
- Variáveis e funções com nomes descritivos

### 7. Autoria
Este projeto foi implementado respeitando rigorosamente os princípios de integridade acadêmica, com domínio completo do código por ambos os alunos.

---

## 🚀 Como Executar

```bash
python jokenpo.py
```

---

## 🎮 Como Jogar

1. **Selecione a modalidade** ao iniciar o programa:
   - Digite `1` para Humano vs Humano
   - Digite `2` para Humano vs Computador
   - Digite `3` para Computador vs Computador

2. **Em cada partida:**
   - Digite sua jogada (ou deixe o computador jogar)
   - Veja o resultado
   - Escolha continuar ou sair

3. **Ao sair:**
   - Visualize o placar final
   - Mensagem de encerramento

---

## 📊 Exemplo de Execução

```
=== BEM-VINDO AO JOKENPÔ ===

Escolha a modalidade:
1 - Humano vs Humano
2 - Humano vs Computador
3 - Computador vs Computador
Opção: 2

--- PARTIDA 1 ---
Jogador 1, escolha: PEDRA, PAPEL ou TESOURA? pedra
Computador escolheu: tesoura

🎉 Jogador 1 venceu!
Placar: Jogador 1: 1 | Computador: 0 | Empates: 0

Deseja continuar? (S/N): s

--- PARTIDA 2 ---
...
```

---

## 📁 Estrutura do Projeto

```
Projeto_Coop_Jokenpo/
├── README.md
└── jokenpo.py
```

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3.x
- **Módulos:** `random` (para gerações aleatórias)

---

## 📝 Notas Importantes

- Todas as jogadas devem ser inseridas em MAIÚSCULA
- O programa valida automaticamente as entradas
- Empates são contabilizados no placar geral
- A escolha da modalidade é permanente durante a execução

---

## 📞 Contato & Entrega

Atividade de Raciocínio Algorítmico - 2026.02

**Data de Conclusão:** [Data da Entrega]

---

*Desenvolvido com ❤️ por Caio Guilherme e Taina Nakashima*
