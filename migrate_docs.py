import os
import shutil

# 配置部分
SOURCE_EXTENSIONS = ['.mdx', '.md']
LANGUAGES = ['en', 'cn']
IGNORE_DIRS = {'.git', 'node_modules', 'en', 'cn', '.mintlify', '.vscode'}

def migrate_files():
    root_dir = os.getcwd()
    print(f"开始在 {root_dir} 进行文件迁移...")

    for current_root, dirs, files in os.walk(root_dir):
        # 排除忽略的目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if not any(file.endswith(ext) for ext in SOURCE_EXTENSIONS):
                continue

            source_path = os.path.join(current_root, file)
            rel_path = os.path.relpath(source_path, root_dir)

            print(f"正在处理: {rel_path}")

            for lang in LANGUAGES:
                new_rel_path = os.path.join(lang, rel_path)
                dest_path = os.path.join(root_dir, new_rel_path)
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                if not os.path.exists(dest_path):
                    shutil.copy2(source_path, dest_path)
                    print(f"  -> 已创建: {new_rel_path}")
                else:
                    print(f"  -> 跳过 (已存在): {new_rel_path}")

    print("\n------------------------------------------------")
    print("✅ 迁移完成！")
    print("请检查 'en' 和 'cn' 文件夹。")
    print("------------------------------------------------")

if __name__ == "__main__":
    migrate_files()
