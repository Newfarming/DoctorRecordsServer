import pymysql, json
from DoctorRecordsServerApp.models import DoctorInfo, Department, NewTechAward, NewTechResearch, OutTable, \
    ObtainPatents, ProfessionalTitle, ResearchProject, ResearchAward, ResearchPapers, StudyTable


def doctorRelationshipDelete(data_dict):
    NewTechAward.objects.filter(**data_dict).delete()
    NewTechResearch.objects.filter(**data_dict).delete()
    OutTable.objects.filter(**data_dict).delete()
    ObtainPatents.objects.filter(**data_dict).delete()
    ProfessionalTitle.objects.filter(**data_dict).delete()
    ResearchAward.objects.filter(**data_dict).delete()
    ResearchPapers.objects.filter(**data_dict).delete()
    ResearchProject.objects.filter(**data_dict).delete()
    StudyTable.objects.filter(**data_dict).delete()


def studyTableInfo(data_dict):
    return StudyTable.objects.filter(**data_dict).first()


def insertStudyTable(data_dict):
    StudyTable.objects.create(**data_dict)


def deleteStudyTable(nid):
    StudyTable.objects.filter(id=nid).delete()


def editStudyTable(nid, data_dict):
    StudyTable.objects.filter(id=nid).update(**data_dict)


def studyTableList(data_dict):
    data_set = StudyTable.objects.filter(**data_dict)
    return data_set


def researchPapersInfo(data_dict):
    return ResearchPapers.objects.filter(**data_dict).first()


def insertResearchPapers(data_dict):
    ResearchPapers.objects.create(**data_dict)


def deleteResearchPapers(nid):
    ResearchPapers.objects.filter(id=nid).delete()


def editResearchPapers(nid, data_dict):
    ResearchPapers.objects.filter(id=nid).update(**data_dict)


def researchPapersList(data_dict):
    data_set = ResearchPapers.objects.filter(**data_dict)
    return data_set


def ResearchAwardInfo(data_dict):
    return ResearchProject.objects.filter(**data_dict).first()


def researchAwardInfo(data_dict):
    return ResearchAward.objects.filter(**data_dict).first()


def insertResearchAward(data_dict):
    ResearchAward.objects.create(**data_dict)


def deleteResearchAward(nid):
    ResearchAward.objects.filter(id=nid).delete()


def editResearchAward(nid, data_dict):
    ResearchAward.objects.filter(id=nid).update(**data_dict)


def researchAwardList(data_dict):
    data_set = ResearchAward.objects.filter(**data_dict)
    return data_set


def ResearchAwardInfo(data_dict):
    return ResearchProject.objects.filter(**data_dict).first()


def insertResearchProject(data_dict):
    ResearchProject.objects.create(**data_dict)


def deleteResearchProject(nid):
    ResearchProject.objects.filter(id=nid).delete()


def editResearchProject(nid, data_dict):
    ResearchProject.objects.filter(id=nid).update(**data_dict)


def researchProjectList(data_dict):
    data_set = ResearchProject.objects.filter(**data_dict)
    return data_set


def professionalTitleInfo(data_dict):
    return ProfessionalTitle.objects.filter(**data_dict).first()


def insertProfessionalTitle(data_dict):
    ProfessionalTitle.objects.create(**data_dict)


def deleteProfessionalTitle(nid):
    ProfessionalTitle.objects.filter(id=nid).delete()


def editProfessionalTitle(nid, data_dict):
    ProfessionalTitle.objects.filter(id=nid).update(**data_dict)


def professionalTitleList(data_dict):
    data_set = ProfessionalTitle.objects.filter(**data_dict)
    return data_set


def obtainPatentsInfo(data_dict):
    return ObtainPatents.objects.filter(**data_dict).first()


def insertObtainPatents(data_dict):
    ObtainPatents.objects.create(**data_dict)


def deleteObtainPatents(nid):
    ObtainPatents.objects.filter(id=nid).delete()


