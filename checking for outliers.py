upper_limit=212
lower_limit=156
outlier=False
number=120

if number> upper_limit:
    outlier=True
if number< lower_limit:
    outlier=True
if outlier== True:
    print(f"{number} is an outlier")
