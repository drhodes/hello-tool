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

    From the project root: 
    The tool should have filename: "hello-python-tool.ts"
    '''



class HelloXPath(Tool):
    '''This tool should shell out to the command line and run:
    $ uv run xpath.py <query>

    The tool should open a random .xml file from the directory

    ./spec-build/spec-4236519a509c9e07ac8b.xml

    Then it should run the query on it.
    
    The tool should have filename: "hello-xpath.ts"
    '''
