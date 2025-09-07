import os

BASE_DIR = "generated_project"
os.makedirs(BASE_DIR, exist_ok=True)

def safe_path(path: str) -> str:
    """Ensure all paths are rooted inside BASE_DIR."""
    return os.path.join(BASE_DIR, path)

def read_file(path: str) -> str:
    """Read and return the contents of a file from the given path inside generated_project."""
    full_path = safe_path(path)
    if not os.path.exists(full_path):
        return f"Error: File not found: {full_path}"
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    """Create or overwrite a file at the given path inside generated_project."""
    full_path = safe_path(path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File written successfully: {full_path}"

def list_files(directory: str = ".") -> str:
    """List all files and directories at a given path inside generated_project."""
    full_dir = safe_path(directory)
    if not os.path.exists(full_dir):
        return f"Error: Directory not found: {full_dir}"
    files = ", ".join(os.listdir(full_dir))
    if not files:
        return f"No files found in directory: {full_dir}"
    return files

def create_folder(path: str) -> str:
    """Create a folder (and any necessary parent folders) inside generated_project."""
    full_path = safe_path(path)
    try:
        os.makedirs(full_path, exist_ok=True)
        return f"Folder created successfully: {full_path}"
    except Exception as e:
        return f"Error while creating folder {full_path}: {str(e)}"