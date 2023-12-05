import os
from shutil import copy2
from tqdm import tqdm

def tripleCheck(path1,path2,path3,save_path):
    
    folder_paths = [path1,path2,path3] 
    file_sets = [set(os.listdir(f)) for f in folder_paths]

    # 3명의 검수 폴더에서 중복되는 파일
    common_files = set.intersection(*file_sets)

    os.makedirs(save_path,exist_ok=True)

    for file in tqdm(common_files):
        src_file = os.path.join(folder_paths[0], file)
        copy2(src_file, save_path)

