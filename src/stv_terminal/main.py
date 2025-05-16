import os
import shlex
import sys

from getpass import getuser
from stv_utils import colorize, suppress_print

from stv_terminal.utils.utils import (log, depth_check)
from stv_terminal.utils.initialize import register_builtin_commands
from stv_terminal.core.Register import CommandRegistry
from stv_terminal.core.stv_parse import parser

parse_result = parser()
if parse_result is None:
    mode, parse_arg, result = False, [], {}
else:
    mode, parse_arg, result = parse_result
if mode:
    need_brief = result["brief"]
    need_exit = result["exit"]
else:
    need_brief = False
    need_exit = False


@colorize(start_str="|> [Ban", color_code="\033[91m")
@colorize(start_str="|> [Warn", color_code="\033[33m")
@colorize(start_str="|> [Err", color_code="\033[95m")
@colorize(start_str="|> [HELP]", color_code="\033[96m")
@colorize
@suppress_print(start_str="|>", suppress=need_brief)
def main():
    """启动终端循环"""
    register_builtin_commands()
    print(f"|> 初始化终端变量")
    log_path = os.path.join(os.path.expanduser("~"), "stvlog/log.txt")
    username = getuser()
    print(f"|> 启动终端循环")

    depth = depth_check()
    if depth[-1]:
        if depth[0] >= 2:
            print(f"|> [Warn 004] Multi layer terminal nesting")

    args = sys.argv[1:] if parse_arg == [] else parse_arg

    while True:
        try:
            cwd = os.getcwd()
            if cwd == os.path.expanduser("~"):
                cwd = "~"
            prompt = f"\n{username}:{cwd} $ "
            if not args:
                line = input(prompt).strip()
            else:
                line = " ".join(args)
            if not line:
                continue

            log(log_path, line)
            parts = shlex.split(line)
            command = parts[0] if parts else ""
            args = parts[1:]
            CommandRegistry.execute(command, args)
            if need_exit and mode:
                break
            command = ''
            args = []
            

        except PermissionError:
            print("|> [Err 001] Permission Denied")
            continue
        except KeyboardInterrupt:
            print("\n|> [^C] 已中断当前操作")
            continue
        except EOFError:
            print(f"\n|> 退出终端循环")
            break
        except Exception as e:
            print(f"|> [Err -02] Inner Error")
            print(f"|> [ErrInfo] {e}")

if __name__ == "__main__":
    main()