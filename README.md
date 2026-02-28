# Python Backend Development: Project modularization and Robustness

This repository documents the structural evolution of a Python-based inventory and data management system, progressing from script-based logic to modular, error-resistant backend architecture.

## Technical Environment Setup
To initialize the development environment and ensure script execution permissions on Windows systems:

### 1. Execution Policy Configuration
Run the following in PowerShell with appropriate user scope:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

### Virtual Environment Management
Initialize Environment: python -m venv .venv

- Activation: .\.venv\Scripts\Activate.ps1
- Dependency Installation: pip install requests

## Learnig Milestones:

### Phase 1: Modular System Architecture
- Structural Reorganization: Transitioned `from` single-file execution to a modular directory structure.
- Utility Decoupling: Separated core logic `from` helper functions (e.g., data_utils.py) to facilitate code reuse.
- CSV Engine: Developed a universal boilerplate `for` exporting Python dictionaries to CSV format using dynamic header detection.

### Phase 2: Robustness and External Integration
- Advanced Exception Handling: Implemented `try-except-else-finally` blocks to manage runtime risks, specifically targeting ValueError, FileNotFoundError, and PermissionError.
- API Integration: Leveraged the requests library to interface with REST APIs (GitHub, ExchangeRate-API).
- `Data` Serialization`: Integrated json module `for` persisting live API responses to local storage.
- Dictionary Security: Utilized the .get() method to ensure fail-safe access to nested JSON data, preventing KeyError terminations.