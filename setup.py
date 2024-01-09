from setuptools import setup, find_packages

setup(
    name="levenshtein-phoneme-similarity",
    version="0.0.2",
    author="Jan Pirklbauer",
    author_email="jan.pirklbauer@tu-bs.de",
    description="Implementation of the Levneshtein Phoneme Distance",
    package_dir={"": "src"},
    packages=find_packages(),
    install_requires=[
        'levenshtein',

    ],
    python_requires='>=3.8'
)
