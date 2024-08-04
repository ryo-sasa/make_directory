import csv
import os
from tqdm import tqdm

def create_folders_from_csv(csv_file, base_folder, skip_header=True):
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        if skip_header:
            next(reader)  # ヘッダー行をスキップ
        for row in tqdm(reader, desc="Creating folders from CSV"):
            create_nested_folders(base_folder, row)

def create_nested_folders(base_folder, folders):
    current_path = base_folder
    for folder in folders:
        if folder:  # 空の値をスキップ
            current_path = os.path.join(current_path, folder)
            create_folder(current_path)

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

if __name__ == "__main__":
    # 同じフォルダにあるCSVファイルの名前を指定
    csv_file_name = "book1.csv"

    # プログラムが存在するフォルダのパスを取得
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # create_folderという名前のフォルダを作成
    create_folder(os.path.join(current_folder, "create_folder"))

    # CSVファイルを読み取り、create_folder内に生成されたフォルダを格納
    create_folders_from_csv(
        os.path.join(current_folder, csv_file_name),
        os.path.join(current_folder, "create_folder"),
    )