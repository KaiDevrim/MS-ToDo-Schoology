import schoolopy

from dotenv import load_dotenv
import os
load_dotenv()

sc = schoolopy.Schoology(schoolopy.Auth(
    os.getenv("schoolKey"), os.getenv("schoolSecret")))
sc.limit = 10  # Only retrieve 10 objects max
