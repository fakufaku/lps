# Levenshtein Phoneme Similarity

This repository contains the implementation of the Levenshtein Phoneme Similarity (also known as 1-LPD) as described in [Pirklbauer+23]

## Installation
### Prequisits
- torch, tochvision, torchaudio (install according to your GPU setup)
- espeak (install e.g. via `apt install espeak` on Ubuntu)

### Setup via pip
Install into your environment using

```
pip install levenshtein-phoneme-similarity --index-url https://__token__:zEgV8cqKJhxGfSyJWbFP@git.rz.tu-bs.de/api/v4/projects/5147/packages/pypi/simple
```

## Usage
Example usage for sound files "sample.wav" and "reference.wav":

```python
from lps import LevenshteinPhonemeSimilarity
import soundfile as sf
(ref, _), (sample, _) = sf.read("reference.wav"), sf.read("sample.wav")
lps = LevenshteinPhonemeSimilarity()
print(f"LPS between ref and sample is{lps(sample, ref):.2%}")
```

## Citation
When using the provided metric, please cite

```
@INPROCEEDINGS{Pirklbauer+23,
  author={Pirklbauer, Jan and Sach, Marvin and Fluyt, Kristoff and Tirry, Wouter and Wardah, Wafaa and Moeller, Sebastian and Fingscheidt, Tim},
  booktitle={Proc. of 15th ITG Conference on Speech Communication}, 
  title={Evaluation Metrics for Generative Speech Enhancement Methods: Issues and Perspectives}, 
  year={2023},
  month={Sep},
  address={Aachen, Germany},
  pages={265-269}
}
```