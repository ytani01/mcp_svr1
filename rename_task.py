import datetime
import os


def rename_and_move_tasks_md():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y%m%d-%H%M")
    new_filename = f"{timestamp}-Tasks-done.md"

    old_path = "Tasks.md"
    new_path = os.path.join("archives", new_filename)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed Tasks.md to {new_filename} and moved to archives/")
    else:
        print("Tasks.md not found.")

if __name__ == "__main__":
    rename_and_move_tasks_md()
