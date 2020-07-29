def shorten_to_date(long_date):
    return long_date.rsplit(",")[0] # or return long_date.rpartition(",")[0] 