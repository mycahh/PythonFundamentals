class CustomWith:
    
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.name = open(self.name, 'r', encoding='utf8')
        print('Getting Recourses'.center(50, '-'))
        return self.name
    
    def __exit__(self, exception_type, value_exception, traceback_error):
        print('Closing Recourses'.center(50, '-'))
        if self.name:
            self.name.close()


