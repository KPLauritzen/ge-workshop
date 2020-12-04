
def task_create_dataset():
    return {
        "file_dep": ["create_dataset.py"],
        "targets": ["data/raw_data.csv"],
        "actions": ["python create_dataset.py"],
    }

def task_preprocess_data():
    return {
        "file_dep": ["data/raw_data.csv", "preprocess_data.py"],
        "targets": ["data/processed_data.csv"],
        "actions": ["python preprocess_data.py"]
    }