import os
import shutil
import sys

def main():
    print("="*60)
    print("        AUTOMATIC IMAGE FILTERING AND COPYING PROGRAM")
    print("="*60)

    # --- 1. INPUT DATA ---
    source_dir = input("1. Enter the path to the source image directory: ").strip().strip('"')
    target_dir = input("2. Enter the path to the destination directory: ").strip().strip('"')
    list_file_path = input("3. Enter the path to the text file containing the image list: ").strip().strip('"')
    print("-" * 60)

    # --- 2. INITIAL CONDITION CHECKS ---
    if not os.path.exists(source_dir):
        print(f"[ERROR] Source directory does not exist: {source_dir}")
        return

    if not os.path.exists(list_file_path):
        print(f"[ERROR] Text list file does not exist: {list_file_path}")
        return

    # --- 3. READ IMAGE NAME LIST ---
    try:
        with open(list_file_path, "r", encoding="utf-8") as f:
            photo_names = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[ERROR] Cannot read the list file: {e}")
        return

    if not photo_names:
        print("[WARNING] The list file is empty. No images to copy.")
        return

    # --- 4. CREATE DESTINATION DIRECTORY ---
    try:
        os.makedirs(target_dir, exist_ok=True)
    except Exception as e:
        print(f"[ERROR] Cannot create destination directory: {e}")
        return

    # --- 5. START FINDING AND COPYING (WITH ERROR TRAPPING) ---
    print(f"Starting to process {len(photo_names)} files...")
    copied_count = 0
    error_count = 0

    for name in photo_names:
        source_path = os.path.join(source_dir, name)

        if os.path.exists(source_path):
            try:
                # Proceed to copy (overwrite if file already exists in target)
                shutil.copy(source_path, target_dir)
                copied_count += 1
                print(f"[{copied_count}] Successfully copied: {name}")
            except PermissionError:
                print(f"[FAILED] Permission Denied: {name}")
                error_count += 1
            except Exception as e:
                print(f"[FAILED] Unknown error when copying file {name}: {e}")
                error_count += 1
        else:
            print(f"[SKIPPED] File not found: {name}")

    # --- 6. EXPORT RESULT REPORT ---
    print("-" * 60)
    print(f"--- COMPLETED! ---")
    print(f"• Total files in the list: {len(photo_names)} files.")
    print(f"• Successfully copied: {copied_count} files.")
    if error_count > 0:
        print(f"• System errors encountered: {error_count} files.")
    print("="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[NOTICE] Program aborted by user via keyboard shortcut.")
    except Exception as e:
        print(f"\n[CRITICAL SYSTEM ERROR]: {e}")
    finally:
        input("\nPress Enter to exit the program...")