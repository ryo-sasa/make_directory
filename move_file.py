import csv
import os
import shutil
from tqdm import tqdm

def move_files_from_csv(csv_file, base_folder, input_folder, skip_header=True):
    try:
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            if skip_header:
                next(reader)  # ヘッダー行をスキップ
            for row in tqdm(reader, desc="Moving files from CSV"):
                if len(row) >= 5:  # 5列以上のデータがある場合に処理
                    target_folder = create_nested_folders(base_folder, row[:4])  # 1-4列目でパスを取得
                    file_name_with_ext = row[4]  # 5列目のファイル名（拡張子を含む）
                    move_file_from_source(input_folder, target_folder, file_name_with_ext)
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def create_nested_folders(base_folder, folders):
    current_path = base_folder
    for folder in folders:
        if folder:  # 空の値をスキップ
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):  # フォルダが存在しない場合は作成
                os.makedirs(current_path)
    return current_path  # 最下層のフォルダパスを返す

def move_file_from_source(source_folder, target_folder, file_name):
    try:
        source_path = os.path.join(source_folder, file_name)
        target_path = os.path.join(target_folder, file_name)
        # デバッグ用にパスを出力
        print(f"Source path: {source_path}")  
        print(f"Target path: {target_path}")  
        # ファイルが存在するかチェック
        if os.path.isfile(source_path):
            print(f"Moving file: {file_name} from {source_path} to {target_path}")  # デバッグ用
            try:
                shutil.move(source_path, target_path)
            except Exception as e:
                print(f"Error moving file {file_name}: {e}")
        else:
            print(f"File does not exist: {source_path}")
    except Exception as e:
        print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    # CSVファイルの名前を指定
    csv_file_name = "input.csv"

    # プログラムが存在するフォルダのパスを取得
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # ベースフォルダを指定
    base_folder = os.path.join(current_folder, "create_folder")

    # inputフォルダを指定
    input_folder = os.path.join(current_folder, "input")

    # CSVファイルを読み取り、最下層のフォルダにファイルを移動
    try:
        move_files_from_csv(os.path.join(current_folder, csv_file_name), base_folder, input_folder)
    except Exception as e:
        print(f"Error processing CSV file: {e}")