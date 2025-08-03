import fal_client
import os, dotenv

dotenv.load_dotenv()
os.getenv("FAL_KEY")

handler = fal_client.submit(
    "fal-ai/flux/dev",
    arguments={
        "prompt": "photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"
    },
)

result = handler.get()
print(result)
