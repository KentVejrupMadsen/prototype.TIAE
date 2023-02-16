from configuration.dataset \
    import \
    getBatchSize, \
    getColorSpectrum, \
    getEpoch, \
    getFullSize, \
    getImageHeight, \
    getImageSize, \
    getImageWidth, \
    getLoadOldWeigths, \
    getValidationSize

from configuration.location \
    import \
    getDataPath

from configuration.buffer \
    import \
    get_training_set, \
    get_validation_set, \
    set_training_set, \
    set_validation_set, \
    getNvidiaGpuMemoryLimit, \
    getUseGpu, \
    getLogicalGpus
