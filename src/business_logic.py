# Third Party Imports
import ezdxf
import pandas as pd

# Standard Library Imports
import configparser
from typing import List
from pathlib import Path
import sys


class ConverterOperations:
    def __init__(self, file_path, save_file_path, convert_option) -> None:
        self.file_path = file_path
        self.save_file_path = save_file_path
        self.convert_option = convert_option
        self.skipped_entities = []
        
        # Initialize configuration
        if getattr(sys, "frozen", False):
            # Running as bundled exe
            self.config_path = Path(sys.executable).parent / "config.ini"
        else:
            # Running as script
            self.config_path = Path(__file__).parents[1] / "config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path, encoding="utf-8")

        # Load the configuration
        self.point_id_layer = self.config["LAYERS"]["point_id"]
        self.description_layer = self.config["LAYERS"]["description"]

    def convert_file(self) -> List:
        # Load the DXF file
        doc = ezdxf.readfile(self.file_path)
        data = []

        # Fetch all POINT entities
        for entity in doc.modelspace().query("POINT"):
            point_loc = entity.dxf.location
            # Find all entities at this location
            all_entities = [
                e
                for e in doc.modelspace()
                if hasattr(e, "dxf")
                and hasattr(e.dxf, "insert")
                and e.dxf.insert.z == point_loc.z
            ]

            # Filter for TEXT entities
            texts = [e for e in all_entities if e.dxftype() == "TEXT"]

            # Initialize variables
            point_id = None
            description = None

            # Get all text entities near this point and process them based on their layers
            for text in texts:
                content = text.dxf.text
                layer = text.dxf.layer
                # print("-"*40)
                # print(f"TEXT entity: {content}, on layer: {layer}")

                # print("*"*20)
                # print(f"DXF layer repr: {repr(layer)}")
                # print(f"Config layer repr: {repr(self.description_layer)}")
                # print("*"*20)
                
                if layer == self.description_layer:
                    # print(f"Description entity found: {content}")
                    description = content
                elif layer == self.point_id_layer:
                    # print(f"Point ID entity found: {content}")
                    try:
                        point_id = int(content)
                    except ValueError:
                        self.skipped_entities.append((content, point_loc))
                        point_id = None
                        description = content
                        # TODO: Migrate to use logging
                        print("Skipped entity:", content)
                else:
                    # print(f"Skipped text: {content}")
                    pass
                # print(f"Point ID: {point_id}, Description: {description}")

            # Append the data
            data.append(
                [
                    point_id,
                    point_loc.x,
                    point_loc.y,
                    point_loc.z,
                    description,
                ]
            )

        # Create a DataFrame
        df = pd.DataFrame(data, columns=["ID", "X", "Y", "Z", "Description"])
        df = df.sort_values(by="ID")

        # Save the DataFrame to the specified format
        if self.convert_option == "txt":
            df.to_string(self.save_file_path, index=False)
        elif self.convert_option == "csv":
            df.to_csv(self.save_file_path, index=False)
        else:
            raise ValueError("Unsupported file format. Use 'txt' or 'csv'")

        return self.skipped_entities
