# 與線段相關的運算模組

# 計算線段的長度
def len(x1,y1,x2,y2):
    return (((x2-x1)**2)+((y2-y1)**2))**0.5

# 計算線段的斜率
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)