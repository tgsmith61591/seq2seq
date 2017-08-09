import keras.backend as kb


if kb.backend() == 'tensorflow':
    from .tensorflow_backend import *
    rnn = lambda *args, **kwargs: kb.rnn(*args, **kwargs) + ([],)
elif kb.backend() == 'theano':
    from .theano_backend import *
else:
    raise ValueError(kb.backend() + ' backend is not supported.')

__all__ = [s for s in dir() if not s.startswith("_")]
