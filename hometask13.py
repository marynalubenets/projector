# Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs

def decorator(func):
    def wrapper(**kwargs):
        if kwargs['user_type'] == 'admin': # checking if user is an admin
            func(**kwargs) # in case when user is an admin execute an inner function
        else: # if user is not an admin display a denial message
            print('You are not an admin. Access denied')
    return wrapper

@decorator # calling a function with decorator
def critical_funcion(user_type) -> str:
    print('This function is only accesible by admins.')

# test runs
critical_funcion(user_type = 'admin')
critical_funcion(user_type = 'not_admin')


# Write a decorator that wraps a function in a try-except block and print an error if error has happened


def catch_errors(func):              # a decorator that wraps a function in a try-except block
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:       # writing exception if correct key is not found
            print(f'Found 1 error during execution of your function: KeyError no such key as {e}')
    return wrapper

@catch_errors                        
def some_function_with_risky_operation(data) -> dict:
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})    # calling a fucntion 
some_function_with_risky_operation({'key': 'bar'})