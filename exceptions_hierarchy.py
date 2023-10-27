"""

Definition of Exceptions:

At the most fundamental level, exceptions in Python are objects.
Like everything else in Python, they are instances of classes.
The base class for all built-in exceptions is BaseException,
though it's more common to derive custom exceptions from the Exception class,
a subclass of BaseException.

"""


# Handling exceptions:

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError as e:
#         print(f"Error: {e}")
#         print("Oops!  That was no valid number.  Try again...")

# Raising exceptions:

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# Exception Chaining

# Chain exception may occur:

# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error") from None

# def func():
#     raise ConnectionError
#
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc


# try:
#     raise KeyboardInterrupt
#
# finally:
#     print('Goodbye, world!')


# def bool_return():
#     try:
#         return True
#     finally:
#         return False
#
# print(bool_return())


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


"""

As you can see, the finally clause is executed in any event. 
The TypeError raised by dividing two strings is not handled 
by the except clause and therefore re-raised after the finally 
clause has been executed. In real world applications, the 
finally clause is useful for releasing external resources (such 
as files or network connections), regardless of whether the use 
of the resource was successful.

"""
# divide(2, 1)
#
#
# divide(2, 0)
#

divide("2", "1")

"""

Hierarchy

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning

"""
