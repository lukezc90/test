# coding=utf-8
# 捕获异常

def test_error(a, b):
	try:
		print(a/b)
		print("正确的")
	except :  # 在多种异常处理都情况下，写多个except，每个except对应一个异常的处理方式
		print("发生异常之后执行的")
		return 1
	else:
		print("如果没有异常执行这里")
		return 1
	finally:
		print("不管有没有异常，都执行这里")
		return 1
	# return 1

test_error(1,1)

