# Zenyx TinyV1 — Notas da versão

**Tag sugerida:** `tiny-v1`  
**Nome da release:** `Zenyx TinyV1`  
**Tipo:** pré-lançamento experimental (pre-release)

Primeiro checkpoint experimental do projeto Zenyx AI.

## Conteúdo do pacote
- `latest.msgpack`: estado serializado de treinamento;
- `tokenizer.model`: tokenizador SentencePiece;
- `config.json`: configuração registrada no backup.

## Configuração
- 4 camadas Transformer, 4 heads, dimensão 256;
- Comprimento de sequência: 256 tokens;
- Vocabulário: 6.430 tokens;
- `total_steps=50000` é valor de configuração, **não número de passos concluídos verificado**.

## Download
Anexe **LLM_BR_Tiny_v1_backup.zip** como recurso binário desta release.

SHA-256: `502f7c76d910b3d773072d2ca58612cdaace4aef20fbccf31be5fca3f1c5f286`

## Limitações
Esse pacote **não contém** a implementação de inferência, a arquitetura em código-fonte ou o script original de treinamento. Por enquanto é possível baixar, validar e inspecionar o checkpoint; executar respostas e continuar treinamento dependem da restauração da implementação original.

Guia: [Instalação e treinamento](../main/docs/INSTALL_AND_TRAIN.md) (na página de Release, use o guia no repositório). Direitos: [LICENSE](../main/LICENSE). Projeto disponibilizado com restrições de uso não comercial e redistribuição.

## Instruções para o mantenedor criar a Release
1. Abra **Releases → Draft a new release**.
2. Create new tag: `tiny-v1`, target `main`.
3. Release title: `Zenyx TinyV1`.
4. Cole estas notas (sem este bloco de instruções), marque **Set as a pre-release**.
5. Arraste `LLM_BR_Tiny_v1_backup.zip` para o campo de arquivos binários.
6. Publique e confira que o ZIP aparece em **Assets**.
