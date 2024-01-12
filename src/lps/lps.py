import numpy as np
from Levenshtein import distance
import torch
from torch.nn import Module
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC


class PhonemePredictor(Module):
    def __init__(self, checkpoint="facebook/wav2vec2-lv-60-espeak-cv-ft", sr=16000):
        super().__init__()
        self.processor = Wav2Vec2Processor.from_pretrained(checkpoint)
        self.model = Wav2Vec2ForCTC.from_pretrained(checkpoint)
        self.sr = sr

    def forward(self, waveform):
        input_values = self.processor(waveform, return_tensors="pt", sampling_rate=self.sr).input_values
        # retrieve logits
        logits = self.model(input_values).logits

        # take argmax and decode
        predicted_ids = torch.argmax(logits, dim=-1)
        return self.processor.batch_decode(predicted_ids)


class LevenshteinPhonemeSimilarity:
    def __init__(self):
        self.phoneme_predictor = PhonemePredictor()

    def __call__(self, sample: np.ndarray, reference: np.ndarray) -> float:
        sample_phonems = self.phoneme_predictor.forward(sample)[0].replace(" ", "")
        ref_phonems = self.phoneme_predictor.forward(reference)[0].replace(" ", "")
        lev_distance = distance(sample_phonems, ref_phonems)
        return 1 - lev_distance / len(ref_phonems)
