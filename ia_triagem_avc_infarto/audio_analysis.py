import librosa
import librosa.feature
import numpy as np

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path)

    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

    features = {
        "tempo": tempo,
        "zcr": zcr,
        "mfcc_mean": np.mean(mfcc),
        "mfcc_std": np.std(mfcc)
    }

    return features
