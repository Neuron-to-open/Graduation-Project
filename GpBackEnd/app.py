# /****************************************************************************
# * Author: Jiayi.Yi
# * Date: 2024/3/12
# * jdk version: java 17.0.3.1 2022-04-22 LTS
# * 系统版本： Windows 11 家庭版 20H2
# * IDE: IntelliJ IDEA
# * 编程语言: Java
# * =========== ====== ===== ==============================================
# * @Copyright (C) Yijiayi All Rights reserved
# *****************************************************************************/

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

