# 1030
# author 官方
def allCellsDistOrder(R, C, r0, c0):
    ret = [(i, j) for i in range(R) for j in range(C)]
    ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    return ret