def editObtainPatents(nid, data_dict):
    ObtainPatents.objects.filter(id=nid).update(**data_dict)


def obtainPatentsList(data_dict):
    data_set = ObtainPatents.objects.filter(**data_dict)
    return data_set


def outTableInfo(data_dict):
    return OutTable.objects.filter(**data_dict).first()


def insertOutTable(data_dict):
    OutTable.objects.create(**data_dict)


def deleteOutTable(nid):
    OutTable.objects.filter(id=nid).delete()


def editOutTable(nid, data_dict):
    OutTable.objects.filter(id=nid).update(**data_dict)


def outTableList(data_dict):
    data_set = OutTable.objects.filter(**data_dict)
    return data_set


def newTechResearchInfo(data_dict):
    return NewTechResearch.objects.filter(**data_dict).first()


def insertNewTechResearch(data_dict):
    NewTechResearch.objects.create(**data_dict)


def deleteNewTechResearch(nid):
    NewTechResearch.objects.filter(id=nid).delete()


def editNewTechResearch(nid, data_dict):
    NewTechResearch.objects.filter(id=nid).update(**data_dict)


def newTechResearchList(data_dict):
    data_set = NewTechResearch.objects.filter(**data_dict)
    return data_set


def newTechAwardInfo(data_dict):
    return NewTechAward.objects.filter(**data_dict).first()


def insertNewTechAward(data_dict):
    NewTechAward.objects.create(**data_dict)


def deleteNewTechAward(nid):
    NewTechAward.objects.filter(id=nid).delete()


def editNewTechAward(nid, data_dict):
    NewTechAward.objects.filter(id=nid).update(**data_dict)


def newTechAwardList(data_dict):
    data_set = NewTechAward.objects.filter(**data_dict)
    return data_set


def connect_db():
    db = pymysql.connect(host="localhost", user="root", password="abcddjs921005", db="DoctorRecordsDatabase",
                         charset="utf8")
    cursor = db.cursor()
    return db, cursor


def userInfo(data_dict):
    return DoctorInfo.objects.filter(**data_dict).first()


def insertUser(data_dict):
    DoctorInfo.objects.create(**data_dict)
    return DoctorInfo.objects.filter(**data_dict).first()


def deleteUser(nid):
    return DoctorInfo.objects.filter(id=nid).delete()


def editUser(nid, data_dict):
    DoctorInfo.objects.filter(id=nid).update(**data_dict)


def userList(data_dict, type_dict):
    # user_set = {}
    data_temp = {}
    print('data_dict')
    print(str(data_dict))
    if ('search' in data_dict) or ('search' in type_dict):
        if 'search' in data_dict:
            data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        if 'search' in type_dict:
            data_temp[type_dict["search_type"] + '__contains'] = type_dict["search"]
        user_set = DoctorInfo.objects.filter(**data_temp)
    else:
        user_set = DoctorInfo.objects.all()
    # user_set = user_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return user_set


def departInfo(data_dict):
    return Department.objects.filter(**data_dict).first()


def insertDepart(data_dict):
    Department.objects.create(**data_dict)


def deleteDepart(nid):
    Department.objects.filter(id=nid).delete()


def editDepart(nid, data_dict):
    Department.objects.filter(id=nid).update(**data_dict)


def departList(data_dict):
    data_temp = {}
    if 'search' in data_dict:
        data_temp[data_dict["search_type"] + '__contains'] = data_dict["search"]
        depart_set = Department.objects.filter(**data_temp)
    else:
        depart_set = Department.objects.all()
    # depart_set = depart_set[slice(int(data_dict['pageStart']), int(data_dict['pageStart'])+int(data_dict['pagesize']))]
    return depart_set


def saveImg(request):
    new_img = Avatar(
        photo=request.FILES.get('photo'),  # 拿到图片
        user=request.FILES.get('photo').name  # 拿到图片的名字
    )
    new_img.save()  # 保存图片