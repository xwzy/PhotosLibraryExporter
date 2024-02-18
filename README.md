# PhotosLibraryExporter

## Introduction
PhotoExport is a tool specifically designed for macOS users, allowing you to export photos from your Photos app library to any specified directory. Whether it's for backup, organization, or migration of your photo collection, PhotoExport offers a fast and intuitive way to accomplish this task.

## Features
- Automatically identifies photo files from both "originals" and "Masters" paths.
- Automatically resolves filename conflicts in the destination path.
- Uses the `tqdm` library to display copy progress in real time, making the process more transparent.
- Simple command-line interface, easy to use.

## Installation Requirements
This tool requires a Python 3.x environment and depends on the following Python libraries:
- `os`
- `shutil`
- `pathlib`
- `tqdm`

Please ensure these dependencies are installed on your system.

## Usage

1. Clone or download this project locally.
2. Open the terminal and switch to the project directory.
3. Run the script with the following command, replacing `<PhotosLibraryPath>` and `<DestinationPath>` with your Photos library path and the desired destination path for the photos:

```bash
python photo_export.py "<PhotosLibraryPath>" "<DestinationPath>"
```

4. The script will start executing and display the copy progress.

## Notes
- Please ensure you have access permissions to the specified Photos library path and destination path.
- Due to macOS's permission management, you might need to grant terminal or Python sufficient permissions to access the Photos library.
- This tool does not modify any files or structures in the original Photos library; it only performs copy operations.

## Contributions
Contributions of any form are welcome, including but not limited to proposals for new features, code improvements, and documentation updates.


-------------------

# PhotosLibraryExporter

## 简介
PhotoExport 是一个专为 macOS 用户设计的工具，它能够从你的 Photos 应用库中导出照片到任意指定目录。无论是备份、整理还是迁移你的照片集，PhotoExport 都能提供一种快速且直观的方法来完成这一任务。

## 特性
- 支持从“originals”和“Masters”路径中自动识别照片文件。
- 自动处理目标路径中的文件名冲突。
- 使用`tqdm`库实时展示复制进度，让整个过程更加透明。
- 简单的命令行界面，易于使用。

## 安装要求
本工具需要Python 3.x环境，并且依赖于以下Python库：
- `os`
- `shutil`
- `pathlib`
- `tqdm`

请确保你的系统中已安装这些依赖。

## 使用方法

1. 克隆或下载本项目到本地。
2. 打开终端，切换到项目目录。
3. 使用以下命令运行脚本，替换`<PhotosLibraryPath>`和`<DestinationPath>`为你的Photos库路径和希望照片被复制到的目标路径：

```bash
python photo_export.py "<PhotosLibraryPath>" "<DestinationPath>"
```

4. 脚本将开始执行，并显示复制进度。

## 注意事项
- 请确保你有权限访问指定的Photos库路径和目标路径。
- 由于macOS的权限管理，你可能需要给予终端或Python足够的权限来访问Photos库。
- 本工具不会修改原始Photos库中的任何文件或结构，仅进行复制操作。

## 贡献
欢迎任何形式的贡献，包括但不限于新功能的提议、代码改进、文档更新等。

