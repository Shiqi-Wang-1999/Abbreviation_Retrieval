class BaseJsonObject(object):
    def __init__(self, code=200,success=True, message='', data=None):
        super(BaseJsonObject, self).__init__()
        self.code = code
        self.success=success
        self.message = message
        self.data = data

    def info(self):
        return self.__dict__


class SuccessJsonObject(BaseJsonObject):
    def __init__(self, data=None):
        super(SuccessJsonObject, self).__init__()
        self.code = 200
        self.success=True
        self.message = '成功'
        self.data = data


class ErrorJsonObject(BaseJsonObject):
    def __init__(self, message='服务内部错误', data=None):
        super(ErrorJsonObject, self).__init__()
        self.code = 500
        self.success=False
        self.message = message
        self.data = data
