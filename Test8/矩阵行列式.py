import numpy 
try:
    a = numpy.array(eval(input())) 
    print(round(numpy.linalg.det(a),2))
    # print(round(np.linalg.det(a),2))
except:
    print("输入错误！")