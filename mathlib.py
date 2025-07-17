# 模拟一个数学工具模块的内容
def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数"""
    return a * b

def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 模块级别的变量
PI = 3.14159
VERSION = "1.0.0"

# 在真实的模块文件中，通常会有这样的代码：
if __name__ == "__main__":
    print("This module is being run directly, not imported")
    # 这里可以放测试代码
else:
    print("This module is imported from the workding directory")