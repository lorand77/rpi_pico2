import os
import gc
import sys

def check_memory():
    """Check RAM memory usage"""
    print("\n=== Memory (RAM) ===")
    gc.collect()
    free = gc.mem_free()
    allocated = gc.mem_alloc()
    total = free + allocated
    print(f"Free: {free:,} bytes ({free/1024:.2f} KB)")
    print(f"Allocated: {allocated:,} bytes ({allocated/1024:.2f} KB)")
    print(f"Total: {total:,} bytes ({total/1024:.2f} KB)")
    print(f"Usage: {(allocated/total)*100:.1f}%")

def check_flash():
    """Check flash storage"""
    print("\n=== Flash Storage ===")
    try:
        stat = os.statvfs('/')
        block_size = stat[0]
        total_blocks = stat[2]
        free_blocks = stat[3]
        
        total = (total_blocks * block_size)
        free = (free_blocks * block_size)
        used = total - free
        
        print(f"Total: {total:,} bytes ({total/1024/1024:.2f} MB)")
        print(f"Used: {used:,} bytes ({used/1024/1024:.2f} MB)")
        print(f"Free: {free:,} bytes ({free/1024/1024:.2f} MB)")
        print(f"Usage: {(used/total)*100:.1f}%")
    except Exception as e:
        print(f"Error: {e}")

def list_files(path='/', indent=0):
    """Recursively list all files and directories"""
    try:
        for item in os.listdir(path):
            item_path = path + '/' + item if path != '/' else '/' + item
            print('  ' * indent + item, end='')
            try:
                stat = os.stat(item_path)
                if stat[0] & 0x4000:  # Directory
                    print('/')
                    list_files(item_path, indent + 1)
                else:  # File
                    print(f" ({stat[6]:,} bytes)")
            except:
                print()
    except Exception as e:
        print(f"Error listing {path}: {e}")

def check_system():
    """Check system information"""
    print("\n=== System Info ===")
    print(f"Platform: {sys.platform}")
    print(f"Python: {sys.version}")
    print(f"Implementation: {sys.implementation}")

def main():
    print("=" * 40)
    print("RP Pico2 System Check")
    print("=" * 40)
    
    check_system()
    check_memory()
    check_flash()
    
    print("\n=== File System ===")
    list_files('/')
    
    print("\n" + "=" * 40)

if __name__ == "__main__":
    main()