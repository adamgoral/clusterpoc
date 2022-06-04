from dataclasses import dataclass
from enum import unique, Enum
from typing import List
import xarray as xr


@dataclass
class Query:
    """
    Query class for the query.
    """
    timestamps: List

@dataclass
class QueryResult:
    """
    QueryResult class for the query.
    """
    data: xr.Dataset

@unique
class DataDimension(str, Enum):
    BOOK = "book"
    CURVE = "curve"
    MATURITY = 'mtty'
    MDR = "mdr"


@dataclass
class CurveData:
    data: xr.DataArray

    def __init__(self, data: xr.DataArray) -> None:
        assert DataDimension.CURVE in data.dims, "data must have dimension 'curve'"
        assert DataDimension.MDR in data.dims, "data must have dimension 'mdr'"
        self.data = data


    @property
    def curves(self) -> List:
        """
        Returns the list of curves.
        """
        return self.data.coords[DataDimension.CURVE]

    @property
    def mdrs(self) -> List:
        """
        Returns the list of mdrs.
        """
        return self.data.coords[DataDimension.MDR]

    def __mul__(self, other) -> 'CurveData':
        if type(other) is CurveData:
            return CurveData(self.data * other.data)
        
        return CurveData(self.data * other)

def query(query: Query) -> QueryResult:
    raise NotImplementedError

def delta_pnl(delta_risk: CurveData, rates_moves: CurveData) -> CurveData:
    return delta_risk * rates_moves * 10_000

