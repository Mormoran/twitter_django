import os

# Twitter access keys
os.environ.setdefault('CONSUMER_KEY', 'xz6iX3TdkL2TFmmrSXvARvJkn')
os.environ.setdefault('CONSUMER_SECRET', '71na1NQVNzwibLQso6S3A1mIxs8LD5Uqzu3me1wCLoTmUFlnva')
os.environ.setdefault('ACCESS_TOKEN', '381284132-3TSKLn9rAixDNYJOEvUQXa46Sww238zkkpvRCBZZ')
os.environ.setdefault('ACCESS_TOKEN_SECRET', 'M1kWjy6Ed8vzqW8g9tGieOecEbGbkxgquKlskdj1dpuMW')

# Django secret key
os.environ.setdefault("SECRET_KEY", "0dj=x79pfud(=r4&0e3p5yz7od65(t07^u_(h$%@txvxr@$7ol")
os.environ.setdefault("DEBUG", "True")

# # Heroku postgres access URI
# os.environ.setdefault("DATABASE_URL", "postgres://wxoguozjgnnuqt:e481addeee091eabdb9003a1cef1f3b9ca4452aa37ac115a9b5544c32e283486@ec2-79-125-13-42.eu-west-1.compute.amazonaws.com:5432/dal2m8n6gntg9f")

# # AWS/IAM access keys
os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "mytweetdash")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "AKIAIZXHQJNW64EVENMA")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "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")

# # mLAB access keys
os.environ.setdefault("MONGODB_URI", "mongodb://heroku_0bjjx80q:mrairpl7g754s5ir1935a8gros@ds149122.mlab.com:49122/heroku_0bjjx80q")