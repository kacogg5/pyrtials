import argparse
import re


def replace_partials(code: str) -> str:
    # Function Partials (Form: int($))
    partial_pattern = re.compile(r"(?:\w+(?:\(.*\))?\.)*\w+\((?:[^()]+,|.+\(.+\).+," +
                                 r")? *(?:\w+ *= *)?\$ *(?:,[^()]+|,.+\(.+\).+)?\)")
    partials = re.findall(partial_pattern, code)

    for partial in partials:
        paren = -1
        bal = 1
        while abs(paren) < len(partial) and bal != 0:
            paren -= 1
            bal += (partial[paren] == ')') - (partial[paren] == '(')

        func = replace_partials(partial[:paren])
        params = re.split(r" *, *", partial[paren+1:-1])

        # replace sub-partials
        new_params = ', '.join(replace_partials(param) for param in params)

        # replace $ signs
        p = 0
        lambda_params = []
        while '$' in new_params:
            np = f'p{p}'
            lambda_params += [np]
            new_params = new_params.replace('$', np, 1)
            p += 1

        code = code.replace(partial, 'lambda ' + ', '.join(lambda_params) + f': {func}({new_params})')

    # Indexing Partials (Form: arr[$])
    indexing_pattern = re.compile(r"(?:\w+(?:\(.*\))?(?:\[.+])*\.)*" +
                                  r"\w+(?:\(.*\))?(?:\[.+])*\[(?:\$|\$:.*|.*:\$)]")
    index_partials = re.findall(indexing_pattern, code)

    for partial in index_partials:
        brack = -1
        bal = 1
        while abs(brack) < len(partial) and bal != 0:
            brack -= 1
            bal += (partial[brack] == ']') - (partial[brack] == '[')

        stem = replace_partials(partial[:brack])
        params = re.split(r" *: *", partial[brack+1:-1])

        # replace sub-partials
        new_params = ':'.join(replace_partials(param) for param in params)

        # replace $ signs
        p = 0
        lambda_params = []
        while '$' in new_params:
            np = f'p{p}'
            lambda_params += [np]
            new_params = new_params.replace('$', np, 1)
            p += 1

        code = code.replace(partial, 'lambda ' + ', '.join(lambda_params) + f': {stem}[{new_params}]')

    return code


parser = argparse.ArgumentParser(description='Run python with built-in partials')
parser.add_argument('-p', dest='path', default='', type=str, required=True)

args = parser.parse_args()

with open(args.path) as pyFile:
    program = pyFile.read().splitlines()

    program = '\n'.join(replace_partials(line) for line in program)

    exec(program)
