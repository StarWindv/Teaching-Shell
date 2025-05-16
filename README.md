# 🚀 stv_terminal - 轻量级自定义 Shell

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **teaching-terminal** 是一个可定制命令的 Shell 实现，提供丰富的交互功能和扩展能力。

## 📖 目录
- [特性亮点](#✨-特性亮点)
- [快速安装](#🚀-快速安装)
- [使用指南](#🕹️-使用指南)
  - [参数模式](#-参数解析模式)
  - [核心命令](#-核心命令表)
  - [别名管理](#🔗-别名管理)
  - [扩展开发](#🧩-自定义扩展)
- [错误处理](#🚨-错误与警告)
- [日志系统](#📝-日志记录)
- [项目结构](#🏗️-项目结构)
- [参与贡献](#🤝-参与贡献)
- [联系信息](#📬-联系信息)

---

## ✨ 特性亮点

- **基础命令**：原生支持 `cd`, `exit`, `clear`, `tree` 等常用指令
- **别名系统**：支持快速创建/删除命令别名
- **扩展机制**：通过 Python 脚本轻松添加自定义命令
- **智能反馈**：详细的错误码系统（如 `Err 000` 命令未找到）
- **操作审计**：自动记录所有输入命令至日志文件
- **安全防护**：阻止高风险操作（如 `.` 开头的别名）

---

## 🚀 快速安装

### 环境要求
- Python ≥ 3.7
- 依赖库：
  ```bash
  filetype
  stv_utils>=0.0.6
  stv_pytree>=0.0.6
  ```

### 安装步骤
1. 克隆仓库并进入目录：
   ```bash
   git clone https://github.com/StarWindv/teaching-terminal.git
   cd teaching-terminal
   ```
2. 一键安装：
   ```bash
   pip install .
   ```

---

## 🕹️ 使用指南

### ⚙️ 参数解析模式

#### 分隔符模式
```bash
stvsh [shell_command] -- [shell_options]
```
- **示例**：`stvsh "ls -l" -- --brief`

#### 无分隔符模式
```bash
stvsh [command_and_options]
```
- **示例**：`stvsh --shell-help`

---

### 📜 核心命令表

| 命令                | 功能描述                     |
|---------------------|----------------------------|
| `cd [path]`         | 切换工作目录                |
| `exit`              | 退出终端                   |
| `clear` / `cls`     | 清空屏幕内容               |
| `ori [command]`     | 调用系统原生 Shell 执行命令 |
| `alias [名] [命令]` | 创建命令别名               |
| `ac`                | 查看所有可用命令           |
| `help` / `/?`       | 显示帮助文档               |

---

### 🔗 别名管理

**创建别名**
```bash
alias ll 'ls -al'  # 创建 ll 作为 ls -al 的别名
```

**删除别名**
```bash
ra ll   # 删除单个别名
ra      # 重置所有别名
```

---

### 🧩 自定义扩展

1. 创建扩展目录（自动生成）：
   ```bash
   ~/.stv_terminal/command/
   ```
2. 添加 Python 脚本示例 (`hello.py`)：
   ```python
   def main(*args, **kwargs):
       print("👋 你好，自定义命令！")
   ```
3. 立即生效：
   ```bash
   hello  # 输出：👋 你好，自定义命令！
   ```
 你不能——或者说我不建议你定义某些破坏性的命令——比如一个包装了`rm -rf *`的命令，当然，选择权在你——用户是自由的嘛！

---

## 🚨 错误与警告

### 常见错误码
| 代码     | 说明                  |
|---------|---------------------|
| `Err 000` | 命令未找到            |
| `Err 001` | 权限不足             |
| `Err 005` | 目标文件不存在        |

### 系统警告
| 代码       | 说明                  |
|-----------|---------------------|
| `Warn 002` | 检测到别名循环警告    |
| `Warn 004` | 多层终端嵌套警告      |

---

## 📝 日志记录

- **存储路径**：`~/.stv_terminal/log/log.txt`
- **滚动机制**：超过 1000 行自动归档为 `log_{num}.bak.txt`

---

## 🏗️ 项目结构

```text
.
├── src/                  # 核心源码
│   └── stv_terminal/
│       ├── core/         # 核心模块（注册/解析）
│       ├── utils/        # 工具函数集
│       └── main.py       # 入口文件
├── docs/                # 文档资源
├── LICENSE             # 许可证文件
└── pyproject.toml      # 项目配置
```

---

## 🤝 参与贡献

欢迎通过 Issues 提交建议或通过 Pull Request 贡献代码！  

---

## 📬 联系信息

- **开发者**：星灿长风v (StarWindv)
- **邮箱**：starwindv.stv@gmail.com
- **项目主页**：[GitHub Repository](https://github.com/StarWindv/teaching-terminal)
