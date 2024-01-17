def say_hi_gender(full_name,gender):
    if gender == '男':
        gender = '先生'
    elif gender == '女':
        gender = '女士'
    else:
        gender = '先生/女士'
    
    return (f"尊敬的{full_name}{gender},欢迎来到火星！")
    

full_name = input()
gender = input()
print(say_hi_gender(full_name,gender))