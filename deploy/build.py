import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run(
    [
        "src/main.py",
        "--name=DXF_Converter",
        "--onefile",
        "--noconsole",
        # "--add-data=LICENSE.txt;.",  # If you have a license file
        "--icon=deploy/app.ico",  # If you have an icon
        "--clean",
        "--windowed",
    ]
)
