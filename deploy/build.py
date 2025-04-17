import PyInstaller.__main__
from pathlib import Path
import os

# Get config file path
config_path = Path(__file__).parent / "config.ini"
if not config_path.exists():
    raise FileNotFoundError(f"Config file not found at {config_path}")

# Get license file path
license_path = Path(__file__).parents[1] / "LICENSE.md"
if not license_path.exists():
    raise FileNotFoundError(f"License file not found at {license_path}")

# Get system pathsep
sep = os.pathsep

PyInstaller.__main__.run(
    [
        "src/main.py",
        "--name=DXF_Converter",
        "--onefile",
        "--noconsole",
        f"--add-data={config_path}{sep}.",
        f"--add-data={license_path}{sep}.",
        "--icon=deploy/app.ico",
        "--clean",
        "--windowed",
    ]
)
