import argparse

import pandas as pd
from google.genai import Client

from holmes import config
from holmes.agent.loop import run


def main():
    parser = argparse.ArgumentPaser(
        description="Holmes: A tool for analyzing and visualizing data."
    )

    parser.add_argument("data_path")
    parser.add_argument("goal")
    args = parser.parse_args()

    df = pd.read_csv(args.data_path)

    client = Client(api_key=config.API_KEY)

    result = run(client, df, args.goal)

    print(result)


if __name__ == "__main__":
    main()
