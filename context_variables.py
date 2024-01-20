"""

What are Context Variables?

    Context-Specific Data: Context variables are variables whose values are specific to a certain context, such as an
    execution thread or a chain of asynchronous tasks. This is similar to thread-local storage, but contextvars are
    designed to work correctly with asynchronous code.

    Isolation Between Contexts: Each context can have its own independent set of values for context variables, so
    changes in one context do not affect others. This is particularly useful in scenarios like handling web requests
    where each request can have its own context and related data.

Why are Context Variables Useful?

    Asynchronous Programming: In asynchronous programming, multiple tasks can be running in the same thread but not
    necessarily in a predictable sequence. Traditional thread-local storage doesn't work well in this scenario because
    it's tied to threads, not to the logical execution flow of asynchronous tasks.

    Maintaining State: They allow for maintaining state in a way that's correctly scoped to the flow of control,
    especially across various asynchronous operations.


"""

import asyncio
from contextvars import ContextVar

# Define a context variable
request_id = ContextVar('request_id')


async def process_request(id):
    token = request_id.set(id)
    # ... do some async operations
    await asyncio.sleep(1)  # Simulating an async operation
    print(f"Processing request {request_id.get()}")
    request_id.reset(token)


async def main():
    await asyncio.gather(
        process_request(1),
        process_request(2)
    )


asyncio.run(main())
