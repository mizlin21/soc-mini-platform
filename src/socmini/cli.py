from pathlib import Path

def main():
    data_dir = Path("data/raw")
    files = [f for f in data_dir.glob("*") if f.name != ".gitkeep"]
    print(f"[SOC-MINI] Loaded {len(files)} raw log files")

if __name__ == "__main__":
    main()
