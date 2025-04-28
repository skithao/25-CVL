"""
练习: 面向对象编程基础

描述：
在本练习中，您将学习如何定义类和创建对象，理解面向对象编程的基本概念。

请补全下面的Student类，实现相关方法。
"""

class Student:
    """
    学生类
    
    请补全以下方法:
    - __init__: 初始化学生信息
    - print_info: 打印学生信息
    """
    
    def __init__(self, name, age, grade):
        """
        初始化学生对象
        
        参数:
        - name: 学生姓名
        - age: 学生年龄
        - grade: 学生成绩
        """
        # 请在下方编写代码，完成属性初始化
        self.name = name
        self.age = age
        self.grade = grade
        pass
    
    def print_info(self):
        """
        打印学生信息
        
        打印格式:
        姓名: [name], 年龄: [age], 成绩: [grade]
        
        返回:
        - 无返回值，直接打印信息
        """
        # 请在下方编写代码，完成打印学生信息的功能
        print("姓名: {}, 年龄: {}, 成绩: {}".format(self.name, self.age, self.grade))
        pass
    
    def is_passing(self):
        """
        判断学生是否通过考试
        
        标准:
        - 成绩大于等于60分为通过
        
        返回:
        - 布尔值，表示是否通过考试
        """
        # 请在下方编写代码，完成判断功能
        if self.grade >= 60:
            return True
        else:
            return False
        pass


def create_student_example():
    """
    创建一个Student类的实例并调用方法
    
    返回:
    - 创建的Student对象
    """
    # 请在下方编写代码
    # 创建一个Student对象，设置姓名为"张三"，年龄为18，成绩为85
    # 调用print_info()方法打印学生信息
    # 返回创建的Student对象
    student = Student("张三", 18, 85)
    student.print_info()
    return student
    pass 