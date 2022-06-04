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
class RiskDimensions(str, Enum):
    BOOK = "book"
    CURVE = "curve"
    MDR = "mdr"

@dataclass
class CurveRates:
    data: xr.DataArray


@dataclass
class CurveData:
    
    data: xr.DataArray

    def __init__(self, data: xr.DataArray) -> None:
        assert RiskDimensions.CURVE in data.dims, "data must have dimension 'curve'"
        assert RiskDimensions.BOOK in data.dims, "data must have dimension 'book'"
        assert RiskDimensions.MDR in data.dims, "data must have dimension 'mdr'"
        self.data = data

    @property
    def curves(self) -> List:
        """
        Returns the list of curves.
        """
        return self.data.dims[RiskDimensions.CURVE]

    @property
    def mdrs(self) -> List:
        """
        Returns the list of mdrs.
        """
        return self.data.dims[RiskDimensions.MDR]

    @property
    def books(self) -> List:
        """
        Returns the list of books.
        """
        return self.data.dims[RiskDimensions.BOOK]

def query(query: Query) -> QueryResult:
    raise NotImplementedError


def delta_pnl(risk: CurveData, rate_moves: CurveRates) -> CurveData:
    return CurveData(risk.data * rate_moves.data)
