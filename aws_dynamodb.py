__author__ = 'jbantupa'

import boto.dynamodb2
from boto.dynamodb2.table import Table

def connect_dynamodb():
    connection=boto.dynamodb2.connect_to_region("us-west-1",aws_access_key_id="AKIAIUNBOSGUIOOHW6CQ",aws_secret_access_key="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")
    return connection

def write_record(data_record):
    conn=connect_dynamodb()
    mtable=Table("movie_data",connection=conn)
    mtable.put_item(data_record)

def write_record_batch(record_list):
    # if len(record_list)>25:
    #     print "25 is the batch limit; please try with < 25 items"
    #     return
    conn=connect_dynamodb()
    mtable=Table("movie_data",connection=conn)
    with mtable.batch_write() as batch:
        for rec in record_list:
            batch.put_item(rec)

    print batch._unprocessed
    conn.close()

def delete_movie(mname, year):
    conn=connect_dynamodb()
    mtable=Table("movie_data",connection=conn)

    delete_status=mtable.delete_item(moviename=mname,releaseyear=year)

    conn.close()
    return delete_status

def delete_movie_batch(movie_list):
    conn=connect_dynamodb()

    mtable=Table("movie_data",connection=conn)

    with mtable.batch_write() as batch:
        for rec in movie_list:
            batch.delete_item(moviename=rec["moviename"],releaseyear=rec["releaseyear"])

    print batch._unprocessed
    conn.close()

def main():
    conn=connect_dynamodb()
    mtable=Table("movie_data",connection=conn)
    print mtable.count()

if __name__ == "__main__":
    main()

