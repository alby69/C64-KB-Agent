from pathlib import Path

from cleaners.c64ref_dataset_builder import C64RefDatasetBuilder
from cleaners.c64ref_markdown_writer import C64RefMarkdownWriter
from cleaners.c64ref_merger import C64RefMerger
from cleaners.c64ref_parser import (
    C64DisasmParser,
    C64IOParser,
    C64MemParser,
    CPU6502Parser,
    KernalParser,
)


def main():
    print("=== Starting c64ref Cleaner Pipeline ===")

    # Paths
    base_dir = Path(__file__).resolve().parent.parent
    src_dir = base_dir / "data" / "sources" / "c64ref" / "src"
    output_dir = base_dir / "data" / "docs" / "c64ref"
    data_dir = base_dir / "data"

    if not src_dir.exists():
        print(f"Error: c64ref source directory does not exist at {src_dir}. Did you initialize the submodule?")
        return

    all_raw_entities = []

    # 1. Parse c64mem files
    print("Parsing memory map files...")
    mem_parser = C64MemParser()
    mem_path = src_dir / "c64mem"
    for txt_file in mem_path.glob("c64mem_*.txt"):
        print(f"  Parsing {txt_file.name}")
        all_raw_entities.extend(mem_parser.parse_file(txt_file))

    # 2. Parse c64io files
    print("Parsing I/O map files...")
    io_parser = C64IOParser()
    io_path = src_dir / "c64io"
    for txt_file in io_path.glob("c64io_*.txt"):
        print(f"  Parsing {txt_file.name}")
        all_raw_entities.extend(io_parser.parse_file(txt_file))

    # 3. Parse kernal files
    print("Parsing KERNAL API files...")
    kernal_parser = KernalParser()
    kernal_path = src_dir / "kernal"
    for txt_file in kernal_path.glob("kernal_*.txt"):
        print(f"  Parsing {txt_file.name}")
        all_raw_entities.extend(kernal_parser.parse_file(txt_file))

    # 4. Parse c64disasm files
    print("Parsing ROM disassembly files...")
    disasm_parser = C64DisasmParser()
    disasm_path = src_dir / "c64disasm"
    for txt_file in disasm_path.glob("c64disasm_*.txt"):
        print(f"  Parsing {txt_file.name}")
        all_raw_entities.extend(disasm_parser.parse_file(txt_file))

    # 5. Parse 6502 CPU instruction files
    print("Parsing CPU 6502 files...")
    cpu_parser = CPU6502Parser()
    cpu_path = src_dir / "6502" / "cpu_6502.txt"
    if cpu_path.exists():
        print(f"  Parsing {cpu_path.name}")
        all_raw_entities.extend(cpu_parser.parse_file(cpu_path))

    print(f"Total parsed raw entities: {len(all_raw_entities)}")

    # 6. Unify and merge multi-source comments
    print("Merging multi-source comments...")
    merger = C64RefMerger()
    merger.build_global_slug_map(all_raw_entities)
    merged_entities = merger.merge_entities(all_raw_entities)
    print(f"Total merged unique entities: {len(merged_entities)}")

    # 7. Write Markdown files with YAML frontmatter
    print("Writing Markdown documentation files...")
    # Clean previous output directory to avoid stale files
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    writer = C64RefMarkdownWriter(base_dir / "data" / "docs" / "c64ref")
    for idx, entity in enumerate(merged_entities):
        if idx % 100 == 0:
            print(f"  Writing entities: {idx}/{len(merged_entities)}")
        writer.write_entity(entity)

    # 8. Update database and datasets
    print("Updating datasets and indices...")
    builder = C64RefDatasetBuilder(data_dir)
    builder.build(merged_entities)

    print("=== c64ref Cleaner Pipeline Completed Successfully ===")

if __name__ == "__main__":
    main()
