from asyncflows import AsyncFlows


async def main():
    query = input("Provide a problem to think about: ")
    flow = AsyncFlows.from_file("debono.yaml").set_vars(
        query=query,
    )

    # Run the flow and return the default output (result of the blue hat)
    result = await flow.run()
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
