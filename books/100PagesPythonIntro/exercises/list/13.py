def remove_dunder(cmd):
    list = dir(cmd)
    rmv_dund = []
    for cmd in list:
        if cmd[0] != "_":
            rmv_dund.append(cmd)
    return rmv_dund

print(remove_dunder(list))
print(remove_dunder(tuple))
