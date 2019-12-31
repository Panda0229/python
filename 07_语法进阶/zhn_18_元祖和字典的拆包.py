def demo(*args,**kwargs):

    print(args)
    print(kwargs)


# 在开发时，要把元组变量或者字典变量直接传递到函数内部时，需要拆包
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums,gl_dict)  # 元祖和字典都传递到args,需要使用拆包
demo(*gl_nums,**gl_dict)  # 拆包语法，简化元祖变量和字典变量的传递

demo(1, 2, 3, name = "小明", age = 18)  # 不用拆包解决方法


