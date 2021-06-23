from typing import Callable, List, Dict
from inspect import getmembers, iscoroutinefunction, isfunction
import inspect
import os
import importlib.util
from discord.ext.commands import context
from util import util

dir = os.getcwd()
dir += "/tests"
print(dir)
tests: list[tuple[Callable, bool]] = []
def is_valid_script(file):
    module = __name__.split(".")[-1]
    name = file.split(".")[0]
    extension = file.split(".")[-1]
    if extension == file:
        return False
    if name == module:
        return False
    return extension == "py"
for file in os.listdir(dir):
    if is_valid_script(file):
        path_dir = dir + "/" + str(file)
        name = "tests/" + file
        spec = importlib.util.spec_from_file_location(name, path_dir)
        module = importlib.util.module_from_spec(spec)
        module.__package__ = "tests"
        spec.loader.exec_module(module)
        for name, value in getmembers(module):
            if isfunction(value):
                print(f"{name} is a function")
                module_name = module.__name__.lower().split("/")[-1]
                module_name = module_name.split(".")[0]
                if module_name == name:
                    print(f"{name} is the right function")
                    tests.append((value, iscoroutinefunction(value)))

async def run(ctx: context) -> None:
    """
    Runs all the tests avialable to the bot
    """
    print("Running tests...")
    for test in tests:
        function = test[0]
        is_async = test[1]
        await util.print_and_send(ctx, f"Running test {function.__name__}")
        if is_async:
            await function(ctx)
        else: 
            function()