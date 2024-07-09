import pymysql, json
from MedInsNoPaperApp.models import UserInfo, MedInsInfo


def userInfo(data_dict):
    return UserInfo.objects.filter(**data_dict).first()


def insertUser(data_dict):
    UserInfo.objects.create(**data_dict)


def deleteUser(nid):
    UserInfo.objects.filter(id=nid).delete()


def editUser(nid, data_dict):
    UserInfo.objects.filter(id=nid).update(**data_dict)


def userList(data_dict):
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        user_set = UserInfo.objects.filter(**data_temp)
    else:
        user_set = UserInfo.objects.all()
    # depart_set = depart_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return user_set


def MedInsInfo(data_dict):
    return MedInsInfo.objects.filter(**data_dict).first()


def insertMedIns(data_dict):
    MedInsInfo.objects.create(**data_dict)


def deleteMedIns(nid):
    MedInsInfo.objects.filter(id=nid).delete()


def editMedIns(nid, data_dict):
    MedInsInfo.objects.filter(id=nid).update(**data_dict)


def MedInsList(data_dict):
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        medins_set = MedInsInfo.objects.filter(**data_temp)
    else:
        medins_set = MedInsInfo.objects.all()
    # depart_set = depart_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return medins_set
