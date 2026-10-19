# Instalar e contribuir com o treinamento — Zenyx TinyV1

## 1. Pré-requisitos

- Python 3.10 ou superior.
- Git.
- Espaço livre suficiente para extrair os arquivos (checkpoint ~57,5 MB, além de dependências).
- Para **inspecionar** os artefatos, não é necessário GPU.
- Para **treinar de verdade**, será necessário o código Python original da arquitetura e do passo de treinamento, atualmente ausente do pacote enviado.

## 2. Obter os arquivos

Abra [a página de releases](https://github.com/igoroliveiradevv/zenyxai/releases). Quando estiver publicado, baixe `LLM_BR_Tiny_v1_backup.zip`. Não confunda o download automático de `Source code (zip)` com os pesos treinados.

Extraia para uma pasta, por exemplo `model/tiny-v1/`. O resultado esperado é:

```text
model/tiny-v1/
  config.json
  latest.msgpack
  tokenizer.model
```

## 3. Preparar ambiente

```bash
git clone https://github.com/igoroliveiradevv/zenyxai.git
cd zenyxai
python -m venv .venv
```

Ative o ambiente:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows CMD: `.venv\Scripts\activate.bat`
- Linux/macOS: `source .venv/bin/activate`

Depois:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python tools/inspect_checkpoint.py model/tiny-v1
```

O inspetor lê o JSON, valida os três arquivos e imprime a estrutura de nível superior do checkpoint usando MsgPack. Ele não executa código serializado, não modifica pesos e não prova compatibilidade para retomar treinamento.

## 4. Executar o modelo

**Ainda não disponível nesta versão documental.** É necessário publicar e testar a classe do modelo, as bibliotecas/versões exatas (ex.: JAX/Flax, se aplicável), o carregador do estado e um laço de geração. Não há base para afirmar que comandos genéricos do Hugging Face funcionam com este checkpoint.

## 5. Ajudar no treinamento

1. Crie uma issue apresentando proposta e dados (origem, licença, idioma, qualidade).
2. Evite corpus com informações pessoais, chaves, senhas, dados protegidos ou conteúdo sem permissão.
3. Crie branch e pull request com descrição, testes, instruções e evidência reproduzível.
4. Antes de enviar **novos pesos**, combine com mantenedores o formato, métricas, versão e local de armazenamento. Não inclua checkpoints grandes nos commits.
5. Para retomar o treinamento de modo reproduzível, precisamos registrar commit do código original, dependências, seed, contagem real de passos, estado do otimizador, dados disponíveis e hashes dos artefatos.

## 6. Sugestões de contribuições imediatamente úteis

- Recuperar e publicar a implementação original do notebook Kaggle/Colab.
- Adicionar teste de reconstrução do checkpoint.
- Adicionar testes de tokenização/geração, assim que houver inferência.
- Criar pipeline de avaliação em português.
- Documentar direitos de uso de dados e procedência dos pesos.

## 7. Reportar problemas

Abra uma [issue](https://github.com/igoroliveiradevv/zenyxai/issues) com SO, Python, comando reproduzível, saída de erro **sem segredos**, e o que você esperava.

Para restrições de direitos e uso, veja [LICENSE](../LICENSE).
