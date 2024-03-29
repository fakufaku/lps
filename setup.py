from setuptools import setup, find_packages

setup(
    name="levenshtein-phoneme-similarity",
    version="1.0",
    author="Jan Pirklbauer",
    author_email="jan.pirklbauer@tu-bs.de",
    description="Implementation of the Levenshtein Phoneme Distance",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'levenshtein',
        'phonemizer',
        'transformers'
    ],
    python_requires='>=3.8'
)
