# Wheels folder for offline installation

This folder contains all Python package wheels (.whl files) required for offline installation in restricted environments without internet access.

## Contents

65 wheel files totaling ~78 MB

## Usage

```powershell
pip install --no-index --find-links=wheels -r requirements.txt
```

See INSTALACAO_OFFLINE.md for complete instructions.
