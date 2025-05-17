# 1. 简介
 ## 1.1 项目说明

base_config: 项目的配置目录，保存如数据库连接、日志配置等信息

common: 通用模块，项目中的异常类、全局变量等信息

docs: 项目的文档说明，包括readme和api接口文档

logs: 项目运行后日志文件默认保存目录

request: flask请求相关的实现，包括封装的FlaskView视图类等

rest_model: 基于pydantic的flask请求和响应数据的实现

test: 单元测试目录

utils: 工具类目录

views: 真正的flask业务蓝图逻辑

## 1.2 FlaskView类说明

（1）基于flask项目的通用视图类，实现了请求和响应的自定义化，减少了每个蓝图中都需要解析请求的步骤

（2）支持自定义基于pydantic BaseModel的请求参数和响应，封装了对于请求格式的默认校验，支持自定义业务校验逻辑

（3）统一了请求的返回模型，基于BaseModel模型返回flask响应

（4）支持业务逻辑的定制

 类的用法（可以参考demo_view.py）：

- 每个api请求，都需要用户继承FlaskView类，并且定义其中两个关键的成员变量：request_param和request_body和methods请求方式。
- 用户可以实现其中的抽象方法：validate()和handle_request()，方法需要返回BaseModel类及其子类
- 用户可以无需关注处理异常，由flask切面来捕获异常并返回错误信息
- 可以在业务处理逻辑中任何时刻抛出异常和异常信息，这些信息将被返回
- 和两个抽象方法中，用户可以使用上下文RequestContext传递信息，其中如果需要获取请求的相关信息，则可以使用RequestContext.get_property(COMMON_REQ),返回一个CommonRequest对象，此对象（成员变量已经转化为BaseModel类对象）保存了flask请求所有信息
