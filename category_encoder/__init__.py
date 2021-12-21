"""

.. module:: category_encoder
  :synopsis:
  :platform:

"""

from category_encoder.backward_difference import BackwardDifferenceEncoder
from category_encoder.binary import BinaryEncoder
from category_encoder.count import CountEncoder
from category_encoder.hashing import HashingEncoder
from category_encoder.helmert import HelmertEncoder
from category_encoder.one_hot import OneHotEncoder
from category_encoder.ordinal import OrdinalEncoder
from category_encoder.sum_coding import SumEncoder
from category_encoder.polynomial import PolynomialEncoder
from category_encoder.basen import BaseNEncoder
from category_encoder.leave_one_out import LeaveOneOutEncoder
from category_encoder.target_encoder import TargetEncoder
from category_encoder.woe import WOEEncoder
from category_encoder.m_estimate import MEstimateEncoder
from category_encoder.james_stein import JamesSteinEncoder
from category_encoder.cat_boost import CatBoostEncoder
from category_encoder.glmm import GLMMEncoder
from category_encoder.quantile_encoder import QuantileEncoder, SummaryEncoder

__version__ = '2.3.0'

__author__ = "willmcginnis", "cmougan"

__all__ = [
    "BackwardDifferenceEncoder",
    "BinaryEncoder",
    "CountEncoder",
    "HashingEncoder",
    "HelmertEncoder",
    "OneHotEncoder",
    "OrdinalEncoder",
    "SumEncoder",
    "PolynomialEncoder",
    "BaseNEncoder",
    "LeaveOneOutEncoder",
    "TargetEncoder",
    "WOEEncoder",
    "MEstimateEncoder",
    "JamesSteinEncoder",
    "CatBoostEncoder",
    "GLMMEncoder",
    "QuantileEncoder",
    "SummaryEncoder",
]
