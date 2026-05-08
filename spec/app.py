'''
Features and requirements
'''

from .err import Feat, Req


class Tool(Req):
    '''This is a tool for use with opencode.'''

class Hello(Tool):
    '''
    This tool should shell out to the command line and do:

    $ echo Hello World!

    The tool should have filename: "hello-tool.ts"
    '''


class HelloPython(Tool):
    '''
    This tool should shell out to the command line and run:

    $ uv run main.py

    From the project root: /usr/backup-working/work/hello-tool

    The tool should have filename: "hello-python-tool.ts"
    '''
