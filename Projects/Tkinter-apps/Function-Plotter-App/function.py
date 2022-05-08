import numpy as np
import matplotlib.pyplot as plt

# ----------------------------  Constants ------------------------------- #
replacements = {
    'sin': 'np.sin',
    'cos': 'np.cos',
    'exp': 'np.exp',
    '^': '**',
}

# think of more security hazards here
forbidden_words = [
    'import',
    'shutil',
    'sys',
    'subprocess',
]


# ================== Converter ================= #
def stringToFunction(string):
    ''' evaluates the string and returns a function of x '''
    for word in forbidden_words:
        if word in string:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func

# func = string2func(input('enter function: f(x) = '))
# a = float(input('enter lower limit: '))
# b = float(input('enter upper limit: '))
# x = np.linspace(a, b, 250)

# plt.plot(x, func(x))
# plt.xlim(a, b)
# plt.show()
