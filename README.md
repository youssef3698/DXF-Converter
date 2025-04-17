# DXF Converter 🏗️➡️📊

_A Python tool that converts DXF files to structured data (CSV/TXT) with configurable layer mapping._

## Table of Contents
- [DXF Converter 🏗️➡️📊](#dxf-converter-️️)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [‼️ The Problem](#️-the-problem)
  - [🛠️ How This Script Solves It](#️-how-this-script-solves-it)
  - [Quick Start Guide](#quick-start-guide)
  - [Future Ideas *(Optional Enhancements)*](#future-ideas-optional-enhancements)
  - [Contributions](#contributions)
  - [License](#license)

## Features
- ✨ Extract point data from DXF files with custom layer mapping
- ⚡ 99% faster than manual processing (2 hours -> 30 seconds in production)
- 🛠️ Configurable via `config.ini` (no code changes needed)

## ‼️ The Problem
We had a malfunctioning total station on site which was able to get all the info but only extract them to DXF.
- **Can't replace total station**: Costs around 12,000 USD to replace equipment
- **Manual data extraction**: Hours spent copying point coordinates/text from AutoCAD
- **Error-prone workflow**: Misaligned layers or missed annotations in spreadsheet
- **No standardization**: Every total station uses different layer naming conventions

## 🛠️ How This Script Solves It 
- **Automated extraction**: Pulls all point data with one click
- **Configurable mapping**: Adapts to any layer naming scheme via `config.ini`
- **QC built-in**: Flags mismatched points/descriptions
- **Multi-format output**: Ready for CSV and TXT export

## Quick Start Guide
1. **Clone Git**:
   ```git
   git clone https://github.com/youssef3698/DXF-Converter.git
   ```

2. **Create Virtual Environment (Optional)**:
   Windows
   ```bash
   python -m venv venv
   ```
   ```bash
   venv\\scripts\\activate
   ```
   
   Mac/Linux
   ```bash
   python3 -m venv venv
   ```
   ```bash
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   Windows
   ```bash
   pip install -r requirements.txt
   ```
   Mac/Linux
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Usage**:
    1. **Using Script**:
         1. Edit `config.ini`:
            ```ini
            [LAYERS]
            point_id = ID Ponto        # Layer containing point IDs
            description = Description  # Layer containing descriptions

            [OUTPUT]
            default_extension = csv    # Default extension type
            ```
        1. Run script:
            ```bash
            python src/main.py
            ```
    2. **Building exe**:
        1. Build exe:
            ```bash
            python deploy/build.py
            ```
        2. Copy `config.ini` to `dist/`:
        3. Edit `config.ini`:
          ```ini
          [LAYERS]
          point_id = ID Ponto        # Layer containing point IDs
          description = Description  # Layer containing descriptions

          [OUTPUT]
          default_extension = csv    # Default extension type
          ```
        4. Run `dist/DXF_Converter.exe`

## Future Ideas *(Optional Enhancements)*
- [ ] Add proper logging system
- [ ] Add batch processing for multiple DXF files
- [ ] Improve tests

## Contributions
This project is considered *feature-complete* for its core purpose. If you'd like to fork or extend it:
1. Open an Issue to discuss major changes
2. Follow the existing code style

## License
This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

*Note: While I may not actively maintain this, I'll review meaningful PRs when possible.*