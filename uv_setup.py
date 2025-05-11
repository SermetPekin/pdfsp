import os
import subprocess
import tarfile
import zipfile
from pathlib import Path

def build_package():
    print("📦 Building package using uv...")
    subprocess.run(["uv", "build"], check=True)

def list_sdist_files(dist_dir):
    for archive in Path(dist_dir).glob("*.tar.gz"):
        print(f"\n📚 Contents of {archive.name}:")
        with tarfile.open(archive, "r:gz") as tar:
            for member in tar.getnames():
                print(f"   - {member}")

def list_wheel_files(dist_dir):
    for wheel in Path(dist_dir).glob("*.whl"):
        print(f"\n📚 Contents of {wheel.name}:")
        with zipfile.ZipFile(wheel, "r") as z:
            for member in z.namelist():
                print(f"   - {member}")

def main():
    dist_dir = "dist"
    if Path(dist_dir).exists():
        print("🧹 Cleaning previous build artifacts...")
        for file in Path(dist_dir).iterdir():
            file.unlink()

    build_package()

    if not Path(dist_dir).exists():
        print("❌ Build failed or dist directory not found.")
        return

    list_sdist_files(dist_dir)
    list_wheel_files(dist_dir)

if __name__ == "__main__":
    main()
