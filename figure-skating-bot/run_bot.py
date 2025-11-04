import asyncio
from src.main import main
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())