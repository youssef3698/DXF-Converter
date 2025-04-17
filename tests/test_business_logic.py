# Standard Library Imports
from pathlib import Path

# Local Application Imports
from src.business_logic import ConverterOperations


def test_convert_file():
    # Test data setup
    file_path = Path(__file__).parent / "input" / "test_case_1_cleaned.dxf"
    save_file_path = Path(__file__).parent / "output" / "test_case_1.csv"
    convert_option = "csv"

    converter = ConverterOperations(file_path, save_file_path, convert_option)
    
    result = converter.convert_file()
    
    # Check if the result is an empty list
    assert isinstance(result, list)
    assert len(result) == 0
    
    # Check if the output file is created and is a CSV file
    assert save_file_path.exists()
    assert save_file_path.suffix == ".csv"
    
    # Check output file content
    with open(save_file_path, "r") as f:
        content = f.read()
        assert "ID,X,Y,Z,Description" in content
        assert "1,1.0,2.0,3.0,Test Point 1" in content
        assert "2,15.0,16.0,17.0,Test Point 2" in content
