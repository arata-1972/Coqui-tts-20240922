import _codecs
import importlib.metadata
from collections import defaultdict

import numpy as np
import torch

from TTS.config.shared_configs import BaseDatasetConfig
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsArgs, XttsAudioConfig
from TTS.utils.radam import RAdam

__version__ = importlib.metadata.version("coqui-tts")


torch.serialization.add_safe_globals([dict, defaultdict, RAdam])

# Bark
torch.serialization.add_safe_globals(
    [
        np.core.multiarray.scalar,
        np.dtype,
        np.dtypes.Float64DType,
        _codecs.encode,  # TODO: safe by default from Pytorch 2.5
    ]
)

# XTTS
torch.serialization.add_safe_globals([BaseDatasetConfig, XttsConfig, XttsAudioConfig, XttsArgs])
