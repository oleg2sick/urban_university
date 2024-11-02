import inspect


def introspection_info(obj):
    result = {}

    obj_type = type(obj)
    result['type'] = obj_type
    
    obj_attr = [attr for attr in dir(obj)
                if not callable(getattr(obj, attr))]
    result['attr'] = obj_attr

    obj_methods = [method for method in dir(obj)
                   if callable((getattr(obj, method)))]
    result['methods'] = obj_methods

    obj_module = inspect.getmodule(obj)
    result['module'] = obj_module

    return result


print(introspection_info(42))
