# Zenyx AI — TinyV1

> 🇧🇷 Modelo experimental de linguagem em desenvolvimento. **Não é um chatbot pronto para uso.**

A **Zenyx TinyV1** é o primeiro checkpoint público do projeto Zenyx AI, mantido por [Igor Oliveira](https://github.com/igoroliveiradevv).

## Estado atual

O pacote `LLM_BR_Tiny_v1_backup.zip` contém:

| Arquivo | Finalidade |
|---|---|
| `latest.msgpack` | Estado de treinamento serializado |
| `tokenizer.model` | Modelo do tokenizador (formato SentencePiece) |
| `config.json` | Hiperparâmetros e metadados |

**Configuração registrada no backup:** 4 camadas, 4 cabeças de atenção, largura de 256, sequência de até 256 tokens, vocabulário de 6.430 tokens e tamanho de lote 16. O campo `total_steps=50000` configura a meta de passos; **não comprova** que tantos passos já foram concluídos.

⚠️ O ZIP **não inclui** a definição Python da arquitetura, rotina de inferência nem código original de treinamento. Um checkpoint sozinho não executa o modelo. Evite prometer respostas, compatibilidade com Transformers ou continuidade de treinamento até que o código correspondente seja disponibilizado e testado.

## Download e instalação

1. Visite [Releases](https://github.com/igoroliveiradevv/zenyxai/releases) e baixe o ZIP **quando o arquivo estiver anexado à release TinyV1**.
2. Descompacte e coloque `latest.msgpack`, `tokenizer.model` e `config.json` juntos.
3. Para inspecionar o pacote, instale Python 3.10+ e execute:

```bash
git clone https://github.com/igoroliveiradevv/zenyxai.git
cd zenyxai
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python tools/inspect_checkpoint.py /caminho/para/pasta-extraida
```

Isso valida os metadados e o checkpoint; **não gera texto**. Veja [guia de instalação e treinamento](docs/INSTALL_AND_TRAIN.md).

## Como contribuir

Aceitamos issues, sugestões, revisão de código, testes e pull requests. Leia [CONTRIBUTING.md](CONTRIBUTING.md). Para integrar e continuar o treinamento real, precisamos restaurar o código exato que criou o checkpoint, assim como a configuração de otimizador/dados e a contagem efetiva de passos.

## Direitos e marca

**Código visível não significa licença open source.** O uso pessoal e a colaboração são permitidos apenas nos termos da [licença específica](LICENSE). Uso comercial e redistribuição sem autorização não são permitidos. O nome e a marca Zenyx AI são reservados aos titulares. Esta licença é uma proposta contratual personalizada, ainda sujeita a revisão jurídica.

## Segurança e limitações

Projeto experimental: as saídas futuras podem conter erros, vieses ou conteúdo inadequado. Não faça upload de senhas, dados pessoais ou documentos sem direito de compartilhamento. Não confie no checkpoint sem validação de integridade e proveniência.
