import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_FunctionDef(self, node):
        # Check for function names that violate PEP8 conventions
        if not node.name.islower():
            self.errors.append(
                f"Function '{node.name}' violates PEP8 naming convention")

        self.generic_visit(node)

    def visit_Call(self, node):
        # Check for print statements (which are deprecated in Python 3)
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            self.errors.append(
                "Use of 'print' statement (deprecated in Python 3)")

        self.generic_visit(node)

def analyze_code(code):
    analyzer = CodeAnalyzer()
    try:
        tree = ast.parse(code)
        analyzer.visit(tree)
    except SyntaxError as e:
        return [f"Syntax error: {e}"]
    return analyzer.errors

if __name__ == "__main__":
    # Example usage:
    python_code = """
def hello_world():
    print ("Hello, world!")
    """

    errors = analyze_code(python_code)
    if errors:
        print("Code analysis found the following issues:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Code analysis found no issues.")
