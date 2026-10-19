#!/usr/bin/env python3
"""Read basic metadata from the TinyV1 backup; never executes model code."""
from pathlib import Path
import argparse
import json
import msgpack

def main():
    parser = argparse.ArgumentParser(description="Inspect a Zenyx TinyV1 checkpoint.")
    parser.add_argument("folder", type=Path, help="Directory with extracted TinyV1 files")
    args = parser.parse_args()
    files = ["config.json", "tokenizer.model", "latest.msgpack"]
    for name in files:
        p = args.folder / name
        if not p.is_file():
            parser.error(f"Arquivo ausente: {p}")
        print(f"{name}: {p.stat().st_size:,} bytes")
    config = json.loads((args.folder / "config.json").read_text(encoding="utf-8"))
    print("config:", json.dumps(config, ensure_ascii=False, indent=2))
    with (args.folder / "latest.msgpack").open("rb") as fh:
        state = msgpack.unpack(fh, raw=False, strict_map_key=False)
    if not isinstance(state, dict):
        parser.error("Checkpoint não contém um mapa no nível superior")
    print("Checkpoint top-level keys:", list(state))
    print("Atenção: inspeção apenas. O código de inferência/treino não acompanha o ZIP.")

if __name__ == "__main__":
    main()
