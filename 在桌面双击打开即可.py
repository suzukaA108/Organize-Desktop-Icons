import shutil # 引入以实现文件和文件夹的各类操作
from pathlib import Path # 引入实现操作系统的各类交互


def organize_desktop_icons():
    # 获取桌面路径
    desktop_path = Path.home() / "Desktop"

    # 定义文件类型分类
    categories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".md", ".rtf"],
        "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico"],
        "Audios": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".kgm", ".kgma", ".kgg", ".mgg", ".mflac", ".ncm"],
        "Videos": [".mp4", ".flv", ".f4v", ".webm", ".avi", ".mov", ".wmv", ".asf", ".mkv", ".avchd", ".mpg", ".mpeg", ".mpe", ".ts", ".flc", "vob", "ogv"]
    }

    # 创建分类文件夹
    for category in categories.keys():
        category_folder = desktop_path / category
        category_folder.mkdir(exist_ok=True)

    # 获取当前脚本文件名
    current_script = Path(__file__).name

    # 遍历桌面文件
    for item in desktop_path.iterdir():
        # 跳过文件夹
        if item.is_dir() and item.name in categories.keys():
            continue
        # 跳过此脚本文件
        if item.name == current_script:
            continue

        # 获取文件扩展名并小写
        file_extension_name = item.suffix.lower()

        # 分类移动文件
        moved = False
        for category, extension_name in categories.items():
            if file_extension_name in extension_name:
                target_folder = desktop_path / category # 构建目标路径
                try:
                    shutil.move(str(item), str(target_folder / item.name)) # 移动并保持原文件名
                    print(f"已移动: {item.name} -> {category}文件夹")
                    moved = True
                    break
                except Exception as e:
                    print(f"移动失败 {item.name}: {str(e)}")

        # 打印未分类文件信息
        if not moved and item.is_file():
            print(f"未分类: {item.name} (扩展名: {file_extension_name})")


if __name__ == "__main__":
    print("开始整理桌面图标...")
    organize_desktop_icons()
    print(r"整理完成 \(^o^)/")
    input("按Enter键退出...")