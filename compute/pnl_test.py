from pnl import CurveData, RiskDimensions
import xarray as xr

def test_constructor():
    data = xr.DataArray(data=[[[0]]], dims=[RiskDimensions.CURVE, RiskDimensions.BOOK, RiskDimensions.MDR])
    CurveData(data)
