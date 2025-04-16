# Third Party Imports
import ezdxf

# Standard Library Imports
from pathlib import Path
import re

def clean_dxf(input_path, output_path):
    # Load the DXF file
    doc = ezdxf.readfile(input_path)
    
    # Clean header variables
    header = doc.header
    
    # Remove sensitive variables
    if '$LASTSAVEDBY' in header:
        header['$LASTSAVEDBY'] = ''
    if '$FINGERPRINTGUID' in header:
        header['$FINGERPRINTGUID'] = '{00000000-0000-0000-0000-000000000000}'
    if '$VERSIONGUID' in header:
        header['$VERSIONGUID'] = '{00000000-0000-0000-0000-000000000000}'
    if '$LATITUDE' in header:
        header['$LATITUDE'] = 0.0
    if '$LONGITUDE' in header:
        header['$LONGITUDE'] = 0.0
    if '$TIMEZONE' in header:
        header['$TIMEZONE'] = 0.0
    # Save the cleaned file
    doc.saveas(output_path)


# Usage
pattern = r".+\.dxf"
pattern_skip = r".+_cleaned\.dxf"

for file in Path(__file__).parent.iterdir():
    if re.match(pattern, file.name):
        if not re.match(pattern_skip, file.name):
            output_path = file.parent / f"{file.stem}_cleaned.dxf"
            clean_dxf(file, output_path)