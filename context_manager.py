"""

In Python, a context manager is a way to allocate and release resources precisely when you want to.
The most widely used example of context managers is the with statement, which is used for unmanaged
resources (like file streams). A context manager handles the setup and teardown of resources, and it
ensures that resources are properly cleaned up regardless of whether the code block runs successfully
or raises an error.

example:

Database connection object (which then automagically closes the connection once the corresponding
'with'-statement goes out of scope)



class DatabaseConnection(object):

    def __enter__(self):
        # make a database connection and return it
        ...
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.dbconn.close()
        ...

"""


class FileOpener:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Open the file and return it
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the file if it was successfully opened
        if self.file:
            self.file.close()


# Usage:
with FileOpener('large_log_file.log') as file:
    data = file.read()

"""
The `__enter__` and `__exit__` methods are part of the context management protocol in Python. They work together to 
ensure that resources are allocated and released properly.

Here's a step-by-step explanation of how they work:

### `__enter__` method

1. **Initialization**: When a context manager is entered using the `with` statement, Python calls the `__enter__` method 
of the context manager object.
   
2. **Resource Allocation**: The `__enter__` method is responsible for acquiring the resource that needs to be managed, 
such as opening a file or acquiring a lock. This is where any setup code will run.

3. **Returning the Resource**: After acquiring the resource, the `__enter__` method returns the resource so it can be 
used inside the `with` block. The value returned by `__enter__` is bound to the variable after the `as` keyword in the 
`with` statement.

### `__exit__` method

1. **Exception Handling**: The `__exit__` method is called when the `with` block is exited for any reason, be it 
because of successful execution, an exception being raised, or the `return`, `continue`, or `break` statements being used to exit the block.
   
2. **Resource Releasing**: Inside `__exit__`, you should release or clean up the resource that was acquired in 
`__enter__`. This ensures that the resource is properly freed, even if an exception was raised in the `with` block.

3. **Parameters of `__exit__`**:
   - `exc_type`: The exception class if an exception has occurred, otherwise `None`.
   - `exc_val`: The exception instance if an exception has occurred, otherwise `None`.
   - `exc_tb`: The traceback object if an exception has occurred, otherwise `None`.

4. **Exception Suppression**: If the `__exit__` method returns `True`, any exception that occurred within the `with` 
block is suppressed, and the execution continues immediately after the `with` block. If `False` is returned (which is 
the default if you don't explicitly return a value), the exception is re-raised after the `__exit__` 
method is completed.


Context managers are particularly useful for ensuring that clean-up logic is executed. 
For example, in file handling, even if an error occurs while processing the file, you want to make sure 
that the file is closed properly. The context manager's `__exit__` method guarantees that the file's `close` 
method will be called, regardless of how the `with` block is exited.

"""
