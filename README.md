# Markdown Parser Django app

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Run the migration
```
py manage.py migrate
```

### 3. Run the custom command to import data from Markdown files
Markdown files are located in `articles` directory.
```
py manage.py import_data
```