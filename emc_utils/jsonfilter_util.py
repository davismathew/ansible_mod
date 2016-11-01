
from ansible import errors
from emc_utils.parseutils import construct_var
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class JSONFilter(object):
    def compare_json(self,variableb, variablea, argslist, command):
        flag = True
        retdict={}
        list=[]
        olddict={}
        newdict={}
        nestlist=[]

        if not variableb:
            return "second command o/p empty"
        elif not variablea:
            return "first command o/p empty"

        for element in argslist:
            for i,val in enumerate(variablea):
                try:
                   if str(variablea[i][element]).encode("utf-8").strip() != str(variableb[i][element]).encode("utf-8").strip():
                        flag = False
                        list.append(construct_var(variableb[i],variablea[i],command))
                except Exception, err:
                    return str(err)
            if(len(list)>0):
                retdict["before,after"] = list
                list=[]


        if(flag):
            return "Success"
        else:
            return retdict

        return flag


def main(self):
    return "something"







