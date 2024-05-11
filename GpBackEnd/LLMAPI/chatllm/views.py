from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chatllm.models import User, Assessment
from paddlenlp.transformers import AutoModelForCausalLM, AutoTokenizer

# Create your views here.
@csrf_exempt
def add(request):
    """
    处理添加评估信息的请求。
    
    参数:
    - request: HTTP请求对象，包含请求的方法、数据等信息。
    
    返回值:
    - JsonResponse对象，包含操作结果信息（消息和错误码）。
    """
    response = {}  # 初始化响应字典
    
    # 检查请求方法是否为POST
    if request.method == 'POST':
        print(request.POST)
    else:
        # 如果不是POST请求，返回错误信息
        response['msg'] = "It's not a post request"
        response['error_num'] = -1
        return JsonResponse(response)
    
    try:
        # 尝试创建评估对象并填充数据
        data = request.POST
        assessment = Assessment()
        assessment.llm = data.get('llm')
        assessment.datasetname = data.get('datasetname')
        remark = data.get('remark')
        remark = float(remark)  # 将remark转换为浮点数
        assessment.remark = remark
        assessment.save()  # 保存评估对象
        response['msg'] = 'successfully accept'
        response['error_num'] = 0
    except Exception as e:
        # 捕获异常，将异常信息返回
        response['msg'] = str(e)   
        response['error_num'] = 1 

    return JsonResponse(response)        


@csrf_exempt
def register(request):
    """
    用户注册功能实现。
    
    参数:
    - request: HTTP请求对象，包含用户提交的注册信息。
    
    返回值:
    - JsonResponse对象，包含注册结果的信息，如成功或失败的消息以及错误码。
    """
    response = {}  # 初始化响应字典
    
    # 检查请求方式是否为POST
    if request.method == 'POST' :
        print(request.POST)  # 打印POST请求信息
    else :
        # 如果不是POST请求，返回错误信息
        response['msg'] = "It's not a post request"
        response['error_num'] = -1
        return JsonResponse(response)
    
    try:
        data = request.POST  # 获取POST请求数据
        print(data)
        username = data.get('name')  # 提取用户名
        password = data.get('password')  # 提取密码

        # 创建用户实例并保存
        user = User()
        user.name = username
        user.password = password
        user.save()

        # 注册成功，设置响应信息
        response['msg'] = 'successfully register'
        response['error_num'] = 0
    except Exception as e:
            # 捕获异常，设置响应信息
            response['msg'] = str(e)
            response['error_num'] = 1

    # 返回响应
    return JsonResponse(response)

        
@csrf_exempt
def login(request):
    """
    处理用户登录请求。
    
    参数:
    - request: HTTP请求对象，包含请求方法、请求数据等信息。
    
    返回值:
    - JsonResponse对象，包含登录结果信息，如成功则包含成功消息和错误码0，如失败则包含失败消息和错误码-1。
    """
    response = {}  # 初始化响应字典
    
    # 检查请求方法是否为POST    
    if request.method == 'POST':
        print(request.POST)  # 打印POST请求参数
    else:
        # 如果请求方法不是POST，则设置错误信息并返回
        response['msg'] = "It's not a post request"
        response['error_num'] = -1
        return JsonResponse(response)
    
    # 从请求中获取用户名和密码
    data = request.POST
    print(data)
    input_name = data.get('username')
    input_password = data.get('password')

    # 检查用户是否存在
    result = User.objects.filter(name=input_name, password=input_password).exists()
    print(result)
    if result:
        # 如果用户存在，设置成功登录信息
        response['msg'] = 'successfully login'
        response['error_num'] = 0
    else:
        # 如果用户不存在，设置失败信息
        response['msg'] = "It's not a POST request"
        response['error_num'] = -1

    # 返回响应
    return JsonResponse(response)


@csrf_exempt
def chat(request):
    """
    处理用户聊天请求的函数。
    
    参数:
    - request: HttpRequest对象，包含客户端发来的HTTP请求信息。
    
    返回值:
    - JsonResponse对象，包含处理结果的JSON格式数据。
    """
    response = {}  # 初始化响应字典
    
    # 检查请求方法是否为POST
    if request.method == 'POST':
        print(request.POST)  # 打印POST请求参数
    else:
        # 如果请求方法不是POST，则设置错误信息并返回
        response['msg'] = "It's not a POST request"
        response['error_num'] = -1
        return JsonResponse(response)
    
    try:
        data = request.POST
        query = data.get('query')
        answer = UseBC(query)
        # 设置欢迎信息和处理成功的状态
        response['answer'] = answer
        response['msg'] = 'successfully chat'
        response['error_num'] = 0

    except Exception as e:
        # 捕获异常，设置响应信息
        response['msg'] = str(e)
        response['error_num'] = 1
        

    return JsonResponse(response)



# @csrf_exempt
# def show(request):





def UseBC(query:str) :
    model = AutoModelForCausalLM.from_pretrained("baichuan-inc/Baichuan-7B")
    tokenizer = AutoTokenizer.from_pretrained("baichuan-inc/Baichuan-7B")
    print(query)
    input_features = tokenizer(query, return_tensors="pd")
    outputs = model.generate(**input_features, max_length=128)
    result = tokenizer.batch_decode(outputs[0])

    return result