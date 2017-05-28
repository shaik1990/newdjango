from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AuditData
from django.shortcuts import render
from django.db import connection
import json
import MySQLdb
import yaml



def AuditDataHandler(requests):
    c = ""
    results = []
    product_id = requests.GET.get("product_id")
    try:
        c = connection.cursor()
        c.execute("call usp_Audit_DataByProductIdGet(%s)", [product_id]);
        results = list(dictfetchall(c))
    except Exception as e:
        print e
    finally:
        c.close()
    return HttpResponse(results)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]

    # columns=yaml.safe_load(json.dumps(columns))

    return[
    json.dumps([dict(zip([str(i) for i in columns], [str(i) for i in row])) for row in cursor.fetchall()])

        #json.dumps([dict(zip([str(i) for i in columns], [str(i) for i in row])) for row in cursor.fetchall()])

    ]



####-----------------------    [dict(zip([str(i) for i in columns], [str(i) for i in row])) for row in cursor.fetchall()]

    #[json.dumps(dict(zip([str(i) for i in columns], [str(i) for i in row])), ensure_ascii=False)
    #for row in cursor.fetchall()]

#    test = [json.dumps(dict(zip([str(i) for i in columns], [str(i) for i in row])), ensure_ascii=False) + ','
#    for row in cursor.fetchall()]

#    json.dumps([dict(zip([str(i) for i in columns], [str(i) for i in row])) for row in cursor.fetchall()])

#    return [
        #dict(zip([str(i) for i in columns], [str(i) for i in row]))
#        json.dumps(dict(zip([str(i) for i in columns], [str(i) for i in row])), ensure_ascii=False) + ','
#        for row in cursor.fetchall()


        #dict(zip([str(i) for i in columns], [str(i) for i in row]))
        #[{k,v} for k ,v in dict(zip([str(i) for i in columns], [str(i) for i in row]))]
        # json.dumps(
        #     [':'.join([{str(k),str(v)}]) for k ,v in dict(zip([str(i) for i in columns], [str(i) for i in row])).items()]
        #     ,indent=4
        # )


    #     values = [{"file_name": k, "file_information": v} for k, v in dict_.items()]
    # json.dumps(values, indent=4)

#    ]

