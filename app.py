# -*- coding: utf-8 -*-
"""
@Author: ZBY
@date: 2025/05/10
@Description: flask启动文件
"""
import traceback

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from common.base_exception import ApiException
from rest_model.base_response import make_flask_response
from rest_model.response_model.response import FailedResp
from utils.log_utils import log
from views.demo_view import test_view

app = Flask(__name__)

# 蓝图注册
app.register_blueprint(test_view)

# 注册db
# db = SQLAlchemy(app)


@app.errorhandler(Exception)
def handle_exception(e):
    log.error(f"flask handle exception, error is: {traceback.format_exc()}")
    if isinstance(e, ApiException):
        return make_flask_response(FailedResp(message=e.get_message))

    return make_flask_response(FailedResp(message="内部错误，请联系工程师处理"))


@app.teardown_request
def request_teardown(error):
    # todo：需要看下这个函数是否在handle_exception之后还能执行？
    # 销毁资源，所有请求后销毁资源的都放这里
    # if not error:
    #     db.session.commit()
    # db.session.close()
    pass

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
