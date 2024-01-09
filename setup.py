from setuptools import setup, find_packages

setup(
    name="levenshtein-phoneme-similarity",
    version="0.0.1",
    author="Jan Pirklbauer",
    author_email="jan.pirklbauer@tu-bs.de",
    description="Implementation of the Levneshtein Phoneme Distance",
    packages=find_packages(),
    install_requires=[
        'levenshtein',

    ],
    python_requires='>=3.8'
)