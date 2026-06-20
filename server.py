import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CurrencyConverterBridge")

@mcp.tool()
async def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str
) -> str:
    """
    Convert currency using OutSystems Currency API.
    """

    outsystems_endpoint = (
        "https://personal-lo6oktnu.outsystemscloud.com/"
        "Converter/rest/internalMCP/ConvertCurrency"
    )

    payload = {
        "Amount": amount,
        "FromCurrency": from_currency,
        "ToCurrency": to_currency
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            outsystems_endpoint,
            json=payload,
            timeout=20
        )

        response.raise_for_status()

        return response.text


