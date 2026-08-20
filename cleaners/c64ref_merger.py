from cleaners.c64ref_parser import Entity


def get_slug(entity: Entity) -> str:
    """Generates the unique slug/filename for an entity based on the naming convention."""
    module = entity.module
    addr = entity.address
    sym = entity.symbol

    # Strip leading $ from address if present
    addr_clean = addr.replace("$", "").lower() if addr else ""
    sym_clean = sym.lower() if sym else ""

    if module == "c64mem":
        if sym_clean:
            return f"{addr_clean}-{sym_clean}"
        return addr_clean
    elif module == "c64io":
        # VIC-II, SID, CIA subdirectories can be handled by the writer,
        # but the slug can just be address-symbol or address.
        if sym_clean:
            return f"{addr_clean}-{sym_clean}"
        return addr_clean
    elif module == "kernal":
        if sym_clean:
            return sym_clean
        return addr_clean
    elif module == "6502":
        return sym_clean
    elif module == "c64disasm":
        if sym_clean:
            return f"{addr_clean}-{sym_clean}"
        return addr_clean
    return addr_clean or sym_clean


class C64RefMerger:
    """Merges entities from different source files of the same module and resolves cross-references."""

    def __init__(self):
        self.global_slugs: dict[str, str] = {}  # key (symbol or address) -> slug

    def build_global_slug_map(self, all_entities: list[Entity]) -> None:
        """First pass to map every unique symbol/address to its slug."""
        for entity in all_entities:
            slug = get_slug(entity)
            if entity.symbol:
                self.global_slugs[entity.symbol.upper()] = slug
            if entity.address:
                self.global_slugs[entity.address.upper()] = slug

    def merge_entities(self, entities: list[Entity]) -> list[Entity]:
        """Group entities by module and address/symbol, unifies descriptions and ranks sources."""
        merged: dict[tuple[str, str], Entity] = {}

        for entity in entities:
            # Generate a key based on address if present, else symbol (e.g. for 6502)
            key_id = entity.address.upper() if entity.address else entity.symbol.upper()
            key = (entity.module, key_id)

            if key not in merged:
                # First time seeing this entity, make a copy
                merged[key] = Entity(
                    module=entity.module,
                    address=entity.address,
                    address_end=entity.address_end,
                    symbol=entity.symbol,
                    heading=entity.heading,
                    description=entity.description,
                    sources=list(entity.sources),
                    related=list(entity.related),
                    disasm_lines=entity.disasm_lines,
                    category=entity.category,
                    flags=entity.flags,
                    formula=entity.formula,
                    opcodes_list=entity.opcodes_list,
                )
            else:
                existing = merged[key]
                # Combine source comments
                existing.sources.extend(entity.sources)

                # Combine disassembly lines if from c64disasm
                if entity.disasm_lines and not existing.disasm_lines:
                    existing.disasm_lines = entity.disasm_lines

                # Update high-level fields if currently missing
                if not existing.category and entity.category:
                    existing.category = entity.category
                if not existing.flags and entity.flags:
                    existing.flags = entity.flags
                if not existing.formula and entity.formula:
                    existing.formula = entity.formula
                if not existing.opcodes_list and entity.opcodes_list:
                    existing.opcodes_list = entity.opcodes_list

        # Second pass: sort sources by priority descending, unify description/heading
        for _key, entity in merged.items():
            # Sort sources by priority descending
            entity.sources.sort(key=lambda s: s.priority, reverse=True)

            # Select the highest priority source's text or heading as primary
            if entity.sources:
                primary_source = entity.sources[0]
                entity.description = primary_source.text

            # Resolve related cross-references using the global slug map
            related_slugs = set()
            for rel in entity.related:
                if rel in self.global_slugs:
                    related_slugs.add(self.global_slugs[rel])

            # If there is same module references (like address within range or symbol),
            # let's include them.
            entity.related = sorted(related_slugs)

        return list(merged.values())
