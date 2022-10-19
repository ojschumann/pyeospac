#!/usr/bin/python
# -*- coding: utf-8 -*-
# cython: language_level=2
import numpy as np
cimport numpy as np

import constants as cst
from libc.stdlib cimport malloc, free
# to use the Numpy-C-API from Cython
np.import_array()


ctypedef np.int32_t int32
ctypedef np.float64_t float64


cdef extern from "eos_types_internal.h":
    struct eos_Option:
       pass

cdef extern from "":
    struct eos_Data:
       pass

cdef extern from "eos_SesUtils.h":
    cdef int  eos_SesCleanFileCache()



cpdef eospac_clean_cache():
    return eos_SesCleanFileCache()

