"""Tests for llm utility functionality"""
import pyarrow as pa
import pytest

from mp_blog.llm_utils import enforce_data_contract, DataContractError


@pytest.mark.parametrize(
    'res,expected_schema,ExpectedException',
    [
        (
            '''[
    {
        "oy": "schlamiel",
        "vey": "schmlamaze"
    }
]''',
            pa.schema([
                pa.field('oy', pa.string()),
                pa.field('vey', pa.string())
            ]),
            None
        ),
          ("As an AI model, I don't know jack (or jill)",
            pa.schema([
                pa.field('oy', pa.string()),
                pa.field('vey', pa.string())
            ]),
            DataContractError
        ),
         (
            '''[
    {
        "1": {"oy": "schlamiel", "vey": "schmlamaze"}
    }
]''',
            pa.schema([
                pa.field('oy', pa.string()),
                pa.field('vey', pa.string())
            ]),
            DataContractError
        ),
    ]
)
def test_enforce_data_contract(res: str, expected_schema: pa.schema, ExpectedException: Exception):
    if ExpectedException is None:
        enforce_data_contract(res, expected_schema)
    else:
        with pytest.raises(ExpectedException):
            enforce_data_contract(res, expected_schema)
