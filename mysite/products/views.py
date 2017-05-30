from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AuditData
from django.shortcuts import render
from django.db import connection
import json
import MySQLdb
from django.views.decorators.csrf import csrf_exempt

# import yaml



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
@csrf_exempt
def AuditDataDeleteHandler(requests):

    body_unicode = requests.body.decode('utf-8')
    bodyArray = json.loads(body_unicode)

    for body in bodyArray:
        c = ""
        host_id = body["host_id"]
        try:
            c = connection.cursor()
            c.execute("call usp_AuditDataDelete(%s)", [host_id]);
        except Exception as e:
            print e
        finally:
            c.close()
    return HttpResponse("Deleted successfully")

@csrf_exempt
def AuditDataUpdateHandler(requests):
    body_unicode = requests.body.decode('utf-8')
    bodyArray = json.loads(body_unicode)

    for body in bodyArray:
        c = ""
        host_id	= body['host_id'],
        config_Validation	= body["Config_Validation"],
        config_Validation_Review	= body["Config_Validation_Review"],
        template_Creation	= body["Template_Creation"],
        cms	= body["CMS"],
        remediation	= body["Remediation"],
        monitoring	= body["Monitoring"],
        global_Server_Config	= body["Global_Server_Config"],
        server_Port	= body["Server_Port"],
        healthcheck	= body["Healthcheck"],
        real_Server	= body["Real_Server"],
        virtual_Server	= body["Virtual_Server"],
        service_Group	= body["Service_Group"],
        server_Vip_Group	= body["Server_Vip_Group"],
        config_Sync	= body["Config_Sync"],
        service	= body["Service"],
        logging_Local	= body["Logging_Local"],
        logging_Remote	= body["Logging_Remote"],
        username = body["Username"],
        aaa	= body["Aaa"],
        nat	= body["Nat"],
        match_List	= body["Match_List"],
        control_Plane	= body["Control_Plane"],
        ip_Host	= body["Ip_Host"],
        ssh	= body["Ssh"],
        spanning_Tree	= body["Spanning_Tree"],
        access_List	= body["Access_List"],
        prefix_List	= body["Prefix_List"],
        vlan	= body["Vlan"],
        interfaces	= body["Interfaces"],
        default_Gateway	= body["Default_Gateway"],
        static_Routes	= body["Static_Routes"],
        ospf	= body["Ospf"],
        bgp	= body["Bgp"],
        route_Map	= body["Route_Map"],
        route_Policy	= body["Route_Policy"],
        as_Path_Set	= body["As_Path_Set"],
        community	= body["Community"],
        snmp	= body["Snmp"],
        accounting_Authorization	= body["Accounting_Authorization"],
        tacacs	= body["Tacacs"],
        banner	= body["Banner"],
        line_Con	= body["Line_Con"],
        monitor	= body["Monitor"],
        ntp	= body["Ntp"],
        gre	= body["Gre"],
        not_Started_	= body["Not_Started_"],
        in_Progress	= body["In_Progress"],
        complete	= body["Complete"],
        process_Not_Started	= body["Process_Not_Started"],
        process_In_Progress	= body["Process_In_Progress"],
        process_Complete	= body["Process_Complete"],
        not_Started	= body["Not_Started"],
        in_Progress_NAV	= body["In_Progress_NAV"],
        in_Progress_MALT	= body["In_Progress_MALT"],
        completed	= body["Completed"]

        try:
            c = connection.cursor()
            c.execute("call usp_AuditDataUpdate(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [host_id,config_Validation,config_Validation_Review,template_Creation,cms,remediation,monitoring,global_Server_Config,server_Port,healthcheck,real_Server,virtual_Server,service_Group,server_Vip_Group,config_Sync,service,logging_Local,logging_Remote,username,aaa,nat,match_List,control_Plane,ip_Host,ssh,spanning_Tree,access_List,prefix_List,vlan,interfaces,default_Gateway,static_Routes,ospf,bgp,route_Map,route_Policy,as_Path_Set,community,snmp,accounting_Authorization,tacacs,banner,line_Con,monitor,ntp,gre,not_Started_,in_Progress,complete,process_Not_Started,process_In_Progress,process_Complete,not_Started,in_Progress_NAV,in_Progress_MALT,completed]);
        except Exception as e:
            print e
        finally:
            c.close()
    return HttpResponse("Successfully saved")


# def testviewHandler(request,AuditData):
#     post=AuditData.objects.all()
#     return render(request,'/products/templates/auditTracking/index.html')