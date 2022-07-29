from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def user_resolver(obj, info, id):
    return {
        "id": id,
    }

@convert_kwargs_to_snake_case
def createUser_resolver(obj, info, id):
    return {
        "id": id,
    }
