from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
import os



# engine=create_engine("postgresql://xvbxecklfindav:4f5a1d204c2188a414f36ee4838616b3c1482d8f4f26a972aacef3bc29a449a0@ec2-34-233-115-14.compute-1.amazonaws.com:5432/d3ej94n4em2egg")


# engine=create_engine("postgresql://fvciisfzvmwxyw:69769d7f8ea33d4a4a90029b018460c8f1925ecedf41801d4b84d36f526c2890@ec2-3-225-110-188.compute-1.amazonaws.com:5432/d3ambe67es0omc")
engine=create_engine("postgresql://rqgkervwgdcqxm:fc86873346941c7daac7f47a8d30cd104216b4906ba1945d0c7da114cce68fdd@ec2-52-70-86-157.compute-1.amazonaws.com:5432/d8g4g2v64kji04")

# engine=create_engine("postgresql+psycopg2://postgres:ali123@localhost:5432/Employee",echo=True)

# engine=create_engine(f"{os.getenv('DB_NAME')}://)",echo=True)

SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()


