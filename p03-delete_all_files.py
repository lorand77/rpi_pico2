import os

def delete_all_files(path='/', exclude_list=None):
    """
    Recursively delete all files and directories
    
    Args:
        path: Starting path (default '/')
        exclude_list: List of files/dirs to preserve (default None)
    """
    if exclude_list is None:
        exclude_list = []
    
    print(f"\nScanning: {path}")
    
    try:
        items = os.listdir(path)
        
        for item in items:
            # Skip excluded items
            if item in exclude_list:
                print(f"Skipping: {item}")
                continue
            
            item_path = path + '/' + item if path != '/' else '/' + item
            
            try:
                stat = os.stat(item_path)
                
                if stat[0] & 0x4000:  # Directory
                    print(f"Entering directory: {item_path}")
                    delete_all_files(item_path, exclude_list)
                    try:
                        os.rmdir(item_path)
                        print(f"Deleted directory: {item_path}")
                    except Exception as e:
                        print(f"Error deleting directory {item_path}: {e}")
                else:  # File
                    try:
                        os.remove(item_path)
                        print(f"Deleted file: {item_path}")
                    except Exception as e:
                        print(f"Error deleting file {item_path}: {e}")
                        
            except Exception as e:
                print(f"Error accessing {item_path}: {e}")
                
    except Exception as e:
        print(f"Error listing {path}: {e}")

def confirm_deletion():
    """Ask for user confirmation before deletion"""
    print("=" * 50)
    print("WARNING: This will DELETE ALL FILES!")
    print("=" * 50)
    print("\nThis action cannot be undone!")
    print("\nType 'DELETE ALL' to confirm: ", end='')
    
    try:
        confirmation = input().strip()
        return confirmation == 'DELETE ALL'
    except:
        # If input() is not available (no REPL), return False
        print("\nInput not available. Aborting.")
        return False

def main():
    """Main function with safety checks"""
    
    # Files/directories to preserve (optional)
    # Uncomment and modify as needed:
    # exclude_list = ['boot.py', 'main.py']
    exclude_list = []
    
    if confirm_deletion():
        print("\nStarting deletion process...")
        delete_all_files('/', exclude_list)
        print("\n" + "=" * 50)
        print("Deletion complete!")
        print("=" * 50)
    else:
        print("\nDeletion cancelled.")

if __name__ == "__main__":
    main()
