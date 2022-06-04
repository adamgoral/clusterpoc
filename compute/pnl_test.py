from pnl import CurveData, DataDimension, delta_pnl
import pytest
import xarray as xr

def test_constructor():
    data = xr.DataArray(data=[[[0]]], dims=[DataDimension.CURVE, DataDimension.BOOK, DataDimension.MDR])
    CurveData(data)

def test_constructor_fail():
    data = xr.DataArray()
    with pytest.raises(AssertionError):
        CurveData(data)

def test_delta_pnl():
    data = xr.DataArray(data=[[1]], dims=[DataDimension.CURVE, DataDimension.MDR])
    delta_risk = CurveData(data)
    data = xr.DataArray(data=[[1]], dims=[DataDimension.CURVE, DataDimension.MDR])
    rates_moves = CurveData(data)
    result = delta_pnl(delta_risk, rates_moves)
    assert result.data.shape == (1, 1)
    assert result.data.dims == (DataDimension.CURVE, DataDimension.MDR)
    assert result.data.data[0, 0] == 10_000