import sys
from pathlib import Path


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    if not root.exists():
        print(f"Path does not exist: {root}")
        sys.exit(1)

    total_lines = 0
    total_files = 0

    print("Scanning Skripts...\n")

    for sk_file in sorted(root.rglob("*.sk")):
        try:
            with open(sk_file, "r", encoding="utf-8", errors="replace") as f:
                lines = sum(1 for _ in f)
        except OSError as e:
            print(f"  [ERROR] Could not read {sk_file}: {e}")
            continue

        total_lines += lines
        total_files += 1
        # Show path relative to root for readability
        rel_path = sk_file.relative_to(root)
        print(f"{rel_path}: {lines} lines")

    print(f"\nScan complete! Found {total_files} files, Total: {total_lines} lines")


if __name__ == "__main__":
    main()
