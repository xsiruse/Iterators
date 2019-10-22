from datetime import datetime


def log_path(path):
    def logger(func):
        def log(*args, **kwargs):
            func_str = func.__name__
            args_str = ', '.join(args)
            kwargs_str = ', '.join([':'.join([str(j) for j in i]) for i in kwargs.items()])
            with open(path, 'a') as f:
                f.write(f'{str(datetime.now())}\t')
                f.write(f'+{func_str}+\t')
                f.write(f'*{args_str}*\t')
                f.write(f'**{kwargs_str}**\t')
                f.write(f'-{str(func(*args, **kwargs))}-\t')
                f.write(f'\n============end of record=============\n')
            return func(*args, **kwargs)

        return log

    return logger
