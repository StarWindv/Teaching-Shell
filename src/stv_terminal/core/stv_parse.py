import sys
from sys import argv

def helper():
    text = f"""\
    格式: `{argv[0]} shell_command -- shell_options`
    
    `shell_command` 指直接运行的命令
    `--` 分隔符, 用来分隔命令与shell参数
    `shell_options` 指shell的行为参数
    
    Options   Shot Cuts   Aliases                 Description
    --help       -h       help/--shell-help/-sh   输出帮助信息并退出
    --brief      -b         None                  禁止bash输出详细信息
    --exit       -e         None                  运行`command`并退出
    
    格式: `{argv[0]} command_and_options`
    - 此模式下, shell参数退化为`shell-help`、`-sh`、`--shell-help`
      即输出帮助信息一个参数, 不支持其他shell选项
    """
    print(text)

def parser():
    """
    因为参数不多，所以就没用argparse
    :return: Tuple[bool, list, [dict or None]]
    """
    script = argv[0]
    args = argv[1:]
    arg_str = " ".join(args)
    counts = arg_str.count(" -- ")
    if counts > 1:
        print(f"|> [Err 002] Parameter quantity not aligned")
        print(f"|> ··········^ In Process Arg Parse")
        sys.exit(2)
    
    """
    思考了一下，既然要做到类似`bash command`的效果，那么就应该是
    在--前放命令等参数
    在--后放bash选项的参数

    如果不存在--，检测有没有特定参数.
    """
    if counts == 1:
        """
        bash command -- bash_options
        """
        command, bash = arg_str.split(" -- ")
        bash = list(map(str, bash.split()))
        if ("-h" in bash) or ("--help" in bash) \
                          or ("help" in bash) \
                          or ("--shell-help" in bash) \
                          or ("shell-help" in bash) \
                          or ("-sh" in bash):
            helper()
            sys.exit(0)

        command = list(map(str, command.split()))

        result = {
            "brief": False,
            "exit": False,
            "script": script,
            "full_args": " ".join(args),
        }

        if ('-b' in bash) or ('--brief' in bash):
            result['brief'] = True
        if ('-e' in bash) or ('--exit' in bash):
            result['exit'] = True

        return True, command, result
    """
    第一个True: 有分隔符
    command: 指直接使用bash运行的命令列表
    result: bash options
    """

    # 接下来是无分隔符模式, 想了想, 直接做成无bash参数模式，因为懒

    if ("-sh" in args) or ("--shell-help" in args) or ("shell-help" in args):
        helper()
        sys.exit(0)

    """
    第一个False: 无分隔符
    args: 指去除了脚本名称的参数列表
    None: 为了对齐参数而加的, 无实意
    """
    return False, args, None