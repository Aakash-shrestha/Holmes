from holmes.tools.base import Tool


def make_inspect_tool(df):
    def inspect_tool():
        sections = [
            f"shape: {df.shape}",
            f"\ndtypes:\n{df.dtypes}",
            f"\nmissing_values:\n{df.isna().sum()}",
            f"\ndescribe:\n{df.describe()}",
            f"\nhead:\n{df.head()}",
        ]
        return "\n".join(sections)

    return Tool(
        name="inspect_data",
        description="Inspect the DataFrame to get its shape, data types, missing values, descriptive statistics, and first few rows.",
        parameters={},
        func=inspect_tool,
    )
