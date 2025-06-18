def main(*args, **kwargs):
    """
    ct, color test
    args 此时是一个元组(list,)
    后文中对args进行解包得到list
    usage: ct integer
    """
    try:
        # print(type(*args))
        # print(repr(*args))
        if len(*args) != 1:
            print("[CT Err] Too More Agrs")
        strings = " ".join(*args)
        
        integer = int(strings)
    except Exception as e:
        print(f"[CT Err] {e}")
        return
    colorstr = f"\033[{integer}m"
    reset = "\033[0m"
    print(f"[CT INFO] {colorstr} COLOR with ID \"{strings}\"{reset}")
